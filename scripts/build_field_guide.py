#!/usr/bin/env python3
"""Build the public DOCX field guide and a PDF companion from Markdown.

The Markdown source remains the editable public source of truth. The generated
editions add a Word TOC field, page numbers, and repeated lightweight authorship
markers requested for the distributable guide.
"""

from __future__ import annotations

import re
import shutil
import subprocess
import tempfile
from pathlib import Path

from docx import Document
from pypdf import PdfReader
from docx.enum.section import WD_SECTION
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT, WD_TAB_LEADER
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs" / "agentic-systems-field-guide.md"
OUTPUT_DIR = ROOT / "docs" / "downloads"
DOCX_OUT = OUTPUT_DIR / "Agentic-System-Building-Guide.docx"
PDF_OUT = OUTPUT_DIR / "Agentic-System-Building-Guide.pdf"
CONCEPT_MAP = ROOT / "harness-concept-map.png"
EXAMPLE_MAP = ROOT / "anonymised-agent-system-map.png"


def set_cell_border(*_args, **_kwargs):
    """Reserved for future table formatting without expanding public dependencies."""


def add_field(paragraph, instruction: str) -> None:
    run = paragraph.add_run()
    begin = OxmlElement("w:fldChar")
    begin.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = instruction
    separate = OxmlElement("w:fldChar")
    separate.set(qn("w:fldCharType"), "separate")
    text = OxmlElement("w:t")
    text.text = "1"
    separate.append(text)
    end = OxmlElement("w:fldChar")
    end.set(qn("w:fldCharType"), "end")
    run._r.extend([begin, instr, separate, end])


def shade(paragraph, fill: str) -> None:
    props = paragraph._p.get_or_add_pPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), fill)
    props.append(shd)


def add_header_footer(section) -> None:
    section.top_margin = Cm(2.0)
    section.bottom_margin = Cm(1.7)
    section.left_margin = Cm(2.15)
    section.right_margin = Cm(2.15)

    section.header.is_linked_to_previous = False
    section.footer.is_linked_to_previous = False
    header = section.header.paragraphs[0]
    header.alignment = WD_ALIGN_PARAGRAPH.CENTER
    header_run = header.add_run("@kwis7")
    header_run.font.name = "Arial"
    header_run.font.size = Pt(7.5)
    header_run.font.color.rgb = RGBColor(190, 190, 190)

    footer = section.footer.paragraphs[0]
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    footer_run = footer.add_run("@kwis7  ·  ")
    footer_run.font.name = "Arial"
    footer_run.font.size = Pt(8)
    footer_run.font.color.rgb = RGBColor(135, 135, 135)
    add_field(footer, "PAGE")


def add_cover(doc: Document) -> None:
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(96)
    r = p.add_run("BUILDING A\nPORTABLE AGENT HARNESS")
    r.bold = True
    r.font.name = "Arial"
    r.font.size = Pt(28)
    r.font.color.rgb = RGBColor(33, 66, 100)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("A textbook and practical workbook for understanding,\ndesigning, implementing, and verifying agentic systems")
    r.italic = True
    r.font.size = Pt(14)
    r.font.color.rgb = RGBColor(91, 105, 120)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(42)
    r = p.add_run("@kwis7\ngithub.com/kwis7")
    r.bold = True
    r.font.size = Pt(13)
    r.font.color.rgb = RGBColor(33, 66, 100)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(36)
    r = p.add_run("Version 2.1 textbook draft  |  9 August 2026")
    r.font.size = Pt(10)
    r.font.color.rgb = RGBColor(115, 115, 115)


def toc_entries() -> list[str]:
    return [
        line[2:].strip()
        for line in SOURCE.read_text(encoding="utf-8").splitlines()
        if line.startswith("# Part ") or line.startswith("# Appendix ")
    ]


def add_hyperlink(paragraph, text: str, anchor: str) -> None:
    hyperlink = OxmlElement("w:hyperlink")
    hyperlink.set(qn("w:anchor"), anchor)
    hyperlink.set(qn("w:history"), "1")
    run = OxmlElement("w:r")
    properties = OxmlElement("w:rPr")
    color = OxmlElement("w:color")
    color.set(qn("w:val"), "214264")
    underline = OxmlElement("w:u")
    underline.set(qn("w:val"), "single")
    size = OxmlElement("w:sz")
    size.set(qn("w:val"), "22")
    properties.extend([color, underline, size])
    run.append(properties)
    content = OxmlElement("w:t")
    content.text = text
    run.append(content)
    hyperlink.append(run)
    paragraph._p.append(hyperlink)


def add_bookmark(paragraph, name: str, bookmark_id: int) -> None:
    start = OxmlElement("w:bookmarkStart")
    start.set(qn("w:id"), str(bookmark_id))
    start.set(qn("w:name"), name)
    end = OxmlElement("w:bookmarkEnd")
    end.set(qn("w:id"), str(bookmark_id))
    paragraph._p.insert(0, start)
    paragraph._p.append(end)


def add_toc(doc: Document, page_refs: dict[str, int] | None = None) -> None:
    title = doc.add_paragraph()
    title.style = "Heading 1"
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title.paragraph_format.space_before = Pt(22)
    title.paragraph_format.space_after = Pt(24)
    title.add_run("Contents")
    current_group = None
    for index, entry in enumerate(toc_entries(), start=1):
        group = "Reference appendices" if entry.startswith("Appendix ") else "Core chapters"
        if group != current_group:
            label = doc.add_paragraph()
            label.paragraph_format.space_before = Pt(14 if current_group else 0)
            label.paragraph_format.space_after = Pt(5)
            label.paragraph_format.left_indent = Cm(0.45)
            label_run = label.add_run(group.upper())
            label_run.bold = True
            label_run.font.name = "Arial"
            label_run.font.size = Pt(9)
            label_run.font.color.rgb = RGBColor(91, 105, 120)
            current_group = group
        toc = doc.add_paragraph()
        toc.paragraph_format.space_before = Pt(5)
        toc.paragraph_format.space_after = Pt(5)
        toc.paragraph_format.line_spacing = 1.2
        toc.paragraph_format.left_indent = Cm(0.45)
        toc.paragraph_format.right_indent = Cm(0.45)
        toc.paragraph_format.tab_stops.add_tab_stop(Cm(15.0), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS)
        add_hyperlink(toc, entry, f"section-{index}")
        page = page_refs.get(entry, "-") if page_refs else "-"
        toc.add_run("\t")
        page_run = toc.add_run(str(page))
        page_run.bold = True
        page_run.font.name = "Arial"
        page_run.font.size = Pt(10.5)
        page_run.font.color.rgb = RGBColor(33, 66, 100)
    note = doc.add_paragraph()
    note.paragraph_format.space_before = Pt(18)
    note.paragraph_format.space_after = Pt(0)
    note.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = note.add_run("Entries are linked to their sections. Page numbers are generated from the PDF layout.")
    run.italic = True
    run.font.size = Pt(9)
    run.font.color.rgb = RGBColor(125, 125, 125)


def configure_styles(doc: Document) -> None:
    styles = doc.styles
    normal = styles["Normal"]
    normal.font.name = "Arial"
    normal.font.size = Pt(10.5)
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.line_spacing = 1.18
    for name, size, color in [
        ("Title", 25, RGBColor(33, 66, 100)),
        ("Heading 1", 17, RGBColor(33, 66, 100)),
        ("Heading 2", 13, RGBColor(46, 92, 129)),
        ("Heading 3", 11.5, RGBColor(58, 99, 134)),
    ]:
        style = styles[name]
        style.font.name = "Arial"
        style.font.size = Pt(size)
        style.font.bold = True
        style.font.color.rgb = color
        style.paragraph_format.space_before = Pt(16 if name != "Title" else 0)
        style.paragraph_format.space_after = Pt(7)
        style.paragraph_format.keep_with_next = True

    if "Quote" not in styles:
        quote = styles.add_style("Quote", WD_STYLE_TYPE.PARAGRAPH)
        quote.font.italic = True


def clean_inline(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = text.replace("**", "").replace("`", "").replace("*", "")
    return (
        text.replace("\u2010", "-")
        .replace("\u2011", "-")
        .replace("\u2012", "-")
        .replace("\u2013", "-")
        .replace("\u2014", "-")
        .replace("\u2015", "-")
        .replace("\u2018", "'")
        .replace("\u2019", "'")
        .replace("\u201c", '"')
        .replace("\u201d", '"')
        .replace("\u00a0", " ")
    )


def parse_table(lines: list[str], start: int):
    rows = []
    idx = start
    while idx < len(lines) and lines[idx].lstrip().startswith("|"):
        parts = [clean_inline(cell.strip()) for cell in lines[idx].strip().strip("|").split("|")]
        if not all(re.fullmatch(r"[: -]+", cell) for cell in parts):
            rows.append(parts)
        idx += 1
    return rows, idx


def add_table(doc: Document, rows: list[list[str]]) -> None:
    if not rows:
        return
    table = doc.add_table(rows=len(rows), cols=max(len(row) for row in rows))
    table.style = "Light Shading Accent 1"
    table.autofit = True
    for row_idx, row in enumerate(rows):
        for col_idx, value in enumerate(row):
            cell = table.cell(row_idx, col_idx)
            cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            cell.text = value
            for paragraph in cell.paragraphs:
                for run in paragraph.runs:
                    run.font.size = Pt(8.5)
                    if row_idx == 0:
                        run.bold = True


def add_map_page(doc: Document, title_text: str, image_path: Path, caption_text: str) -> None:
    """Insert one print-friendly diagram page before the textbook."""
    title = doc.add_paragraph(title_text, style="Heading 1")
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    if image_path.exists():
        image = doc.add_paragraph()
        image.alignment = WD_ALIGN_PARAGRAPH.CENTER
        image.add_run().add_picture(str(image_path), width=Cm(16.6))
    caption = doc.add_paragraph()
    caption.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = caption.add_run(caption_text)
    run.italic = True
    run.font.size = Pt(9)
    run.font.color.rgb = RGBColor(95, 95, 95)
    doc.add_page_break()


def add_markdown_content(doc: Document) -> None:
    lines = SOURCE.read_text(encoding="utf-8").splitlines()
    in_code = False
    code_lines: list[str] = []
    idx = 0
    bookmark_id = 1
    while idx < len(lines):
        raw = lines[idx]
        line = raw.rstrip()
        if line.startswith("Author:") or line.startswith("Repository:") or line.startswith("Edition:") or line.startswith("Generated:"):
            idx += 1
            continue
        if line.startswith("```"):
            if in_code:
                p = doc.add_paragraph(style="No Spacing")
                p.paragraph_format.left_indent = Cm(0.5)
                p.paragraph_format.space_after = Pt(8)
                shade(p, "F2F5F7")
                run = p.add_run("\n".join(code_lines))
                run.font.name = "Courier New"
                run.font.size = Pt(8.5)
                code_lines = []
                in_code = False
            else:
                in_code = True
            idx += 1
            continue
        if in_code:
            code_lines.append(raw)
            idx += 1
            continue
        if line.lstrip().startswith("|"):
            rows, idx = parse_table(lines, idx)
            add_table(doc, rows)
            continue
        if not line.strip():
            idx += 1
            continue
        if re.match(r"^#{4,6} ", line):
            heading = clean_inline(re.sub(r"^#{4,6} ", "", line))
            paragraph = doc.add_paragraph()
            paragraph.paragraph_format.space_before = Pt(9)
            paragraph.paragraph_format.space_after = Pt(3)
            run = paragraph.add_run(heading)
            run.bold = True
            run.font.color.rgb = RGBColor(58, 99, 134)
        elif line.startswith("### "):
            doc.add_paragraph(clean_inline(line[4:]), style="Heading 3")
        elif line.startswith("## "):
            heading = clean_inline(line[3:])
            doc.add_paragraph(heading, style="Heading 2")
        elif line.startswith("# "):
            heading = clean_inline(line[2:])
            if heading == "Building a Portable Agent Harness":
                idx += 1
                continue
            if heading.startswith("Part ") or heading.startswith("Appendix "):
                paragraph = doc.add_paragraph(heading, style="Heading 1")
                paragraph.paragraph_format.page_break_before = True
                add_bookmark(paragraph, f"section-{bookmark_id}", bookmark_id)
                bookmark_id += 1
            else:
                doc.add_paragraph(heading, style="Heading 1")
        elif line.startswith("> "):
            p = doc.add_paragraph(clean_inline(line[2:]), style="Quote")
            shade(p, "EEF3F7")
        elif re.match(r"^[-*] ", line):
            doc.add_paragraph(clean_inline(line[2:]), style="List Bullet")
        elif re.match(r"^\d+\. ", line):
            paragraph = doc.add_paragraph(clean_inline(line))
            paragraph.paragraph_format.left_indent = Cm(0.45)
            paragraph.paragraph_format.first_line_indent = Cm(-0.35)
        elif line == "---":
            pass
        elif line.startswith("!"):
            image = ROOT / "docs" / "assets" / "anonymised-agent-system-map.png"
            if image.exists():
                p = doc.add_paragraph()
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.add_run().add_picture(str(image), width=Cm(15.5))
        else:
            doc.add_paragraph(clean_inline(line))
        idx += 1


def build_docx(page_refs: dict[str, int] | None = None) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    doc = Document()
    configure_styles(doc)
    add_header_footer(doc.sections[0])
    doc.core_properties.author = "@kwis7"
    doc.core_properties.title = "Building a Portable Agent Harness"
    doc.core_properties.subject = "A practical field guide for agentic systems"
    doc.core_properties.comments = "Authored by @kwis7."
    add_cover(doc)
    toc_section = doc.add_section(WD_SECTION.NEW_PAGE)
    add_header_footer(toc_section)
    add_toc(doc, page_refs)
    body_section = doc.add_section(WD_SECTION.NEW_PAGE)
    add_header_footer(body_section)
    add_map_page(
        doc,
        "Harness concept map",
        CONCEPT_MAP,
        "The active model is visible and replaceable. Every configured component and relationship around execution belongs to the harness; only a central coordinating model in a multi-agent topology is the manager.",
    )
    add_map_page(
        doc,
        "An anonymised example system",
        EXAMPLE_MAP,
        "A control center routes work to functional owner agents. Methods may be shared deliberately, while raw data, private memory, task state, and reviewed outputs remain with their owners.",
    )
    add_markdown_content(doc)
    doc.save(DOCX_OUT)


def build_pdf() -> None:
    soffice = shutil.which("soffice")
    if not soffice:
        raise RuntimeError("soffice is required to create the PDF edition")
    with tempfile.TemporaryDirectory() as temp:
        profile = Path(temp) / "libreoffice-profile"
        subprocess.run(
            [
                soffice,
                f"-env:UserInstallation={profile.as_uri()}",
                "--headless",
                "--convert-to",
                "pdf",
                "--outdir",
                temp,
                str(DOCX_OUT),
            ],
            check=True,
            text=True,
            capture_output=True,
        )
        generated = Path(temp) / (DOCX_OUT.stem + ".pdf")
        if not generated.exists():
            raise RuntimeError("PDF conversion completed without a PDF output")
        shutil.copy2(generated, PDF_OUT)


def discover_section_pages() -> dict[str, int]:
    pages: dict[str, int] = {}
    reader = PdfReader(str(PDF_OUT))
    body_start = 0
    for page_no, page in enumerate(reader.pages, start=1):
        text = re.sub(r"\s+", " ", page.extract_text() or "")
        if "Harness concept map" in text:
            body_start = page_no
            break
    for page_no, page in enumerate(reader.pages, start=1):
        if page_no <= body_start:
            continue
        text = re.sub(r"\s+", " ", page.extract_text() or "")
        for entry in toc_entries():
            normalized_entry = re.sub(r"\s+", " ", clean_inline(entry))
            if normalized_entry in text and entry not in pages:
                pages[entry] = page_no
    return pages


if __name__ == "__main__":
    build_docx()
    build_pdf()
    build_docx(discover_section_pages())
    build_pdf()
    print(DOCX_OUT)
    print(PDF_OUT)

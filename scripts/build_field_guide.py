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
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs" / "agentic-systems-field-guide.md"
OUTPUT_DIR = ROOT / "docs" / "downloads"
DOCX_OUT = OUTPUT_DIR / "Agentic-System-Building-Guide.docx"
PDF_OUT = OUTPUT_DIR / "Agentic-System-Building-Guide.pdf"


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
    r = p.add_run("BUILDING A\nLOCAL-FIRST AGENTIC SYSTEM")
    r.bold = True
    r.font.name = "Arial"
    r.font.size = Pt(28)
    r.font.color.rgb = RGBColor(33, 66, 100)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("A practical field guide for researchers, teachers, writers,\nand other knowledge workers")
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
    r = p.add_run("Version 0.2.0  |  17 July 2026")
    r.font.size = Pt(10)
    r.font.color.rgb = RGBColor(115, 115, 115)


def toc_entries() -> list[str]:
    return [
        line[3:].strip()
        for line in SOURCE.read_text(encoding="utf-8").splitlines()
        if line.startswith("## ") and line[3:].strip() != "Contents"
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
    properties.extend([color, underline])
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
    title.style = "Title"
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title.add_run("Contents")
    for index, entry in enumerate(toc_entries(), start=1):
        toc = doc.add_paragraph()
        toc.paragraph_format.space_before = Pt(5)
        add_hyperlink(toc, entry, f"section-{index}")
        toc.add_run(" " + "." * max(3, 72 - len(entry)))
        page = page_refs.get(entry, "—") if page_refs else "—"
        toc.add_run(f" {page}")
    note = doc.add_paragraph()
    note.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = note.add_run("Entries are linked to their sections. Page numbers are generated from the PDF layout.")
    run.italic = True
    run.font.size = Pt(8.5)
    run.font.color.rgb = RGBColor(120, 120, 120)


def configure_styles(doc: Document) -> None:
    styles = doc.styles
    normal = styles["Normal"]
    normal.font.name = "Aptos"
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

    if "Quote" not in styles:
        quote = styles.add_style("Quote", WD_STYLE_TYPE.PARAGRAPH)
        quote.font.italic = True


def clean_inline(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    return text.replace("**", "").replace("`", "").replace("*", "")


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
    for row_idx, row in enumerate(rows):
        for col_idx, value in enumerate(row):
            cell = table.cell(row_idx, col_idx)
            cell.text = value
            for paragraph in cell.paragraphs:
                for run in paragraph.runs:
                    run.font.size = Pt(8.5)
                    if row_idx == 0:
                        run.bold = True


def add_markdown_content(doc: Document) -> None:
    lines = SOURCE.read_text(encoding="utf-8").splitlines()
    in_code = False
    code_lines: list[str] = []
    idx = 0
    bookmark_id = 1
    while idx < len(lines):
        raw = lines[idx]
        line = raw.rstrip()
        if line.startswith("# "):
            idx += 1
            continue  # cover supplies the title
        if line.startswith("**Author:") or line.startswith("**Repository:") or line.startswith("**Version:"):
            idx += 1
            continue
        if line.startswith("```text") or line.startswith("```bash") or line == "```":
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
        if line.startswith("### "):
            doc.add_paragraph(clean_inline(line[4:]), style="Heading 3")
        elif line.startswith("## "):
            heading = clean_inline(line[3:])
            if heading == "Contents":
                idx += 1
                continue
            paragraph = doc.add_paragraph(heading, style="Heading 2")
            add_bookmark(paragraph, f"section-{bookmark_id}", bookmark_id)
            bookmark_id += 1
        elif line.startswith("# "):
            doc.add_paragraph(clean_inline(line[2:]), style="Heading 1")
        elif line.startswith("> "):
            p = doc.add_paragraph(clean_inline(line[2:]), style="Quote")
            shade(p, "EEF3F7")
        elif re.match(r"^[-*] ", line):
            doc.add_paragraph(clean_inline(line[2:]), style="List Bullet")
        elif re.match(r"^\d+\. ", line):
            doc.add_paragraph(clean_inline(re.sub(r"^\d+\. ", "", line)), style="List Number")
        elif line == "---":
            doc.add_paragraph("—", style="Normal").alignment = WD_ALIGN_PARAGRAPH.CENTER
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
    doc.core_properties.title = "Building a Local-First Agentic System"
    doc.core_properties.subject = "A practical field guide for agentic systems"
    doc.core_properties.comments = "Authored by @kwis7."
    add_cover(doc)
    toc_section = doc.add_section(WD_SECTION.NEW_PAGE)
    add_header_footer(toc_section)
    add_toc(doc, page_refs)
    body_section = doc.add_section(WD_SECTION.NEW_PAGE)
    add_header_footer(body_section)
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
    for page_no, page in enumerate(reader.pages, start=1):
        if page_no <= 2:
            continue
        text = page.extract_text() or ""
        for entry in toc_entries():
            if entry in text and entry not in pages:
                pages[entry] = page_no
    return pages


if __name__ == "__main__":
    build_docx()
    build_pdf()
    build_docx(discover_section_pages())
    build_pdf()
    print(DOCX_OUT)
    print(PDF_OUT)

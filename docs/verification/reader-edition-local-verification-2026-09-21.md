# Reader edition: local verification — 2026-09-21

> Historical draft: the files at the download paths have since been replaced. The page counts and hashes below describe the September 21 draft, not the current editions. See the [September 22 receipt](reader-edition-local-verification-2026-09-22.md) for current artifact verification.

This is a local verification receipt for the unpublished reader-edition rebuild. It does not replace the historical runtime evidence or certify a hosted release.

## Scope and result

- Baseline: `1e55eb104a6c4e258e3b283b45ba105c121351e3`.
- Rewrote English and Chinese onboarding and ten handbook chapters per language; added the fictional first-project exercise.
- Generated online and packaged reading copies from the canonical chapter source.
- Built both PDF editions directly from Markdown and removed the DOCX edition.
- Kept generator scripts, scaffold templates and runtime compatibility records unchanged.

## Checks performed

| Check | Result |
|---|---|
| Unit and integration suite | 28 tests passed |
| Generated Markdown/source-manifest check | Passed |
| Repository Markdown local-file links | Passed; external availability is not implied |
| Installable Skill relative-link containment | Passed |
| Source, builder, font and PDF hash checks | Passed |
| Embedded font coverage of handbook text | Passed |
| Same-environment rebuild into a separate directory | Both PDFs were byte-identical |
| English PDF | 21 pages; 46 external-link annotations; 23 internal-link annotations |
| Chinese PDF | 17 pages; 46 external-link annotations; 23 internal-link annotations |
| All-page visual inspection | All 38 final pages inspected as rendered PNGs; changed pages rechecked after layout fixes |
| Independent source review | No remaining blocker in the reviewed scope |
| `git diff --check` | Passed |

The layout review covered covers, contents, headings, tables, code, Chinese glyphs, page margins and reference URLs. It corrected a broken table header, an isolated table row, short code-block splits and shell commands wrapped inside arguments. The two languages' shell command arguments were checked for equivalence after adding explicit continuations.

The renderer emitted a nonfatal Fontconfig cache warning in the restricted local environment. Both editions rendered successfully; the inspected PDF text uses the bundled embedded font. No font-cache setting was changed.

## Reproduction environment

Python 3.12.14; ReportLab 4.4.9; pypdf 6.10.0; Pillow 12.3.0. Visual inspection used Poppler `pdftoppm` at 130 dpi. The normal document build does not download fonts or require Word or LibreOffice. Build instructions are in [CONTRIBUTING.md](../../CONTRIBUTING.md).

Commands run from the repository root:

```bash
python3 scripts/build_master_playbook.py
python3 scripts/build_field_guide.py
python3 scripts/check_docs.py
python3 -m unittest discover -s tests -v
git diff --check
```

A second PDF build used `--output-dir` with a separate temporary directory. Reproducibility was verified within this local environment, not across operating systems or Python versions.

## Final artifacts

- [Agentic-System-Building-Guide.pdf](../downloads/Agentic-System-Building-Guide.pdf) — SHA-256 `8b988111f47de02c9550028cbc2340268ddf6a86403583d76ed8c15d7da4cebc`.
- [Agentic-System-Building-Guide.zh-CN.pdf](../downloads/Agentic-System-Building-Guide.zh-CN.pdf) — SHA-256 `45209a8a262a173ce1181f4cd6ff4414657046597d0404bddd37754fcf00b8db`.

Full source and asset hashes are in [pdf-manifest.json](../downloads/pdf-manifest.json). Font origin, license and preparation are recorded in [the font directory](../assets/fonts/README.md).

## Not performed

- No fresh-session runtime test for Codex, Claude Code, Gemini CLI or another product. Existing evidence dates and levels remain unchanged.
- No observed end-user completion of the new learning exercise. Expected answers are authored fixtures.
- No remote GitHub Actions run. The proposed workflow was added locally only.
- No stage, commit, push, pull request, deployment or publication. New GitHub reference targets become available only after the corresponding source files are published.

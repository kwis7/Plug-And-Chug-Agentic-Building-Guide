# Contributing

Useful contributions make the first task easier to finish or make an existing claim easier to verify. A confusing instruction, a failed command with its environment, or a small source-backed correction is welcome.

## Find the editable source

| Material | Edit here | Generated copies |
|---|---|---|
| English and Chinese handbook | `docs/handbook/en/`, `docs/handbook/zh-CN/` | Compiled online guides, packaged reading copies and PDFs |
| Handbook order and edition | `docs/handbook/book.json` | Contents, metadata and source manifests |
| Technical explanation | `docs/reference/` | Old `docs/*.md` URLs forward here |
| Installable skill behavior | `skills/portable-agentic-system/` | Keep its local dependencies inside that package |
| First learning exercise | `examples/first-project/` | Expected answers are fixtures, not user results |
| Shared diagrams and fonts | `docs/assets/` | PDFs embed the needed assets |

Do not edit a compiled guide or a PDF independently. The older `textbook-*.md` files in the skill are advanced implementation references; they no longer assemble the reader handbook. This distinction lets the skill retain detail without forcing beginners through the full implementation interview.

## Build the documents

Python 3.10 or newer is required. From the repository root, use a virtual environment for the optional documentation dependencies:

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -r requirements-docs.txt
python3 scripts/build_master_playbook.py
python3 scripts/build_field_guide.py
python3 scripts/check_docs.py
python3 -m unittest discover -s tests -v
git diff --check
```

The Windows PowerShell activation command is `.venv\Scripts\Activate.ps1`. The handbook is built directly from Markdown with ReportLab. No Word document, LibreOffice installation, API credential or network fetch is needed during the build. `source-manifest.json` tracks chapter sources; `pdf-manifest.json` also tracks the builder, fonts and resulting PDFs. Neither hash manifest proves visual quality or runtime compatibility.

To check reading copies without changing files, run `python3 scripts/build_master_playbook.py --check`. To rebuild PDFs in a scratch directory, add `--output-dir /path/to/preview` to the PDF builder. Open both editions, inspect every page, and confirm that the contents, bookmarks and external links work. A locally built reference URL may point to a file that will only be available on GitHub after the corresponding source update is published.

Font subsetting is a separate, optional maintenance operation documented in [the font directory](docs/assets/fonts/README.md). Normal PDF builds use the checked-in subsets. Do not update runtime support dates as a side effect of rebuilding a book.

## Check the behavior you changed

The existing scaffold suite uses temporary fixtures. Preserve its checks on overwrite refusal, task states, receipts, locks and evidence labels. Documentation tests cover source drift, local links, example semantics and exported navigation. A minimum page count is not a quality target.

For runtime claims, follow the selected adapter and retain a dated fresh-session receipt. A static configuration test cannot certify a native hook. For new examples, use synthetic or clearly attributed public material and keep unknowns visible.

Keep pull requests focused, describe the problem and observed result, and include the relevant verification. Review unfamiliar code before running it. Follow the repository agent contract for authorized Git and external actions.

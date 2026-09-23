# Reader edition 3: local verification — 2026-09-22

This receipt records the reviewed publication candidate, including the agent foundations revision. It supersedes the [September 21 draft receipt](reader-edition-local-verification-2026-09-21.md). It records local checks; GitHub publication and Actions results are separate remote evidence.

## Scope

The bilingual handbook now contains eleven source chapters per language, including a foundation chapter that explains the company diagram, model, Agent, prompt, Skill, tools, Markdown files, context, local ownership and explicit personalisation. The requested subtitle appears on the English homepage and PDF cover. Each PDF includes the author's original company diagram on a landscape page. Skill explanations state that the core `SKILL.md` document becomes context when loaded; pinning means making the method discoverable for reuse, not changing weights or permanently activating its full text.

The earlier reader-experience rebuild includes bilingual onboarding, a synthetic first-project exercise, reference navigation, and direct PDF generation from Markdown. The DOCX edition is retired. The standard generator, scaffold templates and runtime compatibility records retain their baseline implementation.

## Checks performed

| Check | Result |
|---|---|
| Unit and integration suite | 29 tests passed |
| Generated Markdown and source manifest | Current |
| Markdown local-file links and Skill containment | Passed |
| Packaged diagram image URLs | Raw image URLs; regression assertion passed |
| PDF source, image, builder and font hashes | Passed |
| Embedded font coverage | Passed |
| Same-environment build in a separate directory | Both PDFs byte-identical |
| English PDF | 28 pages; 50 external links; 27 internal links |
| Chinese PDF | 23 pages; 50 external links; 27 internal links |
| Visual review | All 51 pages inspected as rendered PNGs; changed Chinese pages rechecked |
| Diagram layout | One landscape diagram page per edition, followed by portrait text |
| Chinese typesetting | Explicit cover-title break; closing punctuation kept off line starts |
| Independent source review | Image-link issue corrected; independent recheck found no remaining blocker |
| Git whitespace check | Passed |

The visual review covered covers, contents, the two original diagrams, tables, code, Chinese glyphs, headings, page boundaries, footers and reference URLs. Poppler emitted a nonfatal Fontconfig cache warning; rendering completed using the PDF's embedded fonts.

## Artifacts and reproduction

- `Agentic-System-Building-Guide.zh-CN.pdf`: SHA-256 `eb2c14a4f3962e5588ca3a555fe21d408edcb335e8e269e715b822445d2745a6`.
- `Agentic-System-Building-Guide.pdf`: SHA-256 `926740a79249853ede391a0f205ccd60c88ff5b8c764f68f31504948e8d78607`.

The [PDF manifest](../downloads/pdf-manifest.json) records source and asset hashes. Python 3.12.14, ReportLab 4.4.9, pypdf 6.10.0 and Pillow 12.3.0 were used locally. Poppler rendered the review images at 100 dpi. Build instructions and pinned dependencies are in [CONTRIBUTING.md](../../CONTRIBUTING.md).

```bash
python3 scripts/build_master_playbook.py --check
python3 scripts/check_docs.py
python3 -m unittest discover -s tests -v
python3 scripts/build_field_guide.py --output-dir /tmp/plug-chug-pdf-rebuild
git diff --check
```

The local deterministic-build comparison does not establish byte equality across platforms. No fresh-session product compatibility test or observed end-user completion of the exercise was performed. Existing runtime evidence dates remain unchanged. Public-source and local checks do not certify an external action or delivery.

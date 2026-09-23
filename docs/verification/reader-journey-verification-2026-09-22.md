# Teaching journey and navigation: local verification — 2026-09-22

This receipt covers the teaching-journey revision after commit `e12a75b`. It supersedes the artifact counts and hashes in the [earlier reader-edition receipt](reader-edition-local-verification-2026-09-22.md). Remote publication and GitHub Actions are separate evidence.

## Reader contract

The primary reader is a non-programmer using an existing AI app. The shared journey is: paste the repository URL and starting prompt, discuss one recurring job, agree on a concrete setup, build in the chosen folder, finish and check a useful task, try recovery in a fresh conversation, and keep a next-use card with actual paths.

The homepages, quick starts, beginner guides, handbook introductions, installed Skill and facilitator protocol now follow that journey. Fictional practice and direct command-line setup remain optional. The original concept and system maps, functional tools, installation guidance, generator, reference materials and downloads remain accessible from both homepages. The retired DOCX is intentionally excluded.

The starting prompt has one maintained bilingual source, `friend-starter-prompt.md`. The build script generates its four homepage/beginner-guide copies and checks for drift. The facilitator protocol owns the longer conversation; the old facilitation-script URL forwards to it.

A new teaching workspace uses small, understandable files and checks its result and handoff. The standard scaffold retains task manifests, generated status, receipts and applicable gates. An existing standard scaffold cannot be reclassified to bypass a failed check. Generator scripts, templates and runtime compatibility records are unchanged.

## Verification

| Check | Result |
|---|---|
| Unit and integration suite | 30 tests passed |
| Generated Markdown, shared prompts and source manifest | Current |
| Local Markdown links, homepage anchors and Skill containment | Passed |
| Homepage functional navigation | Legacy destinations retained directly or through their maintained replacement paths, excluding DOCX |
| Skill frontmatter validation | Passed with the skill-creator quick validator |
| PDF source, image, builder and font hashes | Passed |
| Embedded font coverage | Passed |
| Separate-directory build in the same environment | Both PDFs byte-identical |
| English PDF | 28 pages; 55 external links; 26 internal links |
| Chinese PDF | 23 pages; 55 external links; 26 internal links |
| Visual review | Final changed English pages reviewed; unchanged pages matched previously reviewed renders; all 23 Chinese pages reviewed |
| Independent decision simulation | New beginner setup and existing failed-gate scenarios selected the intended routes |
| Independent coherence review | No remaining blocker after route, reference-scope and duplicated-protocol corrections |
| Git whitespace check | Passed |

The decision simulation was a read-only test of how another agent interpreted the Skill and its references. It was not a fresh-session product integration test or an observed novice user study. PDF review covered diagrams, headings, code, tables, Chinese glyphs, page boundaries and reference URLs. Poppler's nonfatal Fontconfig warning did not prevent rendering.

The default Python environments lacked PyYAML for the separate skill-creator validator. Validation succeeded using an already cached PyYAML module through a process-local import path; no dependency or global configuration was installed or changed.

## Artifacts and reproduction

- English PDF SHA-256: `dca3656e068992f79d0f16f158fd77d9281a6db51ecd8b5542f7ca7297c0c6c7`.
- Chinese PDF SHA-256: `91b52ba86ea154489e03513bb662773b78f01489aa93265d6a4c27d8272045ce`.

See the [PDF manifest](../downloads/pdf-manifest.json) and [build instructions](../../CONTRIBUTING.md). The local PDF build used Python 3.12.14, ReportLab 4.4.9, pypdf 6.10.0 and Pillow 12.3.0; the deterministic comparison is limited to this environment.

```bash
python3 scripts/build_master_playbook.py --check
python3 scripts/check_docs.py
python3 -m unittest discover -s tests -v
python3 scripts/build_field_guide.py --output-dir /tmp/plug-chug-pdf-rebuild
git diff --check
```

No new product runtime, hook enforcement, external delivery or completed novice setup is certified here. Historical adapter evidence dates remain unchanged. A reader's fresh-session recovery must be marked not tested until actually observed in their chosen app.

# What has been verified

Use the narrowest accurate claim. A file can exist without being loaded by a runtime; a passing test can inspect a hook without proving that the installed application invoked it.

| Evidence | Supports | Does not establish |
|---|---|---|
| Source and link checks | Document paths and generated content agree | Advice is correct in every environment |
| Local scaffold tests | Tested generation and validation behavior | Current vendor integration |
| Fresh-session entrypoint test | The selected installed runtime loaded the intended instructions | All hooks and permissions work |
| Invalid and valid closeout exercise in that runtime | The tested blocking/allow behavior | Factual correctness of every deliverable |
| Output review and source checks | The specified output meets its criteria | Sending, publishing or external delivery |
| Authorized action plus independent readback | The observed external result | Future success or unchanged third-party state |

## Local documentation checks

After installing the optional [documentation dependencies](../../CONTRIBUTING.md), run from the repository root:

```bash
python3 scripts/build_master_playbook.py --check
python3 scripts/check_docs.py
python3 -m unittest discover -s tests -v
```

The PDF build must also be rendered and visually inspected. Hashes catch stale inputs and altered files; they cannot detect every layout defect. The [historical 2026-08-09 receipt](../verification/v2-local-verification-2026-08-09.md) describes an older edition. Its DOCX and page-count statements are historical, not current deliverables.

The [compatibility reference](compatibility.md) and machine-readable manifest carry their own evidence date. This documentation redesign does not promote those runtime claims. Record the actual version, command, observed behavior, date and limitations when performing a new smoke test.

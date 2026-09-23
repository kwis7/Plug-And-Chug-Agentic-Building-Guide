# Preparing a public update

Publishing is a separate action from local editing and verification. Inspect the complete diff, license notices, generated artifacts and the applicable review evidence before approving a release.

## Local checks

From the repository root, run:

```bash
python3 scripts/build_master_playbook.py --check
python3 scripts/check_docs.py
python3 -m unittest discover -s tests -v
git diff --check
git status --short
```

PDF checks require the documented [build dependencies](../../CONTRIBUTING.md). Regenerate and visually review both language editions after a content or layout change. The local test suite exercises disposable scaffold fixtures; it does not establish current installed-runtime behavior.

## Review the scope

Publish generic source, templates, examples, tests and the approved PDFs. Keep credentials, personal paths, private materials, practice output, logs and local backups outside the release. Read [third-party notices](../../THIRD_PARTY_NOTICES.md): code and prose use MIT; the redistributed font subsets use SIL OFL 1.1.

The reader handbook has its own edition metadata in `docs/handbook/book.json`. The toolkit version and its runtime evidence retain their own dates. Updating the book does not automatically release a new runtime integration.

## Approval and verification

Present the changed files and remaining limitations to the owner. Stage, commit, push, open a pull request, deploy, or publish only after authorization for the specific action. Read back the remote result before reporting publication. A local PDF or clean test run is not evidence that GitHub has been updated.

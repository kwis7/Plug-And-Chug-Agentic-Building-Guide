# Repository Agent Contract

This repository builds and documents a portable local-first agent harness. The active model is replaceable; the repository's instructions, adapters, skills, scripts, tasks, gates, data boundaries, and verification form the harness around it.

## Scope

- Keep examples public-safe and generic. Never add personal paths, credentials, account data, client/student records, private corpora, or identifying task content.
- Preserve the distinction among native runtimes, workspace products, switchboards, provider APIs, and custom harness code.
- Do not call an adapter runtime-verified unless a dated fresh-session receipt exists.
- Do not present Markdown instructions as a mechanical security or completion guarantee.

## Changes

- Use `skills/portable-agentic-system/pas/templates/` as the canonical scaffold template source.
- Keep the production `SKILL.md` concise and route detailed material to `pas/references/`.
- Update generator, validator, tests, compatibility manifest, docs, and downloadable artifacts together when a contract changes.
- Use small patches and preserve unrelated user work.

## Verification

Run, as applicable:

```bash
python3 -m unittest discover -s tests -v
python3 skills/portable-agentic-system/scripts/create_agentic_system.py --root /tmp/pas-smoke --config skills/portable-agentic-system/pas/examples/starter-config.json
python3 skills/portable-agentic-system/scripts/validate_agentic_system.py /tmp/pas-smoke
python3 skills/portable-agentic-system/scripts/check_budgets.py /tmp/pas-smoke
python3 skills/portable-agentic-system/scripts/generate_status.py /tmp/pas-smoke --check
git diff --check
```

Generated DOCX/PDF claims require a fresh build, page-count check, full-page rendering, and visual inspection. Static tests do not prove runtime loading, external delivery, deployment, or publication.

## Git and release boundary

Do not stage, commit, push, publish, or open a pull request without explicit user authorisation for that action.

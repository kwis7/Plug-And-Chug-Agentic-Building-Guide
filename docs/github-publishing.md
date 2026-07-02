# GitHub Publishing Guide

## What To Publish

Publish:

- guide docs;
- generic templates;
- scripts;
- tests;
- skill folder;
- example config with fake data.

Do not publish:

- private resumes;
- application materials;
- account data;
- unpublished manuscripts;
- proprietary datasets;
- API keys or `.env` files.

## Pre-Upload Checklist

Run:

```bash
python3 -m unittest discover -s tests -v
python3 skills/portable-agentic-system/scripts/create_agentic_system.py \
  --root /tmp/pas-smoke-system \
  --config skills/portable-agentic-system/pas/examples/starter-config.json \
  --force
python3 skills/portable-agentic-system/scripts/validate_agentic_system.py /tmp/pas-smoke-system
python3 skills/portable-agentic-system/scripts/harness_health_check.py /tmp/pas-smoke-system
```

Then inspect:

```bash
git status --short
git diff --stat
```

Search for secret-like strings:

```bash
rg -n "(api[_-]?key|access[_-]?token|password)\s*[:=]|BEGIN[[:space:]]PRIVATE[[:space:]]KEY" .
```

The repository uses the MIT License for code, scripts, tests, documentation,
templates, skill text, workflow text, examples, and other written content.

Before making the repository public, re-check that this permissive reuse policy
still matches the intended public contribution model.

## Suggested Repository Description

```text
A plain-language guide and installable skill for building a portable, local-first personal agentic harness with agents, task manifests, safety boundaries, skills, and AI-tool adapters.
```

## First Release

For a first public release, tag it as `v0.1.0` and state that the package is a scaffold and teaching guide, not a security product.

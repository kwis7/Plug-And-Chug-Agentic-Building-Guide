# Codex Adapter

Use this when the user wants PAS to run inside Codex while the durable agentic state remains in local Markdown files.

## Official docs checked

- Codex docs: https://developers.openai.com/codex/
- Codex config basics: https://developers.openai.com/codex/config-basic
- Codex configuration reference: https://developers.openai.com/codex/config-reference
- AGENTS.md guidance: https://developers.openai.com/codex/guides/agents-md
- Codex skills docs: https://developers.openai.com/codex/skills/

## Install Skill

Copy or symlink the skill folder to Codex's skills directory:

```bash
mkdir -p ~/.codex/skills
ln -s /path/to/Plug-And-Chug-Agentic-Building-Guide/skills/portable-agentic-system ~/.codex/skills/portable-agentic-system
```

Restart Codex if the skill list was already loaded.

## Project Entrypoint

At the root of a generated system, `AGENTS.md` should import:

```markdown
@import IDENTITY.md
@import RULES.md
@import SYSTEM_MAP.md
@import STATUS.md
@import MEMORY.md
```

## Harness context

Codex should read root files first, then the active task manifest, then only the relevant agent `knowledge/` or `skills/` files.

```bash
export PAS_ROOT="$HOME/Desktop/My Agentic Control Center"
export PAS_LOAD_ORDER="IDENTITY.md RULES.md SYSTEM_MAP.md STATUS.md MEMORY.md"
export PAS_TASK_MANIFEST="$PAS_ROOT/tasks/T-000-bootstrap/task.yaml"
```

## First Prompt

```text
Use $portable-agentic-system with pas-start to help me set up my personal local-first agentic harness.
```

## Writeback

Keep `SYSTEM_MAP.md` as the structural source of truth, `STATUS.md` as the current snapshot, `task.yaml` as the task state, and `MEMORY.md` as compact recovery notes. Use Codex approvals for yellow/red operations, especially file deletion, external network submission, or anything that could expose private material.

# Claude Code Adapter

Use this when the user wants PAS inside Claude Code while keeping durable state in ordinary project files.

## Official docs checked

- Claude Code overview: https://code.claude.com/docs/en/overview
- Claude Code settings: https://code.claude.com/docs/en/settings
- Claude Code memory: https://code.claude.com/docs/en/memory

## Install Skill

Claude Code can use local project skills or global skills. A common global path is:

```bash
mkdir -p ~/.claude/skills
ln -s /path/to/Plug-And-Chug-Agentic-Building-Guide/skills/portable-agentic-system ~/.claude/skills/portable-agentic-system
```

## Project Entrypoint

At the root of a generated system, `CLAUDE.md` should import:

```markdown
@import IDENTITY.md
@import RULES.md
@import SYSTEM_MAP.md
@import STATUS.md
@import MEMORY.md
```

## Harness context

```bash
export PAS_ROOT="$HOME/Desktop/My Agentic Control Center"
export PAS_LOAD_ORDER="IDENTITY.md RULES.md SYSTEM_MAP.md STATUS.md MEMORY.md"
export PAS_TASK_MANIFEST="$PAS_ROOT/tasks/T-000-bootstrap/task.yaml"
```

Load the project entrypoint first, then the active `task.yaml`, then only the needed `knowledge/` or `skills/` files.

## First Prompt

```text
Use the portable-agentic-system skill to audit this folder and tell me which agent should handle my task.
```

## Writeback

Ask Claude Code for explicit file updates, then keep durable state in PAS files rather than relying on chat memory alone. Confirm yellow/red operations before modifying existing files, deleting material, sending messages, or moving private data.

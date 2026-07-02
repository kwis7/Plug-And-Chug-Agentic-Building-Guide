# Gemini CLI Adapter

Use the same plain Markdown contract.

## Official docs checked

- Gemini CLI GitHub repository: https://github.com/google-gemini/gemini-cli
- Gemini API docs: https://ai.google.dev/gemini-api/docs

## Entrypoint

Create or use a root instruction file that tells Gemini to read:

```markdown
IDENTITY.md
RULES.md
SYSTEM_MAP.md
STATUS.md
MEMORY.md
tasks/<active-task>/task.yaml
workspace/current.md
skills/README.md
knowledge/README.md
```

## Harness context

```bash
export PAS_ROOT="$HOME/Desktop/My Agentic Control Center"
export PAS_LOAD_ORDER="IDENTITY.md RULES.md SYSTEM_MAP.md STATUS.md MEMORY.md"
export PAS_TASK_MANIFEST="$PAS_ROOT/tasks/T-000-bootstrap/task.yaml"
```

## First Prompt

```text
Read this agentic control center and summarise the agent registry, current tasks, and next safest action.
```

## Notes

- Keep raw data in local folders and load it only when needed.
- If Gemini cannot auto-import files, paste the entry files in order or use its file-loading mechanism.

## Writeback

Have Gemini return proposed edits rather than treating the chat as permanent state. Save reviewed task state to `task.yaml`, system state to `STATUS.md`, and only compact recovery notes to `MEMORY.md`.

# Architecture

The harness has two jobs:

1. make recurring AI work easier to resume;
2. make risky actions and sensitive material visible before they escape.

## Layers

| Layer | Name | Responsibility |
|---|---|---|
| 0 | Control center | Routing, system map, status snapshot, operation log |
| 1 | Domain agent | One recurring life or work domain |
| 2 | Task manifests | One YAML file per active task |
| 3 | Knowledge and skills | Durable references and reusable workflows |
| 4 | Data and outputs | Raw inputs, workspace drafts, reviewed deliverables, archive |
| 5 | Adapters and automation | Runtime-specific entrypoints, scripts, health checks |

## Three Views

| View | File | Purpose |
|---|---|---|
| Static structure | `SYSTEM_MAP.md` | What exists and where each agent's state/output lives |
| Dynamic snapshot | `STATUS.md` | What is active, blocked, complete, or stale |
| Task chain | `tasks/**/task.yaml` | Input -> owner -> skill -> output -> verification -> next action |

`MEMORY.md` should not do all three jobs. It is for compact recovery notes and important operation history.

## Task Lifecycle

```text
Intake -> Route -> Load context -> Execute -> Verify -> Output -> Update task/status/memory
```

Useful state should not remain trapped in chat. It should be written back to the smallest appropriate file.

## File Contract

| File | Role |
|---|---|
| `IDENTITY.md` | Role and scope |
| `RULES.md` | Stable behaviour and risk rules |
| `SYSTEM_MAP.md` | System structure |
| `STATUS.md` | System snapshot |
| `task.yaml` | Single task state |
| `MEMORY.md` | Compact recovery notes |
| `knowledge/README.md` | Stable references index |
| `skills/README.md` | Reusable workflows index |

## Skill Levels

| Level | Best for | Example |
|---|---|---|
| Level 1 | Checklist or writing workflow | paper review |
| Level 2 | Script-backed repeated operation | import CSV and generate report |
| Level 3 | Isolated context | one research project subagent |

## Knowledge Distillation

Raw material should not move straight into memory or skills. First decide what it is:

- stable background goes to `knowledge/`;
- always-on behaviour goes to `RULES.md`;
- repeated procedure goes to `skills/`;
- current task state goes to `task.yaml`;
- sensitive or bulky source material stays in `raw_data/` or outside Git.

Use [Knowledge Distillation And Skill Fusion](knowledge-distillation-and-skill-fusion.md) when turning old prompts, notes, templates, or personal habits into reusable system pieces.

## Health Check

Run this after structural changes:

```bash
python3 skills/portable-agentic-system/scripts/harness_health_check.py /path/to/system
```

The score is less important than the visibility. Broken references, missing verification, stale tasks, and sensitive tracked files should be easy to notice.

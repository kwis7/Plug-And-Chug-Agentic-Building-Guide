# Filesystem Contract

## Root control center

| Path | Authority | Default loading |
|---|---|---|
| `AGENTS.md` | Compact common operating contract | Native where the runtime supports it |
| `CLAUDE.md` | Claude Code bridge/delta | Claude Code only |
| `GEMINI.md` | Gemini CLI bridge/delta | Gemini CLI only |
| `IDENTITY.md` | Mission and organisational boundary | Non-trivial control-center work |
| `RULES.md` | Stable behaviour and authority rules | Non-trivial control-center work |
| `SYSTEM_MAP.md` | Stable agent ownership and paths | Routing/structure work |
| `STATUS.md` | Generated snapshot | Read when current system state matters; never hand-edit |
| `tasks/**/task.yaml` | One task's objective, authority, state, outputs, verification, resources, and handoff | Active task only |
| `MEMORY.md` | Compact recovery index | Only when resuming history |
| `knowledge/` | Long-term archive/library | Named files only, on demand |
| `skills/` | Reusable playbooks | Metadata first; body when triggered |
| `raw_data/` | Original inputs | Named files only; no recursive reading |
| `workspace/` | Current desk and drafts | Active task only |
| `artifacts/` | Generated intermediates | When a task references them |
| `logs/` | Rotated traces | Tail/index/summarise before model loading |
| `outputs/` | Reviewed deliverables | Delivery/review work only |
| `archive/` | Closed and superseded material | Recovery/audit only |
| `.pas/runtime/locks/` | Ephemeral resource locks | Scripts, not model context |

## Domain agent

Give each durable domain its own entrypoint delta, identity, rules, compact memory, knowledge, skills, tasks, workspace, artifacts, logs, outputs, archive, and optionally a vault. Do not create an agent merely because a directory could exist. A new agent is justified by a persistent mission, privacy boundary, source base, authority, or recurring output lifecycle.

## One fact, one authority

| Fact | Authority |
|---|---|
| What agents exist | `SYSTEM_MAP.md` |
| What tasks are active | Task manifests, projected into generated `STATUS.md` |
| What one task may do | That task's `authority` block |
| What proves completion | Verification receipts and closeout result |
| What must survive as a small handover | `MEMORY.md` |
| What is stable background | `knowledge/` |
| What happened during execution | Rotated `logs/` and receipts |
| What may be reviewed for delivery | `outputs/` |
| What may be sent/published | Current user authority plus release check, not folder location alone |

## Default budgets

| Surface | Portable default |
|---|---:|
| Root `AGENTS.md` | target 16 KiB; hard repo limit 24 KiB |
| Runtime bridge/delta | 4 KiB |
| Root memory | 12 KiB or 120 lines |
| Domain memory | 8 KiB or 100 lines |
| Task manifest | 32 KiB |
| Text log loaded directly | 64 KiB before tail/summarise/index |

Use runtime-specific smaller projections when necessary. A budget failure should force consolidation, not silent truncation of authoritative state.

## Large-file manifest

For large, binary, or sensitive inputs, maintain an index containing path, media type, byte size, source/provenance, sensitivity, owner, retention, checksum when useful, and whether an agent may load the file. The manifest is readable context; the entire warehouse is not.

# Filesystem Contract

Use this contract when building, auditing, or explaining a local-first agentic harness.

## Root Control Center

| Path | Role |
|---|---|
| `AGENTS.md` | Codex entrypoint; imports root identity, rules, map, status, and memory |
| `CLAUDE.md` | Claude Code entrypoint; imports root identity, rules, map, status, and memory |
| `IDENTITY.md` | Who the control center is and what it manages |
| `RULES.md` | Stable routing, safety, startup, closeout, and risk-level rules |
| `SYSTEM_MAP.md` | Long-term structure: agents, responsibilities, state sources, skills, sensitive data, outputs |
| `STATUS.md` | Current system snapshot: active, blocked, recently completed, needs attention |
| `tasks/**/task.yaml` | One task's owner, status, inputs, skill, outputs, verification, and next action |
| `MEMORY.md` | Compact recovery notes and operation log, not registry or full task state |
| `knowledge/` | Stable control-center references |
| `skills/` | Reusable control-center workflows |
| `workspace/` | Current plans, dashboards, and active notes |
| `inbox/` | Temporary intake area |
| `adapters/` | Platform-specific entrypoint files |

## Domain Agent

| Path | Role |
|---|---|
| `AGENTS.md` / `CLAUDE.md` | Runtime entrypoint for that agent |
| `IDENTITY.md` | Role, audience, voice, and scope |
| `RULES.md` | Behaviour, evidence, data, and closeout rules |
| `MEMORY.md` | Compact recovery state |
| `knowledge/` | Stable facts, policies, methods, source rules |
| `skills/` | Reusable workflows |
| `raw_data/` | Original source material; read-only by default |
| `workspace/` | Current drafts and intermediate work |
| `outputs/` | Reviewed deliverables that may be shared |
| `archive/` | Completed or inactive task material |
| `vault/` | Optional long-term notes and reviewed knowledge |
| `scripts/` | Deterministic automation for repeated work |
| `tests/` | Tests for scripts or workflows |

## One Fact, One Authority

| Fact type | Authority |
|---|---|
| System structure | `SYSTEM_MAP.md` |
| System snapshot | `STATUS.md` |
| Single task state | `tasks/**/task.yaml` |
| Recovery summary | `MEMORY.md` |
| Long-term knowledge | `knowledge/` or reviewed `vault/` notes |
| Sendable deliverables | `outputs/` |

## Placement Decision

| If it defines... | Put it in... |
|---|---|
| Who the agent is | `IDENTITY.md` |
| Always-on behaviour | `RULES.md` |
| The system's parts | `SYSTEM_MAP.md` |
| What is active now | `STATUS.md` |
| One task's chain | `task.yaml` |
| Resume notes for next session | `MEMORY.md` |
| Stable reference | `knowledge/` |
| Repeatable task steps | `skills/` |
| Original private source files | `raw_data/` |
| Current scratch work | `workspace/` |
| Reviewed deliverables | `outputs/` |
| Completed task material | `archive/` |

## Audit Questions

1. Can a new AI session tell who it is by reading `IDENTITY.md`?
2. Can it tell what not to do by reading `RULES.md`?
3. Can it answer "what exists?" from `SYSTEM_MAP.md`?
4. Can it answer "what is happening now?" from `STATUS.md`?
5. Can it answer "why did this task flow this way?" from `task.yaml`?
6. Are raw private materials outside Markdown and Git?
7. Are repeated workflows in `skills/` instead of buried in chat?
8. Are reviewed deliverables separated into `outputs/`?

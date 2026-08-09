# System Review And Renewal Reference

Use this reference for `pas-review`: a periodic check of an existing personal agentic system after real use.

## Review Is Not Audit

| Mode | Use when | Main question |
|---|---|---|
| `pas-audit` | The folder is messy, missing structure, or unsafe | "Is the harness structurally sound?" |
| `pas-review` | The system has been used for a while | "What did the system learn, and what should change?" |
| `pas-distill` | There are notes, prompts, templates, or habits to reuse | "Where should this reusable material go?" |

Review may create a queue for `pas-distill`, but it should not shove every useful line into memory.

## Inputs

Read only what is needed for the review window:

1. `SYSTEM_MAP.md`
2. `STATUS.md`
3. `tasks/**/task.yaml`
4. `MEMORY.md`
5. relevant agent `MEMORY.md`, `workspace/current.md`, `knowledge/README.md`, and `skills/README.md`
6. root `knowledge/cross-agent-skill-map.md`, if cross-agent borrowing has happened
7. recent reviewed outputs, if they explain reusable patterns

If the system exists on disk, run `harness_health_check.py` first and include the score.

## Review Questions

Ask:

1. Which tasks are still genuinely active?
2. Which blocked tasks need human input, a source file, or archive?
3. Which completed tasks still sit in Active?
4. Which repeated prompts or corrections should become a skill?
5. Which stable facts or preferences should become knowledge?
6. Does `MEMORY.md` contain task details that belong in `task.yaml`?
7. Does `SYSTEM_MAP.md` still describe the actual agents and outputs?
8. Are raw data, secrets, or drafts too close to sendable outputs?
9. Which adapter or model choices worked well for which task type?
10. Has one agent repeatedly borrowed another agent's method?
11. What is the smallest update that makes the next session easier?

## Classification

| Finding | Destination |
|---|---|
| Active task with unclear next step | `task.yaml.next_action` |
| Current-state mismatch | Correct the owning task manifest, then regenerate `STATUS.md` |
| Reusable method | `skills/` |
| Repeated borrowed method | Local `skills/`/`knowledge/`, or root `cross-agent-skill-map.md` update |
| Stable background, style preference, or concept | `knowledge/` |
| Always-on safety or behaviour | `RULES.md` |
| Resume note for future sessions | `MEMORY.md` |
| Finished or abandoned task | `archive/` |
| Sensitive raw material | `raw_data/`, `private/`, or outside Git |

## Output Rules

- Return a review report first; do not silently edit files.
- Separate findings from proposed changes.
- Mark each proposed change as `safe_to_apply`, `needs_human_review`, or `do_not_apply_yet`.
- If asked to apply changes, do small batches and rerun validation plus health check.
- Keep `MEMORY.md` compact. It should say what future sessions need, not retell every chat.

Use `pas/templates/review-report.md` for the report shape.

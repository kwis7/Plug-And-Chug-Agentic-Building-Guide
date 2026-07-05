# Cross-Agent Skill Map

Purpose: give the control center a read-only routing map for borrowing useful methods across agents without merging memories, identities, or private data.

## Operating Rule

- Decide the active agent first. The active agent's `IDENTITY.md`, `RULES.md`, `MEMORY.md`, `skills/`, `knowledge/`, `workspace/`, and task manifest remain authoritative.
- Borrowed skills and knowledge are read-only references. They can shape method, checklist, source strategy, writing form, QA logic, or review habits, but they do not overwrite the active agent's rules.
- Do not copy private or raw data across agents.
- Save temporary cross-agent notes under the active agent's `workspace/` or task folder.
- If a borrowed method becomes repeatedly useful, distill the reusable part into the active agent's own `skills/` or `knowledge/`, and cite the source agent or source note.

## Borrowable Assets

| Source agent | Borrowable assets | Useful when | Boundary |
|---|---|---|---|
| Example Research Agent | `skills/literature-review.md`, `knowledge/source-policy.md` | Another agent needs source hygiene, literature search shape, citation checks | Do not copy unpublished research data or project-specific claims |
| Example Writing Agent | `skills/revision-checklist.md`, `knowledge/style-guide.md` | Another agent needs tone, structure, or revision logic | Do not copy private client material or drafts |
| Example Project Agent | `skills/qa-check.md`, `knowledge/project-methods.md` | Another agent needs QA flow or project review logic | Do not copy project-specific raw files |

## Source Note Template

```md
# Source Map

- Active agent:
- Borrowed agent / skill:
- Borrowed for:
- Facts used:
- Methods used:
- Private data excluded:
- Files written:
- Items still needing verification:
```

# Cross-Agent Skill Borrowing Reference

Use this reference for `pas-borrow`: borrowing a method, checklist, source strategy, review habit, or workflow shape from one agent while keeping the active agent's identity, memory, task state, and private data separate.

## Core Rule

Borrow methods, not private worlds.

- The active agent remains authoritative.
- Borrowed skills and knowledge are read-only references.
- Do not copy raw or private material across agents.
- Temporary notes go under the active agent's `workspace/` or task folder.
- Repeatedly useful borrowed methods should be distilled into the active agent's own `skills/` or `knowledge/`.

## Read Order

1. Active agent `IDENTITY.md`
2. Active agent `RULES.md`
3. Active task `task.yaml` or `workspace/current.md`
4. Root `knowledge/cross-agent-skill-map.md`
5. Only the borrowed skill or knowledge file needed for the method
6. Active agent output and closeout files

## Borrowing Decision

| Need | Better action |
|---|---|
| One task needs another agent's checklist | Borrow it once and write a source note |
| The same checklist is reused several times | Run `pas-distill` and create a local skill |
| A stable concept is useful across domains | Add a neutral note to root `knowledge/` |
| The borrowed method depends on private data | Do not borrow; ask for a privacy-safe summary or create a separate subagent |
| Two agents now do the same job | Review responsibilities before merging anything |

## Boundaries

Do not cross-copy:

- resumes, applications, personal statements, account exports, health records, legal files, private letters, tax records, credentials, cookies, API keys, browser profiles, unpublished datasets, private drafts, or project-specific raw corpora;
- another agent's `MEMORY.md` as if it were current task truth;
- another agent's `RULES.md` when it conflicts with the active agent.

You may borrow:

- checklist structure;
- source strategy;
- review questions;
- writing form;
- QA logic;
- folder or naming conventions;
- a public, privacy-safe distilled method.

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

## Closing Habit

End with:

1. which method was borrowed;
2. which data stayed inside its owning agent;
3. where the output was written;
4. whether this should become a local skill, a knowledge note, or nothing more.

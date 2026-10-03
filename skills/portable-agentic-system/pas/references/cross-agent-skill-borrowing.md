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
| The borrowed method depends on private data | Keep the data with its owner; use an authorised minimal summary, or delegate inside that owner's verified access boundary |
| Two agents now do the same job | Review responsibilities before merging anything |

## Delegation does not establish isolation

A separate worker or folder does not automatically restrict files, tools, network access, or inherited instructions. A conversation fork can inherit the parent's full history. A fresh worker can still receive project instructions and use tools with broad access. Do not transfer private material merely because execution has a different agent name.

When delegation is justified, agree on a bounded contract and record the context and permission projection in the receiving task:

- owner, objective, minimal authorised inputs, allowed writes, and prohibited actions;
- fresh, resumed, or forked context and which instructions, skills, and memory enter it;
- effective native tools, sandbox/access restrictions, approval mode, and any limits that remain advisory;
- expected evidence, stop condition, verification responsibility, and observed boundary tests.

Use the [skill matrix](skill-matrix.md#context-and-permission-projection) and exactly one [runtime adapter](adapters.md) for detail. Keep private-data work inside its owning scope unless the user explicitly authorises the destination and transfer. If the runtime boundary cannot be verified, return a privacy-safe method summary or a gap instead of claiming isolation.

As reviewed on 2026-10-02, Claude Code's [official subagent documentation](https://code.claude.com/docs/en/sub-agents#manage-subagent-context) distinguishes non-fork context from conversation forks. This is documented product behavior, not a runtime verification of this package.

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

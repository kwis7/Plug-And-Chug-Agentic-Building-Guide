# Cross-Agent Skill Borrowing

This guide is for a common moment in a growing agentic system:

> "One agent already has a useful method. Can another agent use it without mixing their private data?"

Yes. The safe version is method borrowing, not memory merging.

## The Plain Idea

Different agents often develop useful habits. A research agent may have a good source-checking routine. A writing agent may have a strong revision checklist. A project agent may have a neat QA pattern. It would be wasteful to rediscover those methods every time.

The risk is that "borrowing" can quietly become "copy a lot of private context into the wrong place." That is how a useful system turns into a drawer full of cables. Possibly functional, rarely elegant.

Use `knowledge/cross-agent-skill-map.md` as a small routing map. It says:

- which agent has borrowable skills or knowledge;
- when another agent might use them;
- what kind of data must never cross;
- where temporary notes should be saved;
- when a borrowed method should be distilled into the active agent's own `skills/` or `knowledge/`.

## Borrow Methods, Not Private Worlds

| You may borrow | Do not borrow |
|---|---|
| checklist shape | raw private files |
| source-search strategy | credentials, keys, cookies |
| review questions | resumes, applications, account exports |
| writing structure | unpublished manuscripts or datasets |
| QA logic | another agent's `MEMORY.md` as live task state |
| naming or folder conventions | personal identifiers or sensitive project facts |

The active agent remains in charge. Its `IDENTITY.md`, `RULES.md`, `task.yaml`, `workspace/`, and `outputs/` stay authoritative.

## A Typical Flow

1. Decide the active agent first.
2. Read the active agent's rules, current workspace, and task state.
3. Check `knowledge/cross-agent-skill-map.md` for a reusable method.
4. Read only the borrowed skill, knowledge note, or checklist needed for the method.
5. Write any temporary source note under the active agent's `workspace/` or task folder.
6. Keep private/raw data inside the owning agent.
7. If the borrowed method proves useful repeatedly, run `pas-distill` and promote a clean local version into the active agent.

## Source Note

For a borrowing task, add a small note:

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

This note does not need to be dramatic. It just lets a future session understand why a method appeared in this task and what stayed out of bounds.

## How It Works With Distillation

Borrowing is temporary. Distillation is how temporary borrowing becomes a local habit.

If an active agent uses the same borrowed checklist several times, do not keep hopping across agents forever. Create a local version:

- repeated procedure -> `skills/`;
- stable background or source rule -> `knowledge/`;
- always-on safety boundary -> `RULES.md`;
- one-time task detail -> `task.yaml` or `workspace/`.

The local version should cite the source method and remove any private details from the borrowed agent.

## How It Works With Review

During `pas-review`, look for:

- agents repeatedly borrowing the same method;
- borrowed methods that should become local skills;
- private data copied into the wrong agent;
- unclear boundaries in `cross-agent-skill-map.md`;
- outdated source paths or retired agents;
- tasks that borrowed a method but left no source note.

The review should produce a small renewal queue, not a grand reorganisation ceremony. If the queue requires a robe, it is probably too much.

## Prompt To Use

```text
Use $portable-agentic-system with pas-borrow.

Active agent:
Task:
Method I may want to borrow:
What must stay private:
Expected output:
```

## Final Rule

Cross-agent borrowing should make the system more connected without making the data more tangled. Borrow the recipe. Leave the private pantry alone.

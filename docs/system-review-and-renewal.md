# System Review And Renewal

This guide is for the moment after you have used your agentic system for a while and the folders begin to show real life: a few active tasks, some completed work, useful corrections, half-finished notes, and one file called `final-final-reviewed-v3.md` quietly judging everyone.

The goal is not to make maintenance heavy. The goal is to notice what your system has learned, clean up what is stale, and update the structure so the next month is easier than the last one.

## When To Review

Run a review:

- every one to four weeks if you use the system often;
- after a large project ends;
- after adding several agents, adapters, or skills;
- when `MEMORY.md` starts feeling like a messy transcript;
- when tasks are active but nobody remembers why;
- when you keep giving the AI the same correction.

Use:

```text
Use $portable-agentic-system with pas-review.
Review my agentic system since [date / last review / recent project] and suggest updates.
```

## What The Review Reads

Start from the smallest useful set:

| Source | What it shows |
|---|---|
| `SYSTEM_MAP.md` | Whether the agent structure still matches real use |
| `STATUS.md` | What the system currently believes is active, blocked, complete, or stale |
| `tasks/**/task.yaml` | Which tasks moved, stalled, produced outputs, or skipped verification |
| `MEMORY.md` | Recovery notes, operation log, and repeated lessons |
| `knowledge/` | Stable notes that may need updates or links |
| `skills/` | Repeated workflows that may need creation, fusion, or retirement |
| `knowledge/cross-agent-skill-map.md` | Whether method borrowing is clear, safe, and still up to date |
| `outputs/` | Reviewed deliverables that may point to reusable patterns |
| `archive/` | Finished work that should not remain active |

If the system exists on disk, run:

```bash
python3 skills/portable-agentic-system/scripts/harness_health_check.py /path/to/system
```

The health check catches mechanical issues. The review catches meaning.

## The Review Loop

1. **Choose a review window.** Since the last review, the last two weeks, or one completed project.
2. **Read status before memory.** `STATUS.md` says what the system thinks is happening now; `MEMORY.md` explains how it got there.
3. **Check task manifests.** Look for stale active tasks, missing verification, missing outputs, and unclear next actions.
4. **Find repeated friction.** Repeated corrections, repeated prompts, repeated file moves, and repeated confusion are skill candidates.
5. **Distil durable learning.** Stable facts, preferences, and concepts go to `knowledge/`; repeated procedures go to `skills/`.
6. **Check cross-agent borrowing.** If one agent keeps borrowing the same method, either document it clearly in `cross-agent-skill-map.md` or distil a local version.
7. **Update structure only when needed.** New agents are a last resort. A clearer skill or knowledge note is often enough.
8. **Write proposed updates.** Treat the review report as a queue for human approval, not as permission to rewrite the system silently.

## Decision Rules

| Finding | Better destination |
|---|---|
| Stale active task | Update `task.yaml`, then `STATUS.md`, or move to `archive/` |
| Repeated prompt | Draft a small skill |
| Repeated factual correction | Add or update `knowledge/` |
| Repeated safety concern | Propose a `RULES.md` update |
| Long one-off project | Archive or make a subagent only if it will continue |
| Messy memory entry | Move task facts to `task.yaml`; keep only compact recovery notes in `MEMORY.md` |
| Reviewed output with reusable pattern | Distil into `knowledge/` or a skill |
| Repeated cross-agent borrowing | Add/update `cross-agent-skill-map.md`, or distil a local skill |
| Sensitive raw material near public docs | Move back to `raw_data/`, `private/`, or outside Git |

## What The Report Should Produce

A good review report is short enough to act on:

- health score and mechanical issues;
- active, blocked, stale, and recently completed tasks;
- knowledge candidates;
- skill candidates;
- cross-agent borrowing updates;
- rule or safety updates;
- archive candidates;
- suggested next actions in priority order.

Keep the tone practical. A review that produces twelve new agents is usually not a review; it is interior decoration with YAML.

## After The Review

Apply changes in small batches:

1. update task state and `STATUS.md`;
2. archive completed work;
3. create or update one or two knowledge files;
4. create only the skills that will be reused;
5. update `MEMORY.md` with a compact review note;
6. rerun the health check.

End by asking: "Will this make the next session easier to resume?" If yes, keep it. If not, the system may be trying to look organised instead of being useful.

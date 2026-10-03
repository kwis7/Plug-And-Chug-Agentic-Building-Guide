# Skill Matrix Design

Use this when a user wants a skill system or when repeated work starts showing up.

## Rule Vs Skill

| Idea | Destination |
|---|---|
| "Always verify sources" | `RULES.md` |
| "When reviewing a paper, follow these steps" | `skills/paper-review/SKILL.md`, installed in the runtime's supported discovery location |
| "Here is my citation style preference" | `knowledge/` or `RULES.md` |
| "Today I am revising chapter 2" | `tasks/**/task.yaml` and `workspace/current.md` |
| "Run this script to import CSV files" | script-enhanced skill |
| "I keep reusing these notes/prompts/templates" | distill first, then route to `knowledge/`, `skills/`, or `RULES.md` |

## Procedure and execution choices

| Choice | Use when | Shape |
|---|---|---|
| Instruction skill | A repeatable workflow is mostly judgment and checklists | A discoverable package with `SKILL.md` |
| Script-enhanced skill | The workflow repeats mechanical file or data operations | `SKILL.md` plus inspected scripts and named resources |
| Bounded worker | An independent workstream benefits from separate context, tool restrictions, or review | A runtime-supported delegation or worker definition, optionally using selected skills |

A worker is an execution choice, not a higher skill level. Prefer a skill in the current conversation when the phases need shared context or frequent user feedback. Prefer a temporary worker for a bounded result; create a persistent definition only when the role recurs or native restrictions justify it. Do not create identity/rules/memory folders solely to enable delegation.

Separate conversation context from access control. A worker with fresh conversation context may inherit project instructions and have access to the same filesystem or tools. A conversation fork may inherit the full parent history. Neither a folder nor a Git worktree establishes a private-data boundary.

## Context and permission projection

Before delegating sensitive or restricted work, record the selected runtime's actual behavior:

| Surface | Record |
|---|---|
| Context mode | Fresh worker, resumed worker, or conversation fork; what history and instructions are inherited |
| Skills | Which full skill bodies are preloaded, which remain discoverable, and their context cost |
| Memory | Whether memory is loaded or persisted, its owner, and allowed paths |
| Tools and access | Native tool restrictions, filesystem/network sandbox, effective permissions, and approval mode |
| Task boundary | Minimal authorised inputs, allowed writes, prohibited actions, and stop condition |
| Return | Expected result, evidence, gaps, and the parent's verification responsibility |
| Evidence | Installed version, test date, observed loading/denial behavior, and untested surfaces |

As reviewed on 2026-10-02, Claude Code distinguishes fresh non-fork subagents from forks that inherit the parent's conversation. Non-fork workers normally load the parent instruction hierarchy, subject to documented built-in-agent exceptions; the `skills` field preloads full bodies rather than limiting all skill access. Verify the selected version and effective configuration before relying on these behaviors. See the [official context model](https://code.claude.com/docs/en/sub-agents#manage-subagent-context) and [fork comparison](https://code.claude.com/docs/en/sub-agents#how-forks-differ-from-other-subagents).

Use the relevant [runtime adapter](adapters.md) for native configuration. Written exclusions and task authority remain required, but mechanical restrictions need native controls and a denial test. If an effective boundary is unknown, keep private material with its owner and share only an authorised minimal summary.

## Skill Template

Every skill should answer:

1. When should this be used?
2. What inputs does it need?
3. What steps must happen in order?
4. Where does the output go?
5. What should be verified before closing?

Measure invocation and result quality separately. Positive, negative, and collision prompts check routing; representative inputs and output assertions check whether the workflow helps. Compare a few fresh sessions with the skill available and unavailable before claiming an improvement, and record time or token overhead when it affects the decision. Static format validation supports neither behavioral claim. This follows the [official skill evaluation guidance](https://code.claude.com/docs/en/skills#evaluate-and-iterate-on-a-skill), reviewed on 2026-10-02.

## Common Mistakes

- Creating a skill for a one-time task.
- Putting always-on rules inside a skill.
- Making a skill from raw notes before distilling what is reusable.
- Making one giant skill for many unrelated workflows.
- Forgetting to update `skills/README.md`.
- Forgetting to define the output location.

# Skill Matrix Design

Use this when a user wants a skill system or when repeated work starts showing up.

## Rule Vs Skill

| Idea | Destination |
|---|---|
| "Always verify sources" | `RULES.md` |
| "When reviewing a paper, follow these steps" | `skills/paper-review.md` |
| "Here is my citation style preference" | `knowledge/` or `RULES.md` |
| "Today I am revising chapter 2" | `tasks/**/task.yaml` and `workspace/current.md` |
| "Run this script to import CSV files" | script-enhanced skill |
| "I keep reusing these notes/prompts/templates" | distill first, then route to `knowledge/`, `skills/`, or `RULES.md` |

## Three Skill Levels

| Level | Use when | Shape |
|---|---|---|
| Level 1: instruction | The workflow is mostly judgment and checklists | One Markdown file |
| Level 2: script-enhanced | The workflow repeats mechanical file or data operations | Markdown plus scripts |
| Level 3: agent-isolated | The task has long context, sensitive data, or independent project state | Subagent folder with its own identity/rules/memory |

## Skill Template

Every skill should answer:

1. When should this be used?
2. What inputs does it need?
3. What steps must happen in order?
4. Where does the output go?
5. What should be verified before closing?

## Common Mistakes

- Creating a skill for a one-time task.
- Putting always-on rules inside a skill.
- Making a skill from raw notes before distilling what is reusable.
- Making one giant skill for many unrelated workflows.
- Forgetting to update `skills/README.md`.
- Forgetting to define the output location.

# Mode Registry

Single source of truth for Plug And Chug Agentic Empire modes.

## Modes

| Mode | Trigger examples | Human involvement | Output |
|---|---|---:|---|
| `pas-start` | "build my agentic system", "set up personal AI agents", "portable agent setup" | High | Agent matrix, config, scaffold, validation |
| `pas-audit` | "my agents are messy", "review this folder", "clean up my AI agent system" | Medium | Risk map and cleanup plan |
| `pas-add-agent` | "add a job search agent", "make a subagent for this project" | Medium | Agent/subagent spec and files |
| `pas-create-skill` | "turn this workflow into a skill", "make a skill matrix" | Medium | Skill placement and template |
| `pas-distill` | "turn these notes into a skill", "merge these prompts", "add this knowledge to my agent" | Medium | Knowledge routing, skill draft, or fusion plan |
| `pas-adapt` | "use this in Claude/Codex/ChatGPT/Gemini/API/CC Switch" | Low | Runtime adapter instructions |
| `pas-explain` | "explain agents to my colleague/parents" | Low | Plain-language explanation |

## Alias Policy

The skill accepts both slash and plain aliases:

- `/pas-start` or `pas-start`
- `/pas-audit` or `pas-audit`
- `/pas-add-agent` or `pas-add-agent`
- `/pas-create-skill` or `pas-create-skill`
- `/pas-distill` or `pas-distill`
- `/pas-adapt` or `pas-adapt`
- `/pas-explain` or `pas-explain`

If an alias conflicts with a platform's slash command system, tell the user to use the plain alias form.

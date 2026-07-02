# Plug And Chug Agentic Empire Workflow

Use this workflow for all `portable-agentic-system` modes.

## Operating Style

Start from the user's actual life and work, not from tool names. A good first sentence is:

> We can build this like a set of labeled workrooms: one front desk, one room per recurring domain, a status board, a task card, a library for durable knowledge, and recipes for repeated tasks.

Then ask for the next needed decision. Do not ask for every detail at once.

## Mode Selection

| Mode | Choose when | Main output |
|---|---|---|
| `pas-start` | User wants a new system | Intake, agent matrix, scaffold, validation |
| `pas-audit` | User has an existing folder or messy setup | Diagnosis and cleanup plan |
| `pas-add-agent` | User wants one more domain or project agent | Agent spec and files |
| `pas-create-skill` | User repeats a workflow | Skill placement and template |
| `pas-distill` | User wants to turn notes, prompts, templates, or habits into reusable knowledge or skills | Distilled knowledge, skill draft, or fusion plan |
| `pas-adapt` | User wants to use another AI tool | Adapter instructions |
| `pas-explain` | User wants to teach or explain the system | Plain-language explanation |

## `pas-start`: Build A New System

1. Explain the model in plain language.
2. Ask where the system should live. If the user is unsure, suggest a desktop folder named `My Agentic Control Center`.
3. Ask for 2-5 recurring domains. Use `pas/references/intake-questions.md`.
4. Convert domains into an agent matrix:

   | Agent | Purpose | Private raw data? | First skill candidate | Vault? |
   |---|---|---|---|---|

5. Ask the user to confirm the matrix.
6. Create a JSON config matching `pas/examples/starter-config.json`.
7. If the user wants files created, run `scripts/create_agentic_system.py`.
8. Run `scripts/validate_agentic_system.py`.
9. Run `scripts/harness_health_check.py`.
10. Explain how to start the next session:
   - open the root folder;
   - let the AI read `AGENTS.md` or `CLAUDE.md`;
   - ask for the relevant domain agent;
   - close the loop by updating the task manifest, status snapshot, and compact recovery notes.

## `pas-audit`: Review Existing Setup

1. Ask for the folder path or inspect the current workspace if already provided.
2. Map files into categories:
   - identity;
   - rules;
   - memory;
   - knowledge;
   - skills;
   - system map;
   - status;
   - task manifests;
   - workspace;
   - outputs;
   - vault;
   - raw data;
   - adapters.
3. Flag risks:
   - mixed private data and public instructions;
   - too many overlapping agents;
   - no current workspace file;
   - no single `SYSTEM_MAP.md`;
   - no single `STATUS.md`;
   - active work without `task.yaml`;
   - outputs mixed with raw data;
   - rules hidden inside skills;
   - no operation log;
   - raw data pasted into memory.
4. If files exist, run `scripts/validate_agentic_system.py` and `scripts/harness_health_check.py`.
5. Return a cleanup plan with concrete file moves.
6. Do not move files unless the user asks for execution.

## `pas-add-agent`: Add One Agent

1. Ask what recurring domain or project needs its own room.
2. Decide whether this should be:
   - a domain agent;
   - a subagent under an existing agent;
   - a skill inside an existing agent;
   - a one-time workspace note.
3. If an agent is warranted, create:
   - `IDENTITY.md`;
   - `RULES.md`;
   - `MEMORY.md`;
   - `knowledge/README.md`;
   - `skills/README.md`;
   - `raw_data/README.md`;
   - `workspace/current.md`;
   - `outputs/README.md`;
   - `archive/README.md`;
   - optional `vault/`.
4. Update `SYSTEM_MAP.md` if working in an existing control center.
5. Add or update a `task.yaml` if the new agent has active work.

## `pas-create-skill`: Build A Skill Matrix

1. Ask the user to describe the repeated workflow.
2. Decide placement:
   - always-on behaviour -> `RULES.md`;
   - reusable procedure -> `skills/`;
   - stable background -> `knowledge/`;
   - current task state -> `tasks/**/task.yaml`;
   - current system snapshot -> `STATUS.md`;
   - external service -> adapter or connector.
3. Choose skill level:
   - Level 1: instruction checklist;
   - Level 2: script-enhanced;
   - Level 3: subagent-isolated.
4. Use `pas/references/skill-matrix.md`.
5. Create only the smallest useful skill.

## `pas-distill`: Distill Knowledge And Fuse Skills

1. Ask what source material the user wants to reuse:
   - old prompts;
   - notes;
   - PDFs or webpages;
   - downloaded skills or templates;
   - personal habits or repeated corrections.
2. Ask which agent should own the result.
3. Read `pas/references/skill-distillation-and-fusion.md`.
4. Classify each reusable unit:
   - stable knowledge -> `knowledge/`;
   - always-on behaviour -> `RULES.md`;
   - repeated procedure -> `skills/`;
   - current task state -> `tasks/**/task.yaml`;
   - one-time material -> `workspace/` or `archive/`;
   - large or sensitive context -> subagent.
5. If a skill is warranted, read `pas/references/skill-matrix.md` and draft the smallest useful skill.
6. Decide whether to fuse with an existing skill or keep it separate.
7. Keep source material in `raw_data/` or outside Git unless it is public and safe.
8. End with a short report: what became knowledge, what became a skill, what stayed raw, what was rejected, and the first harmless test task.

## `pas-adapt`: Use Another AI Tool

1. Ask which tool the user wants: Codex, Claude Code, CC Switch, ChatGPT Project, Gemini CLI, direct API, OpenClaw, Hermes Agent, Xiaomi MiMo Claw / MiMo Code, DeepSeek, Qwen, MiniMax, Z.AI GLM, Xiaomi MiMo, Tencent Hunyuan, or another runtime.
2. Read `pas/references/adapters.md`.
3. Read the relevant file under `pas/adapters/`.
4. If it is a tool runtime, explain workspace boundaries and confirmation rules before the first prompt.
5. Explain the minimum install path and the first prompt to try.

## `pas-explain`: Teach The System

1. Use the household or workroom metaphor from `pas/references/mental-model.md`.
2. Explain only five terms first: control center, agent, memory, knowledge, skill.
3. Use examples from ordinary life before research or programming examples.
4. End with a simple test: "What should happen when a task ends?" Expected answer: task state is updated, reviewed deliverables go to `outputs/`, durable learning goes to `knowledge/` or reviewed vault notes, and only compact recovery notes go to `MEMORY.md`.

## Done Criteria

A setup pass is done only when one of these is true:

- files were created and validator plus health check output have no blocking errors;
- a concrete scaffold plan is ready and the user chose not to execute yet;
- an audit produced a prioritized cleanup plan;
- a distillation pass produced routed knowledge, a skill draft, or a clear rejection/fusion plan;
- an adapter path was given with a first invocation prompt.

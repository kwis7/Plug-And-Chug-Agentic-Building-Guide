# Troubleshooting

## "The AI forgot everything"

Check:

- Did the selected runtime load its real entrypoint: `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, or the product's documented equivalent?
- Does that entrypoint define a minimal loading order and point to `IDENTITY.md`, `RULES.md`, `SYSTEM_MAP.md`, generated `STATUS.md`, and compact `MEMORY.md` without inventing unsupported import syntax?
- Is current task state in `tasks/**/task.yaml`?
- Did the previous session update the task manifest and regenerate status?

## "Everything is mixed together"

Likely cause: too much was put in one agent. Split by recurring domain:

- research;
- job search;
- family admin;
- finance;
- writing;
- one project subagent.

Also check whether raw data, drafts, and deliverables are separated into `raw_data/`, `workspace/`, and `outputs/`.

## "There are too many agents"

Use this test: if the work happens less than monthly and has no private context, it may be a workspace note or skill, not an agent.

## "The skill never triggers"

Check:

- Does the skill have a clear `description` in frontmatter?
- Is it installed in the runtime's skill folder?
- Did the app restart after installation?
- Is the user request close to the trigger wording?

## "The script refuses to write files"

The scaffold script avoids overwriting. Use a new folder, or pass `--force` only after reading what will be overwritten.

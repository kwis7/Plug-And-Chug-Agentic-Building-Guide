# Claude Code Runtime Adapter

Classification: native coding-agent runtime
Repository verification: `verified_static`
Fresh-session verification: required before upgrading to `verified_runtime`

## Native contract

Claude Code loads `CLAUDE.md`. The portable bridge is:

```text
@AGENTS.md
```

Claude imports use `@path`, not `@import path`. Keep the bridge and Claude-specific delta compact; imported text still consumes context. Claude Code instructions are context, not a security boundary.

Official evidence:

- https://code.claude.com/docs/en/memory
- https://code.claude.com/docs/en/hooks
- https://code.claude.com/docs/en/skills
- https://code.claude.com/docs/en/sub-agents

## Skills and subagents

- Project skills: `.claude/skills/<skill-name>/SKILL.md`.
- Personal skills: `$HOME/.claude/skills/<skill-name>/SKILL.md`.
- Put routing triggers, exclusions, and boundaries in each skill or subagent `description` because that field affects automatic selection.
- Test positive, negative, and collision prompts instead of merely checking that the file exists.

## Completion gate

The generator writes a project `.claude/settings.json` `Stop` command hook. It resolves the project through `${CLAUDE_PROJECT_DIR}`, calls `.pas/bin/runtime_hook_gate.py`, and converts a failed common gate into:

```json
{"decision":"block","reason":"..."}
```

That response prevents Claude from stopping and feeds the reason back as the next instruction. A bare non-zero exit from `closeout_gate.py` is not a complete adapter. The generated baseline uses `Stop`; add `TaskCompleted` only if you have a separate mapping for Claude Code's native task registry rather than assuming it is the portable `task.yaml` lifecycle.

If multiple portable tasks are active, bind the session ID to one task with `.pas/bin/bind_task.py`. Do not call the gate verified until a real Claude Code session is blocked on a missing receipt and succeeds after outputs, receipts, generated status, released locks, budgets, and handoff are valid.

## Static and fresh-session smoke

```bash
python3 skills/portable-agentic-system/scripts/adapter_smoke.py /path/to/generated/system --runtime claude-code
```

Then start a clean Claude Code session in the fixture and ask it to identify the root contract, active task ID, prohibited actions, and difference between memory and knowledge. Record the Claude Code version, command, date, and output.

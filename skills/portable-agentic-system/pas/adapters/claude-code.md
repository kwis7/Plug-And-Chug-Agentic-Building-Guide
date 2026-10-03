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

The first rejection permits an automatic repair attempt. On a `Stop` with `stop_hook_active: true`, the adapter reevaluates the gate even if the latest message has no completion claim. If it still fails, it retains `decision: "block"` and the full rejection `reason`, then adds `continue: false`, `stopReason`, and `systemMessage`. The latter fields explicitly surface the failed closeout to the user. Claude Code gives `continue: false` precedence over continuation decisions, so this stops a failing repair loop without reporting that the gate passed. A repaired gate still returns `{}`. Gemini CLI retains its `decision: "deny"` schema.

This is a failed-stop handoff, not successful task completion. The adapter does not change `task.yaml`, release locks, fabricate receipts, or grant permissions. The task owner must repair the underlying failure or record an honest unsuccessful task state and handoff, then regenerate `STATUS.md`. `stop_hook_active` may originate from another Stop hook, so a failed continued stop can halt without a prior rejection by this adapter. Missing or malformed continuation flags cannot establish that a repair attempt occurred. Hook overrides, timeouts, user interruption, and runtime versions can affect enforcement; verify the installed runtime rather than treating the adapter as a security guarantee.

Protocol references: [Claude Code Stop input](https://code.claude.com/docs/en/hooks#stop-input), [Claude Code JSON output](https://code.claude.com/docs/en/hooks#json-output), and [Codex Stop](https://learn.chatgpt.com/docs/hooks#stop). Codex documents the same failed-stop fields and precedence, which the shared translator also uses for that runtime.

If multiple portable tasks are active, bind the session ID to one task with `.pas/bin/bind_task.py`. Do not call the gate verified until a real Claude Code session exercises both recovery paths: a repeated missing-receipt failure halts with its rejection visible, and a repaired closeout succeeds after outputs, receipts, generated status, released locks, budgets, and handoff are valid. Retain actual hook responses; a model refusing an invalid prompt does not show that the hook ran.

## Static and fresh-session smoke

```bash
python3 skills/portable-agentic-system/scripts/adapter_smoke.py /path/to/generated/system --runtime claude-code
```

Then start a clean Claude Code session in the fixture and ask it to identify the root contract, active task ID, prohibited actions, and difference between memory and knowledge. Record the Claude Code version, command, date, and output.

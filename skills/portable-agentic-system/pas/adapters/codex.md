# Codex Runtime Adapter

Classification: native coding-agent runtime
Repository verification: `verified_static`
Fresh-session verification: required before upgrading to `verified_runtime`

## Native contract

Codex builds an instruction chain from `AGENTS.md` files. It checks the user-level file, then walks from the project root to the working directory and appends the applicable file at each directory. A nearer instruction file is therefore later and more specific. Codex does not treat arbitrary lines such as `@import RULES.md` as imports.

Official evidence:

- https://learn.chatgpt.com/docs/agent-configuration/agents-md
- https://learn.chatgpt.com/docs/build-skills
- https://learn.chatgpt.com/docs/hooks
- https://learn.chatgpt.com/docs/environments/git-worktrees

## Generated files

- Put the compact always-on contract in root `AGENTS.md`.
- Add a nearer domain `AGENTS.md` only for domain-specific deltas.
- Keep the portable hard limit below 24 KiB so the whole hierarchy has room under Codex's default combined ceiling.
- Put repository skills under `.agents/skills/<skill-name>/SKILL.md`; use `$HOME/.agents/skills/` for personal skills.
- Do not copy `IDENTITY.md`, `RULES.md`, memory, knowledge, and current task state into the always-on entrypoint. Tell Codex when to load them.

## Completion gate

The generator creates `.codex/hooks.json`. Its `Stop` handler invokes `.pas/bin/runtime_hook_gate.py`, which reads Codex hook JSON from stdin, runs the common closeout gate, and translates failure into Codex's required top-level response:

```json
{"decision":"block","reason":"..."}
```

Returning the raw `closeout_gate.py` exit code is not the adapter: it must be translated into the runtime protocol. Codex project hooks also do not run merely because the JSON exists; review and trust the exact hook definition with `/hooks`. When more than one task is active, bind the runtime session explicitly:

```bash
python3 .pas/bin/bind_task.py . tasks/T-123/task.yaml --session <codex-session-id>
```

The hook's command resolves the generated absolute root because Codex hooks run from the session working directory, which may be a subdirectory. Regenerate the config after moving the harness. Treat the hook as `configured`, not runtime-verified, until a deliberately invalid closeout is continued and a valid one is accepted in a clean Codex session.

## Concurrency

Use separate Git worktrees for parallel write-heavy tasks. Record the worktree and resources in `task.yaml`; acquire scoped locks for non-Git resources or shared authority files. One branch cannot be checked out in two worktrees at once.

## Static smoke

```bash
python3 skills/portable-agentic-system/scripts/adapter_smoke.py /path/to/generated/system --runtime codex
```

This proves syntax and size checks only. For fresh-session smoke, start a clean Codex session in the generated fixture and ask it to report the first three operating-contract bullets and active task ID. Save the command, Codex version, date, and output as a receipt.

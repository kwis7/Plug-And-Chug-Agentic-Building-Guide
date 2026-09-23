# Runtime, Workspace, Switchboard, and Provider Adapters

**Evidence date: 2026-08-09.** These are repository-recorded classifications, not a new certification of current vendor behavior. The reader-edition rebuild does not upgrade any runtime or gate claim. Refresh the selected product documentation and run a clean-session test before relying on it.

The complete machine-readable source is [runtime-compatibility.json](../../skills/portable-agentic-system/pas/compatibility/runtime-compatibility.json). Each product file lives under [pas/adapters](../../skills/portable-agentic-system/pas/adapters).

## Native runtimes

| Runtime | Native entrypoint | Generated gate adapter | Repository status | Adapter |
|---|---|---|---|---|
| Codex | hierarchical `AGENTS.md` | `.codex/hooks.json` → `Stop` translator | verified static | [codex.md](../../skills/portable-agentic-system/pas/adapters/codex.md) |
| Claude Code | `CLAUDE.md`, valid `@AGENTS.md` bridge | `.claude/settings.json` → `Stop` translator | verified static | [claude-code.md](../../skills/portable-agentic-system/pas/adapters/claude-code.md) |
| Gemini CLI | hierarchical `GEMINI.md`, valid `@./AGENTS.md` bridge | `.gemini/settings.json` → `AfterAgent` translator | verified static | [gemini-cli.md](../../skills/portable-agentic-system/pas/adapters/gemini-cli.md) |
| OpenClaw | native workspace bootstrap files | not generated; typed plugin/wrapper required | documented only | [openclaw.md](../../skills/portable-agentic-system/pas/adapters/openclaw.md) |
| Hermes Agent | `AGENTS.md`, native skills and bounded memory | not generated; advisory until supported wrapper is proved | documented only | [hermes-agent.md](../../skills/portable-agentic-system/pas/adapters/hermes-agent.md) |
| MiMo Code | `/init` generates root `AGENTS.md` | not generated; advisory until supported mechanism is proved | documented only | [mimo-code.md](../../skills/portable-agentic-system/pas/adapters/mimo-code.md) |

For Codex, Claude Code, and Gemini CLI, static means official semantics and the generated files were checked. `documented only` means official behavior was reviewed but this repository generated no product integration. Neither label means the runtime was installed, the project hook was trusted, the entrypoint was loaded, or the gate blocked a real final response.

The common `closeout_gate.py` and each runtime hook speak different protocols. The generated `runtime_hook_gate.py` is the translation layer: Codex and Claude Code expect `decision: block`; Gemini CLI `AfterAgent` expects `decision: deny`. Without this translation, an adapter is only a shell around a validator.

## Workspace/manual projections

| Product | Projection | Status |
|---|---|---|
| Claude Cowork | project/folder instructions, folders, skills/plugins, project memory | manual projection |
| ChatGPT Projects | project instructions and reviewed uploads | manual projection |
| Custom GPTs | instructions, knowledge, capabilities, apps/actions | manual projection |
| Generic workspace agent | scoped folder plus startup contract | manual fallback |
| Tencent WorkBuddy | generic workspace path pending native contract evidence | provisional |
| Xiaomi MiMo Claw | product-specific evidence still incomplete | provisional |

## Switchboard and providers

CC Switch manages provider/model/configuration/routing and usage. It does not own agent identity, tasks, memory, gates, or data boundaries.

DeepSeek, Qwen, MiniMax, GLM, Xiaomi MiMo API, and Tencent Hunyuan are provider profiles. A provider supplies inference; the selected runtime or custom application loads harness context and persists state.

The direct API file is a `reference_pattern`, not a verified implementation. The application author must build and test the actual context, tool, permission, persistence, and closeout loop.

## Verification ladder

1. Official documentation reviewed.
2. Generated static syntax/schema/budget checks pass.
3. Clean runtime loads the intended entrypoint.
4. Invalid closeout is blocked and valid closeout passes.
5. Concurrent resource/worktree contention behaves correctly.

When more than one task is active, bind the runtime `session_id` to one `task.yaml`; otherwise the gate deliberately refuses an ambiguous completion claim.

Record runtime version, command, date, output receipt, and limitations. Never use the existence of an adapter Markdown file as evidence of native support.

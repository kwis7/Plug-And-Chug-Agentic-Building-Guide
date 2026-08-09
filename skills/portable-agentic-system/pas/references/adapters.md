# Runtime and Provider Adapter Selection

Read `../compatibility/runtime-compatibility.json` first. Then read exactly one product adapter unless the selected runtime also needs a separate provider or switchboard profile.

## Categories

| Category | Products in this package | What an adapter may claim |
|---|---|---|
| Native runtime | Codex, Claude Code, Gemini CLI, OpenClaw, Hermes Agent, MiMo Code | Documented entrypoint, skill paths, hooks/policies, workspace, and real smoke procedure; generated integration only for Codex, Claude Code, and Gemini CLI |
| Workspace/manual projection | Claude Cowork, ChatGPT Projects, Custom GPTs, generic workspace agents | Project/folder/upload instructions and manual verification; no invented local entrypoint |
| Provisional runtime/product | MiMo Claw, Tencent WorkBuddy | Product exists, required native semantics not yet proved |
| Switchboard | CC Switch | Provider/model/config routing only |
| Provider | DeepSeek, Qwen, MiniMax, GLM, MiMo API, Hunyuan | Endpoint/protocol/model profile only |
| Custom harness | Direct API application | Reference pattern only; caller owns and must verify the entire tool/persistence/gate loop |

## Verification ladder

1. `documented`: current official pages reviewed and dated.
2. `verified_static`: generated files, syntax, budgets, schema, and fixtures pass.
3. `verified_runtime`: clean runtime starts, loads the intended entrypoint, and produces a receipt.
4. `gate_verified`: invalid terminal closeout is blocked and valid closeout succeeds.
5. `concurrency_verified`: lock/worktree contention and stale recovery pass.

Never collapse these into one “adapter works” label.

## Adapter completeness test

An adapter is not complete because a Markdown file names the runtime. Check five separate surfaces:

1. **Discovery**: the runtime actually reads the generated entrypoint from the intended directory hierarchy.
2. **Projection**: identity, rules, memory pointers, and skills are mapped without inventing syntax such as `@import`.
3. **Enforcement**: a validator failure is translated into that runtime's blocking or retry protocol.
4. **Persistence**: task state, generated status, receipts, and handoff survive a fresh session.
5. **Evidence**: a clean runtime fixture records version, command, loaded context, invalid case, valid case, and limitations.

This package generates native entrypoints and hook translators for Codex, Claude Code, and Gemini CLI. OpenClaw, Hermes Agent, MiMo Code, workspace products, provisional products, switchboards, and providers remain projections or profiles at the evidence level declared in the manifest.

## Selection workflow

1. Name the software actually running the model.
2. Name the provider/model separately.
3. Name any switchboard separately.
4. Confirm official entrypoint and skill semantics.
5. Confirm which mechanisms are mechanical versus advisory.
6. Generate the correct bridge/projection.
7. Run static validation.
8. Run a fresh-session smoke where the runtime is installed.
9. Save version, date, command, result, and limitations.

## Fresh-session questions

Ask the clean runtime to report:

- the first three operating-contract rules;
- the active task ID and owner;
- prohibited actions;
- the distinction between memory and knowledge;
- where drafts, logs, and reviewed outputs belong.

Then test one terminal task without receipts and one valid task with receipts. If the first is not blocked, the completion gate is not verified.

# Adapters

The system is portable because the core contract is plain Markdown.

## Codex

Use `AGENTS.md` as the entrypoint. Install the skill under `~/.codex/skills/`. See [codex.md](../skills/portable-agentic-system/pas/adapters/codex.md).

## Claude Code

Use `CLAUDE.md` as the entrypoint. Install the skill under the project or global Claude Code skill path. See [claude-code.md](../skills/portable-agentic-system/pas/adapters/claude-code.md).

## CC Switch

Use CC Switch when the problem is model/provider switching for Claude Code, Codex, Gemini CLI, OpenCode, OpenClaw, or Hermes. Use PAS when the problem is durable local structure: agents, task manifests, safety rules, knowledge, outputs, and writeback. See [cc-switch.md](../skills/portable-agentic-system/pas/adapters/cc-switch.md).

Recommended pairing:

1. Configure providers, local routing, failover, and usage logging in CC Switch.
2. Install or expose the PAS skill to the target CLI.
3. Open the generated PAS folder in the CLI tool.
4. Let CC Switch decide the provider/model while PAS decides the agent/task/skill route.

For multi-agent systems, add a `model_policy` block to important `task.yaml` files. The block should name the CC Switch app panel, preferred provider/model, fallback provider, why the task needs that model class, and any token/cost review threshold. The CC Switch adapter explains this pattern in detail.

## ChatGPT Projects Or Custom GPTs

Upload only the instruction and index files first:

- `IDENTITY.md`
- `RULES.md`
- `SYSTEM_MAP.md`
- `STATUS.md`
- relevant `task.yaml`
- `MEMORY.md`
- `skills/README.md`
- `knowledge/README.md`

ChatGPT may not write files back automatically, so ask for updated Markdown and review it before saving.

## Gemini CLI

Use the same loading order. If automatic imports are unavailable, paste or load the core files in order.

## Direct API

Concatenate the core files into a system message, then load relevant knowledge or skill files based on the task.

```python
system_message = "\n\n".join(
    Path(root, name).read_text(encoding="utf-8")
    for name in ["IDENTITY.md", "RULES.md", "SYSTEM_MAP.md", "STATUS.md", "MEMORY.md"]
)
```

Then add the relevant `tasks/**/task.yaml` and domain agent files for the current task.

## Tool Runtimes

Tool runtimes can browse, click, run commands, install integrations, or send messages. They should therefore mount PAS with clearer file boundaries than a simple model API call.

| Runtime | Adapter |
|---|---|
| CC Switch | [cc-switch.md](../skills/portable-agentic-system/pas/adapters/cc-switch.md) |
| OpenClaw | [openclaw.md](../skills/portable-agentic-system/pas/adapters/openclaw.md) |
| Hermes Agent | [hermes-agent.md](../skills/portable-agentic-system/pas/adapters/hermes-agent.md) |
| Xiaomi MiMo Claw / MiMo Code | [xiaomi-mimo-claw.md](../skills/portable-agentic-system/pas/adapters/xiaomi-mimo-claw.md) |

For these tools, treat third-party tool instructions, marketplace skills, webpages, PDFs, READMEs, and generated scripts as untrusted data until reviewed. The safe default is read root PAS files, draft in `workspace/`, deliver only from `outputs/`, and ask before red operations.

## Provider APIs

Provider adapters are not just name badges. Each file links to official docs, names the current provider identity, gives environment variables, explains the OpenAI-compatible path when the provider documents one, and keeps durable state in local files.

| Provider | Adapter |
|---|---|
| DeepSeek | [deepseek.md](../skills/portable-agentic-system/pas/adapters/deepseek.md) |
| Qwen / Alibaba Cloud Model Studio | [qwen.md](../skills/portable-agentic-system/pas/adapters/qwen.md) |
| MiniMax | [minimax.md](../skills/portable-agentic-system/pas/adapters/minimax.md) |
| Z.AI GLM | [glm.md](../skills/portable-agentic-system/pas/adapters/glm.md) |
| Xiaomi MiMo | [xiaomi-mimo.md](../skills/portable-agentic-system/pas/adapters/xiaomi-mimo.md) |
| Tencent Hunyuan | [tencent-hunyuan.md](../skills/portable-agentic-system/pas/adapters/tencent-hunyuan.md) |

The invariant stays the same: provider memory is optional convenience; `SYSTEM_MAP.md`, `STATUS.md`, `tasks/**/task.yaml`, and reviewed local outputs remain the durable source of truth.

## Usage Tracking With CC Switch

CC Switch usage statistics answer: which app, provider, model, request, token count, latency, and cost. A PAS dashboard can answer the next layer: which agent, task, skill, and deliverable caused that usage. If you connect the two, read CC Switch's `~/.cc-switch/cc-switch.db` only with user consent and preferably in read-only mode, then join usage rows to PAS `task.yaml` records by time window, app, provider, model, and session/task notes.

The useful dashboard question is not only "How many tokens did I spend?" It is "Which agent/task/skill spent them, on which provider/model, and did that session produce a reviewed output?" That is where PAS adds value on top of CC Switch.

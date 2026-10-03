# Model portability with your existing AI app

[中文](model-portability.zh-CN.md)

Keep your local workspace useful when the app, provider or model changes. The host already runs the model, supplies tools, manages the live conversation and applies its native permissions and compaction. Plug & Chug helps you retain the files that describe your work: ownership, named inputs, chosen preferences, reusable knowledge, task state, checked outputs and recovery pointers.

Use this optional guide when comparing or changing an existing setup. It does not require a second execution engine, a provider gateway or a multi-agent system. Start with the [local workspace guide](local-workspace.md) if your immediate need is to keep working material organised.

## Separate what is changing

| Layer | What it identifies | What to check when it changes |
|---|---|---|
| Client | The app, CLI or SDK you interact with, and its version | Effective settings and the way it selects a runtime or endpoint |
| Runtime | The software executing the conversation and tools | Instruction loading, tools, native permissions, recovery and any configured hooks |
| Provider | The service serving the request | Supported endpoint type, region or plan, availability and data-use conditions |
| Wire API | The request and response protocol | Message roles, tool IDs and arguments, streaming, errors and provider-specific fields |
| Model | The requested identifier and reported resolved revision | Required capabilities, effective controls, context behavior and task results |
| Behavioral overlay | A small versioned adjustment to shared guidance | Whether examples, formatting or process hints improve the same task |

The client and runtime may be the same product. An API provider can also offer a separate agent product. Record the software you actually use; a provider name alone does not identify a runtime. API syntax compatibility does not establish native instruction loading or official support from the host vendor.

Keep the owner and working contract stable while you test a model. An overlay can clarify an output format or remove an unhelpful itinerary after observation. It must not weaken approvals, private-data boundaries, tool authority or completion criteria. Preferences remain [explicit, reviewable choices](personalization-and-evolution.md), rather than guesses about a model or user.

## Keep host responsibilities with the host

Use the host's supported tools, native memory and compaction instead of duplicating them in local scripts. Keep a short local handoff and pointers to named files so another conversation can recover the task. A local recovery note does not reproduce every detail of the host's conversation state, and a directory name does not enforce access restrictions.

When moving to another host, check that it can read the intended files with the intended permissions. Portable files do not automatically register Skills, configure tools, import native memory or activate hooks. The [adapter selection reference](../../skills/portable-agentic-system/pas/references/adapters.md) and [verification journey](verification.md) cover those separate surfaces.

Personal-information originals remain under the user's control. Use only the minimum fields supplied for the task, an explicitly agent-readable redacted derivative or a controlled mediator result. Local storage does not establish offline processing or permission to send data to a different provider. See [privacy and boundaries](privacy-and-boundaries.md).

## Record one selected combination

The [model combination template](../../skills/portable-agentic-system/pas/templates/model-combination.json) is an optional JSON record. Copy it into the owning workspace's established task or configuration location and give it a meaningful ID. It is an illustrative record with unknown capabilities and `acceptance.status: not_run`; it is not an active configuration, a benchmark or a compatibility claim.

Fill only what you know:

- Record client and runtime versions, provider endpoint type and region, requested model ID and any reported resolved ID. Leave the resolved ID and verification date `null` when unavailable. A moving alias is not a pinned revision.
- List the capabilities the task requires. Mark each observation `documented`, `observed`, `unknown` or `unsupported`, with an official source or a local receipt reference. A documented capability still needs an observed task check before acceptance.
- Distinguish a documented token limit from observed compaction behavior. Do not infer usable context from a model label or a file's byte budget.
- Record supported, ignored and unsupported parameters from the selected combination. An empty list means no entries have been recorded, not that every parameter is supported.
- Keep a small overlay ID and version. Point to acceptance receipts, a previous accepted combination and an explicit rollback trigger where available.

Do not put API keys, account identifiers, private paths, request bodies or raw reasoning content in this record. Keep pricing, latency and usage measurements in the referenced receipt when needed: date, wall-clock time, retries, reported token usage, actual or estimated cost, and the pricing source. Unavailable measurements stay unknown. Compare observed task performance without assigning universal model rankings.

From this repository root, check the record with the standard-library checker:

```bash
python3 scripts/check_workspace_records.py \
  skills/portable-agentic-system/pas/templates/model-combination.json
```

Supply related receipt records or their record bundle to the same command when checking references. `acceptance.receipt_refs` contains receipt record IDs, not filenames for the checker to open. The checker validates structure, status and supplied record relationships. It makes no provider request, reads no arbitrary referenced source, switches no model and proves no runtime behavior. Setting a fallback ID neither configures automatic switching nor authorises sending inputs to that fallback.

## Compare the same task

Use a small synthetic task before trying a candidate on personal material. For example, two named notes agree that a workshop starts Thursday at 10:00 but name different rooms. Require a saved result that preserves the time and leaves the location unresolved, then resume from its handoff in a fresh conversation.

Keep inputs, owner, permissions, output assertions and review criteria the same for the baseline and candidate. Record effective settings; incompatible parameters cannot be made equivalent merely by giving them the same value. Use the host's ordinary tools for a harmless local read/write exercise. Mock or omit external side effects.

| Common check | Evidence to retain |
|---|---|
| `instruction_loading` | The fresh session identifies the correct owner, task, named inputs and boundaries from the intended files |
| `tool_round_trip` | An authorised local tool call and returned result are handled correctly; saved output is reopened and checked |
| `uncertainty` | The output preserves the disagreement and does not invent a room |
| `recovery` | Another fresh session finds the saved result, gap and next allowed step without the old chat |

Add an observed check for every additional required capability, such as structured output, streaming or an image input. Leave unsupported or unavailable checks explicit. A chat-only plan cannot pass the local tool check by describing what a tool would do.

Keep routing and output quality separate: correct Skill selection does not establish factual correctness. Review the result against the named inputs and criteria, record interventions, and repeat important cases before claiming an improvement. A small manual comparison is enough to begin.

`passed` requires observed-mode evidence, a verification date and linked observed receipts for all four common checks and every required capability. An authored example must remain `not_run` or honestly `partial`; a failed required check remains `failed`. A later runtime, protocol, model revision or overlay change needs a new record or renewed evidence for the affected checks.

Test a native completion gate, native access denial or concurrency separately only when that setup uses and claims them. Use the [verification journey](verification.md) for invalid closeout, bounded recovery and repaired acceptance. A model declining a request does not prove that a hook or permission mechanism fired. One successful comparison supports the tested task and combination, not every use of that model.

## Current protocol caveats

Official sources reviewed on **2026-10-02** illustrate why the exact combination matters:

- Claude Code's gateway documentation explicitly does not support routing Claude Code to non-Claude models through any gateway. A third-party experiment must not be presented as official Claude Code compatibility. Gateways also need to pass through the capabilities the installed runtime uses. [Claude Code gateways](https://code.claude.com/docs/en/llm-gateway)
- Claude Code distinguishes aliases from full model names. Record the resolved model when available instead of treating an alias as an immutable version. [Model configuration](https://code.claude.com/docs/en/model-config)
- DeepSeek thinking mode accepts but ignores certain sampling parameters, and tools-bearing conversations have specific `reasoning_content` replay requirements. Verify the selected client's protocol handling; receipts should describe the check without copying raw reasoning content. [DeepSeek thinking mode](https://api-docs.deepseek.com/guides/thinking_mode/)
- Qwen thinking controls include nonstandard parameters with model-dependent support. Endpoint and credential region must also match the selected service. [Thinking controls](https://www.alibabacloud.com/help/en/model-studio/deep-thinking), [OpenAI API compatibility](https://www.alibabacloud.com/help/en/model-studio/compatibility-of-openai-with-dashscope)
- Z.AI distinguishes its general API endpoint from the Coding Plan endpoint. Record the selected endpoint type rather than assuming one endpoint serves every plan. [Z.AI quick start](https://docs.z.ai/guides/overview/quick-start)

These are dated documented facts, not live acceptance results for this repository. The existing compatibility manifest retains its own evidence date and verification levels.

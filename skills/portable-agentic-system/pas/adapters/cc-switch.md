# CC Switch Adapter

Use this when the user wants to run PAS inside Claude Code, Codex, Gemini CLI, OpenCode, OpenClaw, or Hermes while using CC Switch to choose models, providers, local routing, failover, skills, and usage tracking.

CC Switch is the model and CLI configuration layer. PAS is the local agentic harness layer. Keep those jobs separate and they work neatly together.

## Official docs checked

- CC Switch official site: https://ccswitch.io/en/
- CC Switch repository: https://github.com/farion1231/cc-switch
- Installation guide: https://github.com/farion1231/cc-switch/blob/main/docs/user-manual/en/1-getting-started/1.2-installation.md
- Quick start: https://github.com/farion1231/cc-switch/blob/main/docs/user-manual/en/1-getting-started/1.4-quickstart.md
- Add provider: https://github.com/farion1231/cc-switch/blob/main/docs/user-manual/en/2-providers/2.1-add.md
- Switch provider: https://github.com/farion1231/cc-switch/blob/main/docs/user-manual/en/2-providers/2.2-switch.md
- Proxy service: https://github.com/farion1231/cc-switch/blob/main/docs/user-manual/en/4-proxy/4.1-service.md
- App routing: https://github.com/farion1231/cc-switch/blob/main/docs/user-manual/en/4-proxy/4.2-routing.md
- Usage statistics: https://github.com/farion1231/cc-switch/blob/main/docs/user-manual/en/4-proxy/4.4-usage.md
- Skills management: https://github.com/farion1231/cc-switch/blob/main/docs/user-manual/en/3-extensions/3.3-skills.md
- Configuration files: https://github.com/farion1231/cc-switch/blob/main/docs/user-manual/en/5-faq/5.1-config-files.md
- Environment variable conflicts: https://github.com/farion1231/cc-switch/blob/main/docs/user-manual/en/5-faq/5.4-env-conflict.md

## What CC Switch owns

- Provider records, API keys, endpoints, model names, and model presets.
- Switching providers for supported CLI tools.
- Optional local proxy/routing at a local address such as `http://127.0.0.1:15721`.
- Request logs, provider/model usage statistics, token totals, latency, and cost estimates.
- CLI configuration writes such as `~/.claude/settings.json`, `~/.codex/auth.json`, `~/.codex/config.toml`, and `~/.gemini/.env`.
- Skill installation and updates for supported tools when using the CC Switch Skills page.

## What PAS owns

- `IDENTITY.md`: who the control centre or agent is.
- `RULES.md`: safety rules, operation risk levels, and external-content boundaries.
- `SYSTEM_MAP.md`: which agents exist and where their state lives.
- `STATUS.md`: active, blocked, completed, and attention-needed work.
- `tasks/**/task.yaml`: the durable state of one task.
- `knowledge/`, `skills/`, `workspace/`, `outputs/`, `archive/`, and `vault/` file boundaries.

Do not store provider keys, cookies, tokens, or CC Switch database exports in PAS Markdown or Git.

## Install shape

Install CC Switch from its official site, GitHub Releases, or Homebrew cask on macOS:

```bash
brew install --cask cc-switch
```

Then install the PAS skill into the target CLI tool. For Claude Code:

```bash
mkdir -p ~/.claude/skills
ln -s /path/to/Plug-And-Chug-Agentic-Building-Guide/skills/portable-agentic-system ~/.claude/skills/portable-agentic-system
```

If CC Switch Skills management is being used and it can manage the target app's skill directory, install or update the PAS skill there instead of maintaining several manual copies.

## Harness context

```bash
export PAS_ROOT="$HOME/Desktop/My Agentic Control Center"
export PAS_LOAD_ORDER="IDENTITY.md RULES.md SYSTEM_MAP.md STATUS.md MEMORY.md"
export PAS_TASK_MANIFEST="$PAS_ROOT/tasks/T-000-bootstrap/task.yaml"
export CCSWITCH_CONFIG_DIR="$HOME/.cc-switch"
export CCSWITCH_PROXY_URL="http://127.0.0.1:15721"
```

Load `PAS_LOAD_ORDER`, then the active `PAS_TASK_MANIFEST`, then only the relevant agent `knowledge/` or `skills/` files.

## Three-layer mental model

Use CC Switch and PAS as three connected ledgers:

| Layer | System | What it knows |
|---|---|---|
| Model switchboard | CC Switch | app, provider, endpoint, model, proxy/routing state, request log, tokens, latency, cost |
| Work routing | PAS | control centre, agent, task package, skill, file boundaries, verification, next action |
| Usage interpretation | PAS dashboard or local report | which agent/task/skill caused which model usage and whether the output was worth it |

CC Switch can tell you "Claude Code used Provider X and Model Y for N tokens." PAS should add "that usage belonged to Research Agent task T-024, skill literature-review, output fit-report.md, status reviewed." That second sentence is the part generic model switchers do not know by themselves.

## Provider setup for Claude Code

1. Open CC Switch and select the Claude Code app panel.
2. Add a provider using a preset such as DeepSeek, Zhipu GLM, Bailian/Qwen, MiniMax, Kimi, Xiaomi MiMo, SiliconFlow, OpenRouter, or another provider available in the current app.
3. Put the provider API key in CC Switch, not in PAS files.
4. Enable the provider.
5. Open Claude Code at `PAS_ROOT`.
6. Ask Claude Code to use the PAS skill and the local PAS files.

If the provider only exposes an OpenAI-compatible Chat Completions API, use CC Switch local routing/proxy when Claude Code needs Anthropic-format compatibility.

## Per-agent and per-task model routing

PAS should not hard-code one global model for every task. Instead, record a light `model_policy` in each task package when model choice matters.

Example `tasks/T-024-literature-review/task.yaml`:

```yaml
id: T-024
owner: research-assistant
status: active
skill: literature-review
input:
  - raw_data/papers/
outputs:
  - outputs/T-024-literature-map.md
model_policy:
  ccswitch_app: Claude
  preferred_provider: Bailian / Qwen
  preferred_model: account-selected long-context Qwen model
  fallback_provider: DeepSeek
  switch_mode: cc-switch-routing
  reason: long-context reading and Chinese/English source synthesis
budget:
  max_real_total_tokens: 250000
  review_after_cost_usd: 5
usage_tags:
  pas_task_id: T-024
  pas_agent: research-assistant
  pas_skill: literature-review
next_action: run_with_ccswitch_provider
```

Use this field as a local instruction, not as a magic API. CC Switch controls app/provider configuration; PAS records the desired route and reminds the user or agent what to switch to.

Suggested starting matrix:

| Agent or task package | Typical need | CC Switch action | PAS record |
|---|---|---|---|
| Research Agent / literature review | long reading, citation notes, bilingual synthesis | choose a long-context or strong reading provider for Claude Code or Gemini CLI | `model_policy.reason: long-context synthesis` |
| Coding Agent / debugging | code edits, tests, repo search | choose the provider that works best in the active CLI and supports the needed API format | `skill: code-debugging`, outputs in `workspace/` then `outputs/` |
| Writing Agent / editing | tone, structure, translation, revision | choose the provider whose style works for the language and genre | `skill: writing-revision`, include language and audience |
| Data Agent / analysis | scripts, notebooks, table inspection | choose a reliable tool runtime first, then a model backend | keep raw data in `raw_data/`, reviewed reports in `outputs/` |
| Life Admin Agent / forms | privacy-sensitive everyday documents | prefer the safest approved provider and smallest needed context | mark risky fields and send only reviewed `outputs/` |

The matrix is deliberately plain. The useful move is not "always use Model A for Agent B"; it is "write down why this task needs this kind of model, then make the switch visible."

## Task package workflow with CC Switch

1. **Create or open the task package.** Confirm `task.yaml` has `id`, `owner`, `skill`, `outputs`, `next_action`, and, if useful, `model_policy`.
2. **Choose the runtime.** Decide whether the work will happen in Claude Code, Codex, Gemini CLI, OpenClaw, Hermes, or another CC Switch-supported app.
3. **Choose the provider in CC Switch.** Use an app-specific provider for one CLI, or a universal provider when the same endpoint should be reused across apps.
4. **Enable routing when you want logs and fast switching.** CC Switch proxy/routing can record request logs and usage statistics. It also allows routed provider changes without the same restart burden as direct config switching.
5. **Start the session with task identity.** Put the task ID and agent name in the first prompt so the transcript and any imported session logs are easy to match later.
6. **Run the task.** The CLI agent reads PAS files and works inside the folder boundaries. CC Switch handles the model/backend.
7. **Write back state.** Update `task.yaml`, `STATUS.md`, compact `MEMORY.md`, and reviewed `outputs/`.
8. **Refresh usage view.** Check CC Switch Usage for app/provider/model/token/cost, then let the PAS dashboard or manual report attach those numbers to the task.

First prompt pattern:

```text
PAS task T-024. Agent: research-assistant. Skill: literature-review.
CC Switch provider target: Bailian / Qwen through Claude Code routing.
Read CLAUDE.md, then tasks/T-024-literature-review/task.yaml.
Use only the relevant knowledge and raw_data paths. Draft in workspace/ and prepare reviewed output in outputs/.
```

For a task that should switch provider before running:

```text
Before starting, check task.yaml model_policy.
If the active CC Switch provider does not match it, tell me exactly which CC Switch app panel and provider card to enable.
Do not rewrite provider keys or paste secrets into this chat.
```

## Switching model or provider

Without routing:

- Claude Code takes effect immediately after CC Switch updates the configuration.
- Codex usually needs the terminal or CLI session restarted.
- Gemini CLI usually re-reads configuration on each request.
- OpenCode and OpenClaw may need the CLI restarted.

With CC Switch routing/proxy enabled:

- Switch providers from the CC Switch interface or tray menu.
- Keep the CLI pointed at the local proxy.
- Requests can be logged for usage statistics and failover.
- Provider switching can take effect without restarting the routed CLI.

## Dynamic token and cost monitoring

CC Switch usage statistics already has the lower-level fields PAS needs: app, provider, model, request time, input/output tokens, cache tokens where available, latency, status, and estimated cost. PAS should borrow that idea, but group the numbers by work structure:

| PAS dashboard field | Source |
|---|---|
| `pas_task_id` | `tasks/**/task.yaml` and the first prompt/session note |
| `pas_agent` | `task.yaml.owner` |
| `pas_skill` | `task.yaml.skill` |
| `app` | CC Switch usage filter or request/session log |
| `provider` | CC Switch provider field |
| `model` | CC Switch model field, after its model normalisation if available |
| `real_total_tokens` | CC Switch usage statistics |
| `estimated_cost` | CC Switch pricing/cost estimate |
| `latency` and `status` | CC Switch request log |
| `output_path` | `task.yaml.outputs` |
| `outcome` | PAS verification and task status |

Recommended dashboard views:

- **By agent**: Which agents are consuming the most tokens and money?
- **By task**: Which active tasks are becoming expensive or stuck?
- **By skill**: Which repeated workflows are costly enough to deserve optimisation?
- **By provider/model**: Which models are actually being used for which kind of work?
- **By outcome**: Which usage produced reviewed outputs, and which usage only produced abandoned drafts?

Keep the join conservative. CC Switch may not natively store a PAS task ID, so a PAS dashboard should combine time window, app, provider, model, task/session note, and output path. If the task ID was not mentioned at session start, mark the attribution as `needs_review` instead of pretending.

## First prompt in Claude Code

```text
Use portable-agentic-system with pas-adapt and the CC Switch adapter.
Read CLAUDE.md, then the active task.yaml. My model/provider is managed by CC Switch.
Keep API keys out of Markdown, keep drafts in workspace/, and only prepare reviewed deliverables in outputs/.
```

For a concrete task:

```text
Use portable-agentic-system with pas-start.
CC Switch is handling the Claude Code provider. Build or audit my local agentic system from this folder, then tell me which agent should own my current task.
```

## Pair with provider adapters

CC Switch explains how the CLI points to a provider. A provider adapter explains that provider's own endpoint, model, and API behaviour.

Common pairings:

| CC Switch choice | Also read |
|---|---|
| DeepSeek | `pas/adapters/deepseek.md` |
| Bailian / Qwen | `pas/adapters/qwen.md` |
| MiniMax | `pas/adapters/minimax.md` |
| Zhipu GLM / Z.AI GLM | `pas/adapters/glm.md` |
| Xiaomi MiMo | `pas/adapters/xiaomi-mimo.md` |
| Tencent Hunyuan custom provider | `pas/adapters/tencent-hunyuan.md` |

## Usage dashboard bridge

CC Switch can record usage by app, provider, model, tokens, latency, status, and estimated cost. PAS can add the human meaning: which agent, task, skill, or project caused the usage.

Use this bridge pattern:

1. Keep every active task in `tasks/**/task.yaml` with `id`, `owner`, `skill`, `outputs`, and `next_action`.
2. Start long sessions by mentioning the task ID once, for example `PAS task T-024`.
3. Enable CC Switch proxy logging or CLI session import when usage tracking is desired.
4. Treat `~/.cc-switch/cc-switch.db` as read-only if a PAS dashboard imports it.
5. Join usage rows to PAS tasks by time window, app, provider, model, and task/session notes.
6. Show the final dashboard by agent, task, skill, provider, model, tokens, cost, and outcome.

CC Switch is therefore the lower-level usage meter. A PAS dashboard can be the higher-level work ledger. It is not a replacement for the CC Switch interface unless CC Switch exposes an extension point for that use case.

If a local dashboard reads CC Switch storage directly, open `~/.cc-switch/cc-switch.db` read-only. Its table layout belongs to CC Switch and may change, so the dashboard should inspect available tables/columns instead of assuming a permanent schema. Never write into the CC Switch database from PAS.

Read-only inspection pattern:

```bash
sqlite3 "file:$HOME/.cc-switch/cc-switch.db?mode=ro&immutable=1" ".tables"
```

Then map available usage rows into a local derived file such as:

```text
workspace/usage/ccswitch-usage-derived.csv
```

Do not commit that derived file if it contains private provider names, task names, document titles, costs, or other personal workflow traces.

## Writeback

After a model-switched session, ask the CLI agent for a small writeback bundle:

```text
Return proposed updates for:
1. the active task.yaml;
2. STATUS.md if task status changed;
3. compact MEMORY.md recovery notes;
4. any reviewed output path under outputs/.

Do not include API keys, provider tokens, cookies, or CC Switch database content.
```

## Sandbox check without provider credentials

```bash
python3 - <<'PY'
import os
from pathlib import Path

root = Path(os.environ.get("PAS_ROOT", "/tmp/pas-smoke-system"))
for name in "IDENTITY.md RULES.md SYSTEM_MAP.md STATUS.md MEMORY.md".split():
    assert (root / name).exists(), name

task = Path(os.environ.get("PAS_TASK_MANIFEST", root / "tasks/T-000-bootstrap/task.yaml"))
assert task.exists(), task

cc_dir = Path(os.environ.get("CCSWITCH_CONFIG_DIR", Path.home() / ".cc-switch"))
print(f"PAS context readable. CC Switch config dir expected at: {cc_dir}")
PY
```

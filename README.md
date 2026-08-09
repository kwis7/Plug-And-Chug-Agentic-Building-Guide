# Plug-And-Chug Agent Harness Building Guide

[English](README.md) | [中文](README.zh-CN.md)

A public-safe, local-first toolkit for explaining, designing, generating, adapting, and validating durable AI agent systems.

## The central idea

The model is the active worker, but it is not the whole agent system. The **harness** is every configured part around execution: runtime entrypoints, identity, rules, permissions, agent ownership, skills, tools, connectors, tasks, generated status, memory, knowledge, raw material, workspace, artifacts, logs, outputs, hooks, gates, budgets, locks, worktrees, validators, and adapters.

Changing the model is like replacing an employee. The company keeps its mission, policies, archives, playbooks, work orders, tools, desks, and quality controls. In a single-agent system, call the model an employee. Only a central coordinating model in a multi-agent system is the manager.

### Harness concept map

![The active replaceable model inside the complete harness boundary](docs/assets/harness-concept-map.png)

### Anonymised example system map

![A control center, four functional owner agents, shared methods, private context boundaries, and a verified execution flow](docs/assets/anonymised-agent-system-map.png)

The first map explains the concept. The second shows one possible multi-agent topology. Keep both: the example does not define every user's system, and the concept diagram does not pretend to be a complete implementation.

## Memory is not knowledge

- `MEMORY.md` is a compact shift handover and recovery index.
- `knowledge/` is the long-term archive, reference library, and institutional knowledge.
- `task.yaml` and `workspace/` hold current task state and execution context.
- `raw_data/` holds named originals; it must not be recursively loaded by default.
- `outputs/` holds reviewed deliverables, but does not itself authorise sending or publishing.

## What version 2 adds

- Real Codex, Claude Code, and Gemini entrypoints instead of imaginary `@import` syntax.
- A machine-readable compatibility manifest separating native runtimes, workspace projections, provisional products, switchboards, providers, and custom API harnesses.
- A v2 task contract with objective, authority, prohibited actions, completion criteria, failure conditions, receipts, resource claims, and handoff.
- Generated `STATUS.md` instead of relying on a model to remember to update two sources of truth.
- Runtime-native closeout translators: Codex/Claude `Stop` and Gemini `AfterAgent` convert the common gate into each host's required block/retry protocol.
- A deterministic closeout gate that rejects missing outputs, receipts, current status, released task locks, budget failures, or handoff.
- Hard instruction, memory, task, and large-file manifest budgets.
- Atomic, task-declared resource locks with writer/session/worktree checks, heartbeat renewal, and worktree guidance.
- Description quality checks and positive/negative/collision evaluation templates.
- A detailed but progressively disclosed production Skill plus a standalone textbook/workbook.
- Two bilingual maps: a harness concept map and a systematic anonymised example system map.
- A 30+ page textbook-style guide whose adapters are a compact appendix rather than the main subject.

## Install the Skill

Codex-compatible project scope:

```bash
mkdir -p .agents/skills
ln -s /path/to/Plug-And-Chug-Agentic-Building-Guide/skills/portable-agentic-system \
  .agents/skills/portable-agentic-system
```

Codex-compatible personal scope:

```bash
mkdir -p "$HOME/.agents/skills"
ln -s /path/to/Plug-And-Chug-Agentic-Building-Guide/skills/portable-agentic-system \
  "$HOME/.agents/skills/portable-agentic-system"
```

Claude Code uses `.claude/skills/`; Gemini CLI supports `.gemini/skills/` or `.agents/skills/`. Read the matching adapter before installing because runtime discovery and enforcement are not identical.

## Generate a starter harness

```bash
python3 skills/portable-agentic-system/scripts/create_agentic_system.py \
  --root "/path/to/My Agent Harness" \
  --config skills/portable-agentic-system/pas/examples/starter-config.json

python3 skills/portable-agentic-system/scripts/validate_agentic_system.py "/path/to/My Agent Harness"
python3 skills/portable-agentic-system/scripts/check_budgets.py "/path/to/My Agent Harness"
python3 skills/portable-agentic-system/scripts/generate_status.py "/path/to/My Agent Harness" --check
python3 skills/portable-agentic-system/scripts/harness_health_check.py "/path/to/My Agent Harness"
```

The generator refuses to overwrite existing files unless `--force` is explicitly supplied. Review the exact target before using force.

## Generated shape

```text
My Agent Harness/
├── AGENTS.md              # compact common contract
├── CLAUDE.md              # @AGENTS.md plus Claude-specific delta
├── GEMINI.md              # @./AGENTS.md plus Gemini-specific delta
├── IDENTITY.md
├── RULES.md
├── SYSTEM_MAP.md
├── STATUS.md              # generated from task manifests
├── MEMORY.md              # compact and budgeted
├── routing-evals.json
├── runtime-compatibility.json
├── .codex/hooks.json
├── .claude/settings.json
├── .gemini/settings.json
├── .pas/bin/              # copied validators, gates, locks, and hook translator
├── tasks/
├── knowledge/
├── skills/
├── raw_data/
├── workspace/
├── artifacts/
├── logs/
├── outputs/
└── example-Agent/
    ├── AGENTS.md  CLAUDE.md  GEMINI.md
    ├── IDENTITY.md  RULES.md  MEMORY.md
    └── tasks/ knowledge/ skills/ raw_data/ workspace/ artifacts/ logs/ outputs/ archive/
```

Every `raw_data/`, `artifacts/`, `logs/`, and `outputs/` directory includes a manifest. Files at or above 256 KiB must record an exact size, context policy, and retrieval summary instead of entering context recursively.

## Product classification

| Category | Products | Meaning |
|---|---|---|
| Native runtimes | Codex, Claude Code, Gemini CLI, OpenClaw, Hermes Agent, MiMo Code | Have product-specific entrypoint/workspace semantics |
| Workspace/manual projections | Claude Cowork, ChatGPT Projects, Custom GPTs, generic workspace agents | Use project/folder/upload instructions rather than claiming a local native chain |
| Provisional | Xiaomi MiMo Claw, Tencent WorkBuddy | Product exists; required native loading/gate semantics still need evidence |
| Switchboard | CC Switch | Changes provider/model/config/routing; does not own durable harness state |
| Providers | DeepSeek, Qwen, MiniMax, GLM, MiMo API, Tencent Hunyuan | Supply model inference; caller/runtime owns harness loading |
| Custom harness | Direct API application | Application author owns context, tools, persistence, budgets, gates, and writeback |

See the [compatibility manifest](skills/portable-agentic-system/pas/compatibility/runtime-compatibility.json) and [adapter guide](docs/adapters.md). Static checks, fresh-session loading, completion-gate behaviour, concurrency, and external delivery are separate evidence levels.

Only Codex, Claude Code, and Gemini CLI receive generated native entrypoints plus completion-hook translators. OpenClaw, Hermes Agent, and MiMo Code are documented runtime guides without generated integrations; direct API is a reference pattern. This distinction prevents a Markdown adapter shell from being mistaken for working support.

## Main resources

- [Quick start](QUICKSTART.md)
- [Standalone master build playbook](skills/portable-agentic-system/pas/references/master-build-playbook.md)
- [Simple prompt for a friend](skills/portable-agentic-system/pas/references/friend-starter-prompt.md)
- [Staged questionnaire](skills/portable-agentic-system/pas/references/intake-questions.md)
- [Filesystem contract](skills/portable-agentic-system/pas/references/filesystem-contract.md)
- [Task, gate, budget, and lock governance](docs/governance.md)
- [Runtime and provider adapters](docs/adapters.md)
- [Long-form field guide](docs/agentic-systems-field-guide.md)
- [Harness concept map](docs/assets/harness-concept-map.svg)
- [Anonymised example system map](docs/assets/anonymised-agent-system-map.svg)
- [Downloadable DOCX](docs/downloads/Agentic-System-Building-Guide.docx)
- [Downloadable PDF](docs/downloads/Agentic-System-Building-Guide.pdf)

## Verification

```bash
python3 -m unittest discover -s tests -v
python3 /path/to/skill-creator/scripts/quick_validate.py skills/portable-agentic-system
git diff --check
```

The health score is explicitly static. It never proves that a runtime loaded the instructions, a hook blocked an invalid closeout, a provider responded, an output was delivered, or a deployment succeeded.

## Privacy and licence

The public example uses generic first- and second-level folder patterns only. It contains no private source data, credentials, account records, client/student material, personal paths, or private task content.

Released under the repository [MIT License](LICENSE). Preserve attribution when adapting the guide.

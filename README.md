# A Plug-And-Chug Guide to Building Your Personal Agentic System

[English](README.md) | [中文](README.zh-CN.md)

A public-safe, local-first guide and working toolkit for building an AI agent system that fits the way you actually think and work.

## Vision

This project helps people build a personal AI agent system that lives in ordinary local folders, remains understandable to its owner, and can travel across models and tools. The aim is not to make AI feel more complicated. It is to give recurring work a durable home: clear rules, organised context, reusable methods, visible task state, and checks that make completion mean something.

The system should become easier to use over time because it preserves its structure without turning every chat transcript into permanent memory. Models, APIs, and interfaces can change; your work should not have to restart from zero.

## Who this is for

- researchers, students, writers, analysts, developers, and other knowledge workers;
- non-technical users who want to organise recurring AI-assisted work before learning software engineering;
- people who use AI across several areas of life or work and keep losing useful context between sessions;
- anyone who wants reusable workflows, clearer privacy boundaries, and less dependence on one model or interface.

A computer science degree is not required. A real reason to let AI help you, plus a willingness to give that help a clear structure, is enough to begin.

## Use this if you

- ask AI for help in multiple recurring domains;
- repeatedly explain the same background in new chats;
- want useful prompts and habits to become reusable skills;
- need to separate private source material, drafts, and reviewed outputs;
- want agents to borrow methods without mixing private data;
- want active, blocked, verified, and completed work to be visible;
- want the freedom to change models or runtimes without rebuilding your whole workspace.

For one quick answer, a normal chat is often enough. This package becomes useful when work repeats, grows, carries risk, or needs to survive the end of a conversation.

## The problem it addresses

Once AI is used for more than isolated questions, work starts to scatter. One chat contains a good draft, another holds the source list, and a third contains the decision made last week. Files accumulate with temporary names. The model may be capable, but the working environment around it becomes hard to recover.

The difficult part is often not model intelligence. It is continuity: what the model can see, which file is authoritative, what remains unfinished, what may be shared, and how the next session can continue without relying on human memory or the model remembering to update itself.

A local agentic harness gives that work somewhere to land. The chat can end and the active model can change, while the rules, task state, knowledge, procedures, evidence, and reviewed outputs remain readable in your own workspace.

## Why not just chat with the best model?

A stronger model can produce a better answer. It does not automatically preserve the project rules, source trail, task state, privacy boundaries, or verification habits that make a long-running body of work reliable.

For a developer, the durable value is not only one bug fix but also the project instructions, usual commands, tests, and unresolved edge cases. For a writer, it is the brand voice, source material, revision history, and approved formats. For a teacher, it is the course context and what students struggled with last time. For a researcher, it is the chain from sources and notes to methods, decisions, and drafts.

Direct chat is excellent for quick questions. A harness is for work that comes back and needs a place to continue.

## What a harness means here

The model is the active worker, but it is not the whole agent system. The **harness** is the complete configured environment around execution: runtime entrypoints, identity, rules, permissions, agent ownership, skills, tools, connectors, tasks, generated status, memory, knowledge, raw material, workspace, artifacts, logs, outputs, hooks, gates, budgets, locks, worktrees, validators, and adapters.

Changing the model is like replacing an employee. The company keeps its mission, policies, archives, department playbooks, work orders, tools, desks, and quality controls. In a single-agent system, the model is an employee. Only a coordinating model in a multi-agent system is the manager.

![The active replaceable model inside the complete harness boundary](docs/assets/harness-concept-map.png)

This distinction matters: a model supplies active reasoning; the harness supplies continuity, structure, access, procedures, and control. A folder full of Markdown is not automatically an enforced system, so this toolkit also includes scripts, manifests, hooks, validators, and evidence labels where deterministic behaviour is needed.

## How the information is organised

- `MEMORY.md` is a compact shift handover and recovery index.
- `knowledge/` is the long-term archive, reference library, and institutional knowledge.
- `task.yaml` and `workspace/` hold current task state and execution context.
- `raw_data/` holds named originals; it must not be recursively loaded by default.
- `outputs/` holds reviewed deliverables, but does not itself authorise sending or publishing.
- `STATUS.md` is generated from task manifests so current state does not depend on a model remembering a second update.
- `skills/` contains reusable procedures; rules that should always apply belong in entrypoints or policy files instead.
- receipts, gates, budgets, and locks make verification and concurrent ownership explicit where prose alone is not enough.

Memory and knowledge are both long-term files, but they serve different jobs. Memory answers “what must the next session know to resume?” Knowledge answers “what stable material should the system reuse?” Current execution belongs on the task desk, not in either archive.

## Why personalisation matters

- Your agent map can reflect your recurring work rather than somebody else's template.
- Your rules can reflect your privacy needs, risk tolerance, language, and approval boundaries.
- Your skills can capture procedures you actually repeat.
- Your outputs can match the formats you really submit, publish, study from, or archive.
- Your memory can stay compact because stable references live in knowledge and bulky originals remain outside automatic context.
- Your verification can match the consequences of the task instead of treating every generated answer as complete.

Personalisation is not decoration. It is how the system reduces repeated prompting without forcing your life into a tool's default workflow.

## An anonymised example system

The map below shows one possible multi-agent topology based on a real system, with names, private projects, paths, credentials, and sensitive domains replaced by neutral examples. A control centre routes work to functional owner agents. Methods may be shared, but private context remains with its owner. Tasks move through an explicit execution and verification flow.

![A control center, four functional owner agents, shared methods, private context boundaries, and a verified execution flow](docs/assets/anonymised-agent-system-map.png)

The concept map explains what surrounds one active model. The example map shows how those harness components can form a larger system. It is an example to adapt, not an organisation chart to copy.

## Start small

Two or three clear agents are usually more useful than ten vague ones.

| Example agent | Owns | A useful first skill |
|---|---|---|
| Research Assistant | papers, notes, citations, analysis | source review |
| Job Search Agent | postings, resumes, application tracking | posting intake |
| Life Admin Agent | forms, household tasks, follow-ups | document checklist |
| Learning Agent | courses, practice, review logs | mock review |

Create an **agent** when work is recurring and needs separate ownership and context. Create a **skill** when a procedure repeats inside an existing agent. Create a **knowledge note** for stable reusable material. Keep one-time work in the current task workspace.

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

## Use it across different AI tools

The same local structure can support different models and products, but portability does not mean pretending every product loads instructions in the same way. Codex, Claude Code, Gemini CLI, hosted workspaces, provider APIs, model switchboards, and custom applications have different discovery, permission, hook, and persistence behaviour.

This repository therefore keeps the durable harness model common while documenting each runtime's real entrypoints and evidence level separately. Start with the [adapter guide](docs/adapters.md) when connecting a tool, and use the [compatibility manifest](skills/portable-agentic-system/pas/compatibility/runtime-compatibility.json) when you need the precise support classification. A documented adapter is not automatically a runtime-tested integration.

## What the toolkit helps you do

- interview the user and design a small agent map around real recurring work;
- generate a control centre and domain-agent folders without overwriting an existing system by default;
- separate identity, rules, memory, knowledge, active work, raw material, and outputs;
- turn repeated procedures into progressively disclosed skills;
- route tasks by clear descriptions and test positive, negative, and collision cases;
- generate status from task contracts and require evidence before closeout;
- manage memory and large-file context budgets;
- coordinate concurrent work with resource claims, locks, and worktree guidance;
- validate structure, privacy boundaries, references, manifests, and completion receipts;
- review the system after real use and distil useful corrections into durable improvements.

## Main resources

- [Quick start](QUICKSTART.md)
- [Standalone master build playbook](skills/portable-agentic-system/pas/references/master-build-playbook.md)
- [Simple starting prompt](skills/portable-agentic-system/pas/references/friend-starter-prompt.md)
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

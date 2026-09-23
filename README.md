# Plug & Chug

## AI Agents, Explained

Why build your own local agentic system when you already have fancy apps like Codex, Claude Code, or WorkBuddy?

[English](README.md) | [中文](README.zh-CN.md) · [Start here](docs/start-here.md) · [Handbook](docs/handbook/index.md) · [English PDF](docs/downloads/Agentic-System-Building-Guide.pdf) · [中文 PDF](docs/downloads/Agentic-System-Building-Guide.zh-CN.pdf)

**A practical teaching guide for people who want their own AI working system, including people who have never written code.** Use the AI software you already have. Let it ask about your work, explain the choices, and help set up a local folder you understand and can return to.

The aim is simple: your materials, preferences, useful methods and unfinished work should survive the end of a chat. You should be able to change models without starting your working life over.

<a id="start-with-your-ai"></a>
## Start by giving this to your AI

Open the AI app you normally use and copy the whole block below. Codex and Claude Code are examples of tools that can work with local files; your app's actual permissions determine what it can do. This route starts with a conversation, so you do not need to install the Skill or run a terminal command first.

<!-- STARTING_PROMPT:en -->
```text
I don't know how to program. Please use this repository to help me build
my own local agentic system:
https://github.com/kwis7/Plug-And-Chug-Agentic-Building-Guide

Start with the beginner guide. Ask what I want help with, which AI app
I use, and what computer I have. Ask only two or three questions at a time.
Recommend the simplest useful setup for my work and explain it plainly.
Handle the technical steps you can actually perform. Before creating files,
show me the new folder and what you will put there, then wait for my agreement.
Use a new folder and preserve my existing files.
Help me complete one small task, check the result, and try continuing in
a new conversation. Finish with a short note explaining where my files are,
what to open next time, and what to ask you to do.
If you cannot read the repository or work with local files, explain the
one next step I need to take instead of claiming the setup is complete.
```
<!-- /STARTING_PROMPT -->

That is the **Plug & Chug starting point: one prompt, then guided setup**. You still choose what the system is for and where it lives. Your AI helps with the technical work and teaches each part when it becomes useful.

[Step-by-step beginner guide](docs/start-here.md) · [Save the starting prompt](skills/portable-agentic-system/pas/references/friend-starter-prompt.md#english) · [Questions your AI will ask](skills/portable-agentic-system/pas/references/intake-questions.md) · [Full facilitator protocol](skills/portable-agentic-system/pas/references/facilitation-protocol.md)

## What you will learn and build

A useful first result is a folder for one area of your life or work, a clear role for your AI, a small checked output, and a note that lets the next conversation continue. You can understand and change that arrangement without learning every technical term at once.

| Step | What happens | Read alongside it |
|---|---|---|
| Understand the pieces | Learn what models, Agents, prompts, Skills and files actually do | [The basics, with a company diagram](docs/handbook/en/00-foundations.md) |
| Choose your first use | Pick one recurring task and say what a useful result looks like | [Guided setup](docs/start-here.md) |
| Make a place for the work | Keep instructions, sources, drafts and checked results understandable | [Workspace and file roles](docs/handbook/en/02-workspace.md) |
| Finish something small | Let the AI work, then check the result with its sources | [First task](docs/handbook/en/01-first-task.md) |
| Return another day | Open a fresh conversation and recover the next step | [Continuing across sessions](docs/handbook/en/03-resume.md) |
| Make it yours | Preserve useful methods, add responsibilities when needed, and review what works | [Skills](docs/handbook/en/04-skills.md) · [Agents](docs/handbook/en/05-agents.md) · [Maintenance](docs/handbook/en/08-maintenance.md) |

The [complete handbook](docs/handbook/index.md) follows this learning path in English and Chinese. Prefer one document? Read the [English](docs/agentic-systems-field-guide.md) or [Chinese](docs/agentic-systems-field-guide.zh-CN.md) online edition, or download either PDF at the top of this page.

## The idea: keep the work, change the model

Think of a company. **You are the owner. The model is the employee doing the reasoning. An Agent gives that employee a working role**, with instructions, relevant information, tools and an execution loop. The **harness** is the whole configured working environment: its files, methods, access arrangements, task records and checks.

![The company metaphor: a replaceable model inside a persistent working system](docs/assets/harness-concept-map.png)

[Open the concept map as SVG](docs/assets/harness-concept-map.svg)

A **prompt** tells the model what you want. A **Skill** keeps a reusable method in a Markdown document, usually `SKILL.md`; when loaded, that text becomes part of the model's context. Think of pinning a useful playbook where it can be found again. It does not train new model weights or mean the full document is always loaded. A **tool** performs an action, such as reading or saving a file. A file on disk enters context only when the environment actually supplies its contents.

Your existing app provides capabilities. Your personal system arranges those capabilities around your work: which files matter, what a good result looks like, which methods to reuse, and how to continue later. Local files make those arrangements inspectable and recoverable. The model may still use a cloud service; local storage alone does not establish offline operation or privacy.

## What could your system help with?

| Your recurring work | What your system can preserve | A method worth reusing |
|---|---|---|
| Studying | Learning goals, practice results and explanations you understood | Review mistakes and plan the next practice |
| Research | Named sources, notes, open questions and checked conclusions | Compare evidence without filling gaps by guesswork |
| Writing | Your chosen tone, reference material, revisions and approved formats | Turn notes into a draft and review it against your brief |
| Job searching | Selected postings, authorised application material and task progress | Compare a posting with your experience and prepare a draft |
| Life administration | Instructions, working checklists and unfinished tasks | Prepare a document checklist and record the next step |

Start with one useful responsibility. A separate Agent becomes helpful when another area needs its own sources, instructions or ownership. You do not need a department for every task.

Personalisation means explicitly choosing language, explanation style, evidence standards and output formats that suit you. Your corrections can improve future work when you choose to retain them. Useful procedures become Skills; stable background becomes knowledge; today's progress stays in the task. The [personalisation explanation](docs/handbook/en/00-foundations.md#personalise-the-work-explicitly) shows the difference.

<a id="toolkit-features"></a>
## Find the function you need

These are available parts of the toolkit. You can ask your AI to use the relevant part; learning all the names is optional.

| I want to… | What the toolkit provides | Direct entry |
|---|---|---|
| Build my first personal system | A staged conversation and a proposed design | [Starting prompt](skills/portable-agentic-system/pas/references/friend-starter-prompt.md) · [Questionnaire](skills/portable-agentic-system/pas/references/intake-questions.md) |
| Create the standard folder structure | A generator, starter configuration and templates | [Setup commands](QUICKSTART.md#manual-standard-scaffold) · [Generator](skills/portable-agentic-system/scripts/create_agentic_system.py) · [Configuration](skills/portable-agentic-system/pas/examples/starter-config.json) |
| Check an existing system | Structure, file-budget, routing and status checks | [Health checker](skills/portable-agentic-system/scripts/harness_health_check.py) · [Review guide](docs/reference/system-review-and-renewal.md) |
| Add an Agent or a Skill | Decide what needs a separate role and write a usable trigger | [Routing and role checks](skills/portable-agentic-system/pas/references/description-routing-evals.md) · [Skill template](skills/portable-agentic-system/pas/templates/skill/SKILL.md) |
| Keep methods that worked | Turn repeated procedures and corrections into reusable material | [Skill distillation](docs/reference/knowledge-distillation-and-skill-fusion.md) |
| Let Agents share methods | Borrow a procedure while keeping each owner's inputs separate | [Cross-agent method sharing](docs/reference/cross-agent-skill-borrowing.md) |
| Track work and check completion | Task records, generated status, receipts and completion gates | [Task and gate guide](docs/reference/task-lifecycle.md) · [Status generator](skills/portable-agentic-system/scripts/generate_status.py) |
| Control context and concurrent work | Memory/file budgets, resource locks and worktree guidance | [Budget checker](skills/portable-agentic-system/scripts/check_budgets.py) · [Locks and concurrency](skills/portable-agentic-system/pas/references/textbook-reliability.md) |
| Change AI software or model provider | Runtime adapters and separately recorded support levels | [Adapter guide](docs/reference/compatibility.md) · [Adapter selection](skills/portable-agentic-system/pas/references/adapters.md) |
| Clean up and improve after use | Review stale instructions, noisy memory and overlapping methods | [Review and renewal](docs/reference/system-review-and-renewal.md) |

The [installable Skill](skills/portable-agentic-system/SKILL.md) brings these workflows together. Its named modes include `pas-start`, `pas-audit`, `pas-adapt`, `pas-add-agent`, `pas-create-skill`, `pas-distill`, `pas-borrow` and `pas-review`; they are requests to a supporting assistant, not terminal commands.

## How a larger personal system fits together

The second diagram shows an anonymised example: a coordinator routes work to roles with different responsibilities, while shared methods and private working material have different homes. It is an example to adapt as your needs grow.

![A coordinator, functional owner agents, shared methods and a checked execution flow](docs/assets/anonymised-agent-system-map.png)

[Open the example system map as SVG](docs/assets/anonymised-agent-system-map.svg) · [Architecture reference](docs/reference/architecture.md)

| Place | What belongs there |
|---|---|
| `AGENTS.md`, `RULES.md` | The instructions and working boundaries relevant to this project |
| `MEMORY.md` | A short recovery note and pointers to what matters next |
| `knowledge/` | Stable reference material worth retrieving again |
| `skills/` | Reusable procedures, with a clear reason to load each one |
| `tasks/`, `workspace/` | Current task state and work in progress |
| `raw_data/` | Named source material, read only within the task's allowed scope |
| `outputs/` | Reviewed results; storing something here does not send or publish it |
| `STATUS.md` | An overview generated from task records |

The [filesystem contract](skills/portable-agentic-system/pas/references/filesystem-contract.md) explains the full structure, including manifests, intermediate artifacts, logs and archives. The [file-role guide](docs/reference/file-roles.md) is a shorter introduction.

<details>
<summary>See the standard generated folder structure</summary>

```text
My Agent Workspace/
├── AGENTS.md / CLAUDE.md / GEMINI.md
├── IDENTITY.md / RULES.md / SYSTEM_MAP.md
├── MEMORY.md / STATUS.md
├── routing-evals.json / runtime-compatibility.json
├── .codex/ / .claude/ / .gemini/     Runtime configuration
├── .pas/bin/                       Local checks and gates
├── tasks/ / workspace/             Current work
├── knowledge/ / skills/             Reusable material and methods
├── raw_data/ / artifacts/ / logs/   Named inputs and working records
├── outputs/ / archive/             Reviewed and closed work
└── example-Agent/                  A role with its own files and workspace
```

This is the full standard scaffold. The guided conversation may start with a smaller teaching workspace; that is not an undocumented minimal-generator mode.

</details>

## Try the teaching example first, if you like

The [first-project exercise](examples/first-project/README.md) supplies three fictional venue notes. Compare them, check the sources, save a result, then open a new conversation and continue from a handoff. It is a way to practise before using your own materials; it is not required before building your personal system.

[Start the exercise](docs/start-here.md#practice-first) · [Reference comparison](examples/first-project/expected/comparison.md) · [Reference handoff](examples/first-project/expected/handoff.md)

<a id="technical-setup"></a>
## Optional: install the Skill or run the toolkit yourself

The guided route above is the main beginner entry. This section is for people who want direct commands, or for the AI helping them. Run these Bash/Zsh examples only after replacing the example paths with your chosen locations.

### Install the Skill

After obtaining a local copy of this repository, run from the project where you want to use the Skill. For a Codex-compatible project location:

```bash
mkdir -p .agents/skills
ln -s /path/to/Plug-And-Chug-Agentic-Building-Guide/skills/portable-agentic-system \
  .agents/skills/portable-agentic-system
```

For a personal location, use `"$HOME/.agents/skills"` as the destination instead. Read the matching adapter for discovery and loading details: [Codex](skills/portable-agentic-system/pas/adapters/codex.md), [Claude Code](skills/portable-agentic-system/pas/adapters/claude-code.md), or [Gemini CLI](skills/portable-agentic-system/pas/adapters/gemini-cli.md). Other products have [separate adapter instructions](docs/reference/compatibility.md). Installing a Skill is distinct from generating your workspace.

### Preview, generate, and check a workspace

From this repository's root, with Python 3.10 or later, set a new target and preview it:

```bash
PAS_SCRIPTS="skills/portable-agentic-system/scripts"
PAS_CONFIG="skills/portable-agentic-system/pas/examples/starter-config.json"
PAS_TARGET="../my-first-agent-workspace"
python3 "$PAS_SCRIPTS/create_agentic_system.py" \
  --root "$PAS_TARGET" --config "$PAS_CONFIG" --dry-run
```

Review the target and starter configuration. To create the previewed structure and run its checks:

```bash
python3 "$PAS_SCRIPTS/create_agentic_system.py" \
  --root "$PAS_TARGET" --config "$PAS_CONFIG"
python3 "$PAS_SCRIPTS/validate_agentic_system.py" "$PAS_TARGET"
python3 "$PAS_SCRIPTS/check_budgets.py" "$PAS_TARGET"
python3 "$PAS_SCRIPTS/check_descriptions.py" "$PAS_TARGET"
python3 "$PAS_SCRIPTS/generate_status.py" "$PAS_TARGET" --check
python3 "$PAS_SCRIPTS/harness_health_check.py" "$PAS_TARGET"
```

The generator uses the Python standard library and refuses existing files by default. A failed run may leave partial output; inspect it before retrying. [Quick start](QUICKSTART.md) includes cloning, expected results and the next steps. [Troubleshooting](docs/reference/troubleshooting.md) explains common failures.

## Reading and reference shelf

- **Learn:** [Chapter-by-chapter handbook](docs/handbook/index.md) · [English PDF](docs/downloads/Agentic-System-Building-Guide.pdf) · [Chinese PDF](docs/downloads/Agentic-System-Building-Guide.zh-CN.pdf).
- **Give your AI a reading copy:** [English playbook](skills/portable-agentic-system/pas/references/master-build-playbook.md) · [Chinese playbook](skills/portable-agentic-system/pas/references/master-build-playbook.zh-CN.md) · [Detailed build workbook](skills/portable-agentic-system/pas/references/textbook-build-workbook.md).
- **Design:** [Starting prompt](skills/portable-agentic-system/pas/references/friend-starter-prompt.md) · [Questionnaire](skills/portable-agentic-system/pas/references/intake-questions.md) · [Facilitator protocol](skills/portable-agentic-system/pas/references/facilitation-protocol.md).
- **Operate:** [Filesystem contract](skills/portable-agentic-system/pas/references/filesystem-contract.md) · [Task, gate, budget and lock governance](docs/reference/task-lifecycle.md) · [Privacy and boundaries](docs/reference/privacy-and-boundaries.md).
- **Connect and verify:** [Adapters](docs/reference/compatibility.md) · [Exact compatibility manifest](skills/portable-agentic-system/pas/compatibility/runtime-compatibility.json) · [Verification guide](docs/reference/verification.md) · [Verification receipt](docs/verification/reader-journey-verification-2026-09-22.md).
- **Explore or contribute:** [Documentation index](docs/README.md) · [Contributing and build commands](CONTRIBUTING.md) · [Changelog](CHANGELOG.md).

## What is verified

The [compatibility manifest](skills/portable-agentic-system/pas/compatibility/runtime-compatibility.json), reviewed on 2026-08-09, labels the generated Codex, Claude Code and Gemini CLI integrations `verified_static`; their fresh-session checks are `not_run`. Other adapters carry their own evidence levels. Passing local checks does not prove your installed app loaded a rule or enforced a gate. The [verification guide](docs/reference/verification.md) shows how to check your setup.

For repository development, run `python3 -m unittest discover -s tests -v`; document-build checks are in [CONTRIBUTING.md](CONTRIBUTING.md). Code and prose use the [MIT License](LICENSE); bundled fonts use [SIL OFL 1.1](THIRD_PARTY_NOTICES.md). The teaching examples contain fictional, public-safe material.

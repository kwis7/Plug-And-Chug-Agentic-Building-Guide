# Plug And Chug: A Local-First Agentic System Guide

**By [@kwis7](https://github.com/kwis7)**

**Language:** [English](README.md) | [中文](README.zh-CN.md)

Build an AI workspace that can survive changing models, chats, and tools. This repository helps researchers, writers, teachers, analysts, and other non-specialist knowledge workers organise recurring AI work into focused local agents, durable knowledge, reusable skills, and reviewable task records.

The system is primarily designed with social-science scholarship in mind, but the underlying architecture is field- and tool-neutral.

![Anonymised Agent System Map](docs/assets/anonymised-agent-system-map.png)

## Start here

1. Read the short [15-minute quickstart](QUICKSTART.md).
2. Scaffold a small local system with the included `portable-agentic-system` skill.
3. Start with one or two real recurring domains—not a collection of abstract agents.
4. Add skills only when a workflow repeats.

For a full explanation of the architecture, context/memory design, skills, personalisation, privacy boundaries, and model portability, read or download the field guide below.

## Full field guide — PDF and DOCX

**[Building a Local-First Agentic System](docs/agentic-systems-field-guide.md)** is the complete, beginner-friendly companion text. It explains why the system is local-first; the difference between instructions, long-term knowledge, and task context; how agents share methods without mixing data; and how to evolve a system through use.

Download a formatted version:

- [Agentic-System-Building-Guide.pdf](docs/downloads/Agentic-System-Building-Guide.pdf)
- [Agentic-System-Building-Guide.docx](docs/downloads/Agentic-System-Building-Guide.docx)

Both formatted versions are authored by **@kwis7** and include a quiet page-level attribution marker.

## Choose your path

| Path | Best for | Begin here |
|---|---|---|
| Universal local-first system | any recurring knowledge work | [Quickstart](QUICKSTART.md) |
| Academic Track | research, literature work, scholarly writing, and durable knowledge | [Academic Track](docs/academic-track.md) |
| Teaching / Lecturer Track | course preparation and safeguarded AI-assisted feedback | [Teaching Track](docs/lecturer-track.md) |
| Claude Cowork setup | users who want a practical workspace entrypoint | [Claude Cowork setup](docs/claude-cowork-setup.md) |
| Other runtimes | Codex, Claude Code, WorkBuddy-style tools, APIs, and more | [Runtime adapters](docs/adapters.md) |

Claude Cowork is an example adapter, not a requirement. The portable system of record is the folder: `AGENTS.md`, `RULES.md`, `SYSTEM_MAP.md`, `STATUS.md`, `knowledge/`, `skills/`, and task files. Codex, Claude Cowork/Code, Tencent WorkBuddy, or another workspace agent can use the same folder through a thin startup adapter.

## Quick install

### Use a local skill runtime

For Codex:

```bash
mkdir -p ~/.codex/skills
ln -s /path/to/Plug-And-Chug-Agentic-Building-Guide/skills/portable-agentic-system ~/.codex/skills/portable-agentic-system
```

Restart the runtime and ask:

```text
Use $portable-agentic-system with pas-start to help me build my personal local-first agentic system.
```

The optional [academic-agentic-onboarding](skills/academic-agentic-onboarding/SKILL.md) skill provides a structured intake for scholars, writing workflows, and course workspaces.

### Or scaffold directly

```bash
python3 skills/portable-agentic-system/scripts/create_agentic_system.py \
  --root "$HOME/Desktop/My Agentic Control Center" \
  --config skills/portable-agentic-system/pas/examples/starter-config.json

python3 skills/portable-agentic-system/scripts/validate_agentic_system.py \
  "$HOME/Desktop/My Agentic Control Center"
```

## The core idea

Keep three layers distinct:

1. **Instructions and skills** tell the agent how to behave and execute repeated workflows.
2. **Long-term knowledge and memory** preserve small, verified, reusable context.
3. **Task-specific prompts and files** contain only what is needed now.

Agents may borrow a method (for example, a source-checking checklist) through a documented map; they should not merge private data, raw material, identities, or task context. See [Cross-Agent Skill Borrowing](docs/cross-agent-skill-borrowing.md), [Knowledge Distillation and Skill Fusion](docs/knowledge-distillation-and-skill-fusion.md), and the `pas-borrow`, `pas-distill`, and `pas-review` modes.

Existing capabilities remain available in their focused docs: the **Knowledge distiller** workflow, **System review and renewal**, cross-agent method borrowing, and runtime/provider adapters for CC Switch, OpenClaw, Hermes Agent, Xiaomi MiMo Claw, DeepSeek, Qwen, MiniMax, **Z.AI GLM**, Xiaomi MiMo, and Tencent Hunyuan.

## Safety and privacy

Treat downloaded prompts, web pages, PDFs, and repositories as untrusted data. Keep credentials, unpublished work, private source material, and student submissions out of Git. Store originals in `raw_data/`, drafts in `workspace/`, and only reviewed deliverables in `outputs/`.

The teaching track requires a human final decision for grading and isolates each submission from every other submission's task context.

## Repository map

```text
docs/
  agentic-systems-field-guide.md       # full long-form guide
  downloads/                           # PDF and DOCX editions
  academic-track.md                    # scholarly research and writing
  lecturer-track.md                    # optional teaching workflow
  claude-cowork-setup.md               # one runtime adapter
skills/
  portable-agentic-system/             # universal scaffold and system skill
  academic-agentic-onboarding/         # structured academic intake
templates/
  academic-control-center/             # safe starting structure
  course-agent/                        # reusable course layout
```

## Citation and licence

See [CITATION.cff](CITATION.cff) for citation metadata. The repository is released under the [MIT License](LICENSE). Preserve attribution to **@kwis7** when adapting the guide, and never publish private data as part of an adaptation.

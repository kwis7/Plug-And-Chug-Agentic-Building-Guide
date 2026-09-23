# Plug & Chug

## AI Agents, Explained

Why build your own local agentic system when you already have fancy apps like Codex, Claude Code, or WorkBuddy?

[English](README.md) | [中文](README.zh-CN.md)

Good work with AI should be easy to pick up again. This guide helps you keep the materials, decisions, and useful methods from recurring projects in a workspace you control.

Start with one task you already do. Give it a place for sources, work in progress, and reviewed results. Leave a short note that lets the next session continue. As the work grows, you can add reusable skills, separate responsibilities, and stronger checks.

The toolkit provides templates and Python scripts for that structure. The handbook explains when each part helps and what still needs checking when you change AI tools.

## Choose your starting point

| I want to… | Start here |
|---|---|
| Finish a small task with AI | [Start with one task](docs/start-here.md) — supplied sources, a checked result, and a restart exercise |
| Understand the approach | [Read the handbook](docs/handbook/index.md) — English and Chinese, with downloadable PDFs |
| Generate the standard workspace | [Use the toolkit](QUICKSTART.md#manual-standard-scaffold) — complete local commands and checks |

These are alternative starting points. You do not need to install the skill or run the generator to try the learning example.

## One task, across two sessions

The [first project](examples/first-project/README.md) compares three fictional venues for a 16-person workshop after 18:00 with step-free entry.

| Input | Checked result |
|---|---|
| Cedar Hall: 18 people, 18:00–21:00, step-free entry | Meets the recorded requirements |
| Willow Room: 24 people, 09:00–17:00, step-free entry | Opening hours do not fit |
| Maple Studio: 20 people, 18:00–22:00, entry access unspecified | Needs clarification; do not invent accessibility information |

The first session saves a comparison and its source links. The next session reads a short handoff, finds the unresolved Maple question, and drafts it without sending anything. You can inspect the [reference comparison](examples/first-project/expected/comparison.md) and [reference handoff](examples/first-project/expected/handoff.md), or try first and compare afterward.

All venue information is synthetic learning data. The exercise performs no search or booking.

## The tool, the worker, and your way of working

Think of a company. You are the owner; the **model** is the employee doing the reasoning. An **agent** gives that worker a role, relevant instructions, working state and access to tools through a running application. A **prompt** gives instructions for the current work; a **Skill** packages a reusable method. Markdown (`.md`) is a readable file format for these instructions and records, not intelligence by itself.

![The company metaphor: a replaceable model inside a persistent working system](docs/assets/harness-concept-map.png)

Codex, Claude Code and WorkBuddy already provide agent capabilities. Your own system can use those capabilities: choose where authoritative work lives, which preferences apply, which methods are worth repeating, and how the next session resumes. You do not need to build another application to make those decisions explicit.

A local workspace makes that arrangement inspectable and recoverable. Personalization gives it your confirmed working standards and useful domain knowledge. The model may still run through a cloud service; local files alone do not establish offline operation or privacy. The [foundations chapter](docs/handbook/en/00-foundations.md) walks through these relationships, the company diagram and one actual execution cycle.

## What is included, and what is verified

- A bilingual learning path, fictional example, and handbook: [English PDF](docs/downloads/Agentic-System-Building-Guide.pdf) · [中文 PDF](docs/downloads/Agentic-System-Building-Guide.zh-CN.pdf).
- A self-contained [portable-agentic-system skill](skills/portable-agentic-system/SKILL.md), templates, and a standard scaffold generator.
- Local checks for generated structure, task records, budgets, routing descriptions, and status.

The generator produces native entrypoints and hook configurations for Codex, Claude Code, and Gemini CLI. The repository's [compatibility manifest](skills/portable-agentic-system/pas/compatibility/runtime-compatibility.json), reviewed on 2026-08-09, labels these `verified_static` and their fresh-session checks `not_run`. Other tools have distinct documented, manual, provisional, or provider-only classifications. See the [compatibility reference](docs/reference/compatibility.md) before connecting a tool.

Passing local checks does not prove that your installed runtime loaded instructions, enforced a hook, or completed an external action. Instructions in Markdown are not a security boundary. [Verification](docs/reference/verification.md) explains the evidence to collect.

## Contribute or adapt

Start with [CONTRIBUTING.md](CONTRIBUTING.md) for documentation, example, and toolkit changes. For exact behavior, use the [documentation index](docs/README.md) and [technical reference](docs/reference/file-roles.md).

Code and prose use the [MIT License](LICENSE); bundled fonts use [SIL OFL 1.1](THIRD_PARTY_NOTICES.md). Preserve the copyright and license notice when reusing substantial portions. Examples contain fictional, public-safe material; use your own privacy boundaries before introducing real work.

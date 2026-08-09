#!/usr/bin/env python3
"""Build the textbook-style standalone playbook from modular references."""

from __future__ import annotations

from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "portable-agentic-system"
REFERENCES = SKILL / "pas" / "references"
OUTPUT = REFERENCES / "master-build-playbook.md"
DOC_OUTPUT = ROOT / "docs" / "agentic-systems-field-guide.md"


PARTS = [
    ("Foundations — from a model to an agentic system", REFERENCES / "textbook-foundations.md"),
    ("Context, state, memory, knowledge, and files", REFERENCES / "textbook-context-state-storage.md"),
    ("Architecture and personalisation", REFERENCES / "textbook-architecture.md"),
    ("Reliability, governance, and enforcement", REFERENCES / "textbook-reliability.md"),
    ("Build workbook — from interview to verified harness", REFERENCES / "textbook-build-workbook.md"),
]

APPENDICES = [
    ("Runtime adapter matrix", ROOT / "docs" / "adapters.md"),
    ("Governance schemas and command reference", ROOT / "docs" / "governance.md"),
    ("The short starter prompt", REFERENCES / "friend-starter-prompt.md"),
]


def prepare_section(text: str) -> str:
    """Drop a module's duplicate title while preserving its internal hierarchy."""
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if not line.strip():
            continue
        if line.startswith("# "):
            lines.pop(index)
        break
    return "\n".join(lines).strip()


def build() -> str:
    intro = f"""# Building a Portable Agent Harness

*A textbook and practical workbook for understanding, designing, implementing, and verifying personal agentic systems*

Author: [@kwis7](https://github.com/kwis7)
Repository: [kwis7/Plug-And-Chug-Agentic-Building-Guide](https://github.com/kwis7/Plug-And-Chug-Agentic-Building-Guide)
Edition: 2.1 textbook draft
Generated: {date.today().isoformat()}

## What this book is for

This book explains why a capable model is not yet a dependable agent system. It develops a practical vocabulary for models, runtimes, providers, agents, skills, context, task state, memory, knowledge, data stores, tools, gates, and multi-agent coordination. It then turns those concepts into a staged build and audit method.

The emphasis is not on collecting adapter files. Runtime adapters matter, but they belong near the end because they project one durable design into a particular host. The main subject is the reasoning needed to build a personal harness that remains understandable when models, providers, and tools change.

Use this book in three ways:

1. Read Parts 1–4 as a conceptual and technical textbook.
2. Work through Part 5 to design or audit a real system.
3. Use the appendices only after the runtime and enforcement requirements are known.

The installed `portable-agentic-system` skill is intentionally shorter. It uses progressive disclosure: the runtime sees the trigger metadata first, loads the core workflow when selected, and opens these long references only for a full build, audit, or teaching handoff.

## Two maps, two jobs

The **Harness Concept Map** explains the whole idea in one page. It singles out the active replaceable model and shows that every configured component around execution belongs to the harness. The **Anonymised Example System Map** shows how the concept becomes a control center, functional domain agents, shared methods, private owner data, task flow, and quality gates.

Keep both maps. A concept diagram should not be forced to carry every implementation detail, and an example topology should not replace the core definition.

## Governing thesis

The model is the active worker, but it is not the whole system. The harness is the complete configured operating environment: instruction discovery, identity, rules, ownership, skills, tools, connectors, task contracts, state, memory, knowledge, context assembly, data lifecycle, outputs, hooks, gates, budgets, locks, worktrees, validators, and runtime adapters.

Changing the model is like replacing an employee. The company retains its charter, policies, archives, department manuals, work orders, tools, desks, and quality controls. In a single-agent system the model is the employee. Only a central coordinating model in a genuine multi-agent topology is the manager.

Knowledge is the long-term archive and institutional library. Memory is a bounded shift handover and recovery index. Task state says what is happening now. Context and workspace are the current desk. A skill is a reusable operating procedure. These objects cooperate, but they should not collapse into one file.

## Public-safe example vocabulary

Examples use generic functional names such as `Investment Analysis-Agent`, `Research-Agent`, `Application Operations-Agent`, `Report and Design-Agent`, `knowledge/`, `skills/`, `tasks/`, `workspace/`, `raw_data/`, `artifacts/`, `logs/`, `reports/`, and `outputs/`. They demonstrate structure only.

Never publish private source data, credentials, account records, client or student material, health records, unpublished corpora, absolute personal paths, task contents, logs, or report contents.

## Evidence language

- `documented`: a current official source was reviewed.
- `verified_static`: generated files, schemas, budgets, and fixtures pass.
- `verified_runtime`: a clean runtime loaded the intended entrypoint.
- `gate_verified`: an invalid closeout was blocked and a valid one accepted.
- `concurrency_verified`: lock/worktree contention and stale recovery passed.
- `external_verified`: an authorised external result was independently read back.
- `manual_projection`: the product uses projects, uploads, or folder instructions rather than a native local chain.
- `provisional`: important semantics remain unproved.

Do not compress these claims into “the adapter works”.

## Primary technical references

Runtime behavior in this edition is based on official documentation, including [Codex `AGENTS.md`](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [Codex skills](https://learn.chatgpt.com/docs/build-skills), [Codex hooks](https://learn.chatgpt.com/docs/hooks), [Claude Code memory and `CLAUDE.md`](https://code.claude.com/docs/en/memory), [Claude Code hooks](https://code.claude.com/docs/en/hooks), [Claude Code skills](https://code.claude.com/docs/en/skills), [Gemini CLI context files](https://geminicli.com/docs/cli/gemini-md/), [Gemini CLI skills](https://geminicli.com/docs/cli/skills/), and [Gemini CLI hooks](https://geminicli.com/docs/hooks/reference/). Product behavior changes; review the compatibility manifest date and refresh official sources before making a current support claim.

Architecture examples draw general lessons from [OpenHands](https://github.com/All-Hands-AI/OpenHands), [LangGraph](https://github.com/langchain-ai/langgraph), and [Letta](https://github.com/letta-ai/letta): separate model from controller/runtime, persist explicit checkpoints, and engineer memory as a bounded working set plus retrievable archive. This guide does not require those projects.
"""
    blocks = [intro.strip()]
    for number, (title, path) in enumerate(PARTS, start=1):
        if not path.exists():
            raise FileNotFoundError(path)
        blocks.append(f"# Part {number}: {title}\n\n{prepare_section(path.read_text(encoding='utf-8'))}")
    for index, (title, path) in enumerate(APPENDICES):
        if not path.exists():
            raise FileNotFoundError(path)
        letter = chr(ord("A") + index)
        blocks.append(f"# Appendix {letter}: {title}\n\n{prepare_section(path.read_text(encoding='utf-8'))}")
    return "\n\n---\n\n".join(blocks) + "\n"


if __name__ == "__main__":
    content = build()
    DOC_OUTPUT.write_text(content, encoding="utf-8")
    reference_content = content.replace(
        "../skills/portable-agentic-system/pas/compatibility/",
        "../compatibility/",
    ).replace(
        "../skills/portable-agentic-system/pas/adapters/",
        "../adapters/",
    )
    OUTPUT.write_text(reference_content, encoding="utf-8")
    print(OUTPUT)
    print(DOC_OUTPUT)

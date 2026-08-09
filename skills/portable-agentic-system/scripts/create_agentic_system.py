#!/usr/bin/env python3
"""Create a portable, local-first agent harness from canonical templates."""

from __future__ import annotations

import argparse
import json
import re
import shlex
import sys
from datetime import date
from pathlib import Path
from typing import Any

from generate_status import render_status


SKILL_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_ROOT = SKILL_ROOT / "pas" / "templates"
VAULT_DIRS = [
    "00_Inbox",
    "10_Digested",
    "20_Concepts",
    "30_Skills",
    "40_Outputs",
    "50_Reviews",
    "90_Archive",
]
ESSENTIAL_SCRIPTS = [
    "pas_common.py",
    "generate_status.py",
    "closeout_gate.py",
    "check_budgets.py",
    "check_locks.py",
    "runtime_hook_gate.py",
    "bind_task.py",
    "validate_agentic_system.py",
    "check_descriptions.py",
    "adapter_smoke.py",
    "harness_health_check.py",
]


class ScaffoldError(Exception):
    """Raised when scaffold creation cannot proceed safely."""


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    slug = re.sub(r"-{2,}", "-", slug)
    if not slug:
        raise ScaffoldError(f"Cannot derive a slug from {value!r}")
    return slug


def load_config(path: Path) -> dict[str, Any]:
    try:
        config = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ScaffoldError(f"Config file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ScaffoldError(f"Config is not valid JSON: {exc}") from exc
    if not isinstance(config, dict):
        raise ScaffoldError("Config root must be a JSON object")
    if not config.get("system_name"):
        raise ScaffoldError("Config must include system_name")
    if not isinstance(config.get("agents"), list) or not config["agents"]:
        raise ScaffoldError("Config must include a non-empty agents list")
    return config


def normalize_agents(config: dict[str, Any]) -> list[dict[str, Any]]:
    agents: list[dict[str, Any]] = []
    seen: set[str] = set()
    seen_folders: set[str] = set()
    for index, raw in enumerate(config["agents"], start=1):
        if not isinstance(raw, dict):
            raise ScaffoldError(f"Agent #{index} must be a JSON object")
        name = str(raw.get("name") or "").strip()
        if not name:
            raise ScaffoldError(f"Agent #{index} is missing name")
        slug = slugify(str(raw.get("slug") or name))
        if slug in seen:
            raise ScaffoldError(f"Duplicate agent slug: {slug}")
        seen.add(slug)
        folder_base = slug[:-6] if slug.endswith("-agent") else slug
        folder = f"{folder_base}-Agent"
        if folder in seen_folders:
            raise ScaffoldError(f"Agent folder collision after normalisation: {folder}")
        seen_folders.add(folder)
        routing_description = str(raw.get("routing_description") or "").strip()
        exclusions = raw.get("exclusions")
        positive_examples = raw.get("positive_examples")
        negative_examples = raw.get("negative_examples")
        if len(routing_description) < 80:
            raise ScaffoldError(f"Agent #{index} routing_description must be at least 80 characters and say when to use the agent")
        if not isinstance(exclusions, list) or not exclusions:
            raise ScaffoldError(f"Agent #{index} must include a non-empty exclusions list")
        if not isinstance(positive_examples, list) or len(positive_examples) < 2:
            raise ScaffoldError(f"Agent #{index} must include at least two positive_examples")
        if not isinstance(negative_examples, list) or len(negative_examples) < 2:
            raise ScaffoldError(f"Agent #{index} must include at least two negative_examples")
        agents.append(
            {
                "name": name,
                "slug": slug,
                "folder": folder,
                "purpose": str(raw.get("purpose") or "Support a recurring domain.").strip(),
                "audience": str(raw.get("audience") or "personal work").strip(),
                "vault": bool(raw.get("vault", True)),
                "routing_description": routing_description,
                "exclusions": [str(item).strip() for item in exclusions if str(item).strip()],
                "positive_examples": [str(item).strip() for item in positive_examples if str(item).strip()],
                "negative_examples": [str(item).strip() for item in negative_examples if str(item).strip()],
                "collision_examples": [str(item).strip() for item in raw.get("collision_examples", []) if str(item).strip()],
            }
        )
    return agents


def render(rel_path: str, replacements: dict[str, str]) -> str:
    path = TEMPLATE_ROOT / rel_path
    if not path.exists():
        raise ScaffoldError(f"Canonical template missing: {path}")
    text = path.read_text(encoding="utf-8")
    for token, value in replacements.items():
        text = text.replace(f"[{token}]", value)
    leftovers = sorted(set(re.findall(r"\[[A-Z][A-Z0-9_]+\]", text)))
    if leftovers:
        raise ScaffoldError(f"Unresolved template tokens in {rel_path}: {', '.join(leftovers)}")
    return text


def task_json(today: str) -> str:
    task = {
        "schema_version": 2,
        "id": "T-000-bootstrap",
        "owner": "root-control-center",
        "owner_root": ".",
        "status": "active",
        "objective": "Review and customise the generated harness before production use.",
        "scope": {
            "included": ["generated control-center and domain-agent files"],
            "excluded": ["external publishing", "credential configuration"],
        },
        "inputs": ["SYSTEM_MAP.md", "STATUS.md"],
        "authority": {
            "allowed_reads": ["."],
            "allowed_writes": ["."],
            "allowed_tools": ["local validation scripts"],
            "prohibited_actions": ["publish", "send", "delete originals", "use credentials"],
        },
        "outputs": ["STATUS.md"],
        "completion_criteria": [
            "agent roles and boundaries reviewed",
            "runtime adapter selected and smoke-tested",
            "validation and budget checks pass",
        ],
        "failure_conditions": ["required entrypoint missing", "unresolved privacy boundary"],
        "verification": {"commands": [], "receipts": []},
        "verification_state": "pending",
        "execution": {"writer": None, "parallel_write": False, "worktree": None, "resources": []},
        "handoff": {"summary": None, "next_action": "customise agent roles"},
        "created": today,
        "updated": today,
    }
    return json.dumps(task, ensure_ascii=False, indent=2) + "\n"


def storage_manifest(directory: str, context_policy: str) -> str:
    return json.dumps(
        {
            "schema_version": 1,
            "directory": directory,
            "default_context_policy": context_policy,
            "instructions": "Index files above 256 KiB before use. Never place secrets in this manifest.",
            "entry_schema": {"path": "relative/path", "size_bytes": 0, "context_policy": context_policy, "summary": "short retrieval note"},
            "entries": [],
        },
        indent=2,
    ) + "\n"


def routing_evals(agents: list[dict[str, Any]]) -> str:
    suites = []
    for agent in agents:
        suites.append(
            {
                "agent": agent["slug"],
                "description": agent["routing_description"],
                "exclusions": agent["exclusions"],
                "positive": [{"prompt": prompt, "expected": agent["slug"]} for prompt in agent["positive_examples"]],
                "negative": [{"prompt": prompt, "expected": f"not:{agent['slug']}"} for prompt in agent["negative_examples"]],
                "collision": [{"prompt": prompt, "expected": "review-boundary"} for prompt in agent["collision_examples"]],
                "runtime_observations": [],
            }
        )
    return json.dumps({"schema_version": 1, "suites": suites}, ensure_ascii=False, indent=2) + "\n"


def runtime_hook_configs(root: Path) -> dict[str, str]:
    absolute_script = shlex.quote(str((root / ".pas" / "bin" / "runtime_hook_gate.py").resolve()))
    absolute_root = shlex.quote(str(root.resolve()))
    codex_command = f"/usr/bin/env python3 {absolute_script} --runtime codex --root {absolute_root}"
    gemini_command = f"/usr/bin/env python3 {absolute_script} --runtime gemini-cli --root {absolute_root}"
    claude_command = '/usr/bin/env python3 "${CLAUDE_PROJECT_DIR}/.pas/bin/runtime_hook_gate.py" --runtime claude-code --root "${CLAUDE_PROJECT_DIR}"'
    return {
        ".codex/hooks.json": json.dumps(
            {
                "description": "Portable closeout gate. Review and trust this project hook before relying on it.",
                "hooks": {"Stop": [{"hooks": [{"type": "command", "command": codex_command, "timeout": 30, "statusMessage": "Checking portable task closeout"}]}]},
            },
            indent=2,
        ) + "\n",
        ".claude/settings.json": json.dumps(
            {"hooks": {"Stop": [{"hooks": [{"type": "command", "command": claude_command, "timeout": 30}]}]}},
            indent=2,
        ) + "\n",
        ".gemini/settings.json": json.dumps(
            {"hooks": {"AfterAgent": [{"hooks": [{"type": "command", "name": "portable-closeout-gate", "command": gemini_command, "timeout": 30000}]}]}},
            indent=2,
        ) + "\n",
        ".pas/runtime/README.md": "# Runtime bindings\n\nCodex and Gemini CLI hook configs contain generated absolute paths; Claude Code resolves `${CLAUDE_PROJECT_DIR}` at runtime. Regenerate or update absolute paths after moving this harness. A hook file is only *configured* until that runtime loads it and both an invalid and a valid closeout fixture are exercised in a fresh session. Bind a session explicitly with `.pas/bin/bind_task.py` when more than one task is active.\n",
    }


def cross_agent_map(root_name: str, agents: list[dict[str, Any]]) -> str:
    rows = "\n".join(
        f"| {a['name']} | `{a['folder']}/skills/`, `{a['folder']}/knowledge/` | "
        f"Methods related to {a['purpose']} | Raw data, identity, memory, and task state stay with the owner |"
        for a in agents
    )
    return f"""# Cross-Agent Capability Map

This is a read-only routing map for `{root_name}`. Borrow methods, not private context.

| Source agent | Borrowable methods | Useful when | Boundary |
|---|---|---|---|
{rows}

The active agent remains authoritative. Record borrowed sources in the active task package.
"""


def root_files(config: dict[str, Any], agents: list[dict[str, Any]], root: Path) -> dict[str, str]:
    today = date.today().isoformat()
    root_name = str(config["system_name"]).strip()
    values = {
        "SYSTEM_NAME": root_name,
        "OWNER_LABEL": str(config.get("owner_label") or "the user").strip(),
        "LANGUAGE": str(config.get("language") or "English").strip(),
        "DATE": today,
    }
    registry = "\n".join(
        f"| {a['name']} | `{a['folder']}/` | {a['routing_description']} | {'; '.join(a['exclusions'])} | "
        f"`{a['folder']}/tasks/` | `{a['folder']}/outputs/` |"
        for a in agents
    )
    agent_list = "\n".join(f"- **{a['name']}**: `{a['folder']}/` - {a['purpose']}" for a in agents)
    files = {
        "AGENTS.md": render("control-center/AGENTS.md", values),
        "CLAUDE.md": render("control-center/CLAUDE.md", values),
        "GEMINI.md": render("control-center/GEMINI.md", values),
        "IDENTITY.md": render("control-center/IDENTITY.md", values),
        "RULES.md": render("control-center/RULES.md", values),
        "MEMORY.md": render("control-center/MEMORY.md", values),
        "SYSTEM_MAP.md": f"""# SYSTEM_MAP

Stable ownership and routing registry for `{root_name}`. Current task state belongs in task manifests. Descriptions are routing contracts, not promotional summaries.

| Agent | Path | Routing description | Exclusions | Task state | Reviewed output |
|---|---|---|---|---|---|
{registry}
""",
        "STATUS.md": "# STATUS\n\nGenerated from `**/tasks/**/task.yaml`. Do not edit by hand.\n",
        "README.md": f"""# {root_name}

This is a local-first agent harness. The active model is replaceable; the files, gates, tools, and data boundaries around it form the harness.

## Domain agents

{agent_list}

## Start

Use the native entrypoint for the current runtime: `AGENTS.md` for Codex-compatible runtimes, `CLAUDE.md` for Claude Code, or `GEMINI.md` for Gemini CLI. Review and trust project hooks before relying on them, then run:

```bash
python3 .pas/bin/validate_agentic_system.py .
python3 .pas/bin/check_budgets.py .
python3 .pas/bin/check_descriptions.py .
python3 .pas/bin/adapter_smoke.py . --runtime codex
```

Static checks do not prove runtime loading. Exercise one deliberately invalid closeout and one valid closeout in a fresh session for every runtime you claim to support.
""",
        "knowledge/README.md": "# knowledge/\n\nLong-term institutional knowledge loaded only when relevant. This is the archive/library, not compact recovery memory.\n",
        "knowledge/cross-agent-skill-map.md": cross_agent_map(root_name, agents),
        "skills/README.md": "# skills/\n\nReusable capability packages. Use precise descriptions and test positive, negative, and collision prompts.\n",
        "routing-evals.json": routing_evals(agents),
        "tasks/README.md": "# tasks/\n\nTask contracts are authoritative for objective, authority, state, outputs, verification, resources, and handoff.\n",
        "tasks/T-000-bootstrap/task.yaml": task_json(today),
        "workspace/current.md": "# Current workspace\n\nUse this desk for active drafts and intermediate work. Task state stays in `task.yaml`.\n",
        "raw_data/README.md": "# raw_data/\n\nOriginal inputs. Read only named files; do not recursively ingest this directory. Index every file above 256 KiB in `manifest.json` with `context_policy: never-auto-load`.\n",
        "raw_data/manifest.json": storage_manifest("raw_data", "never-auto-load"),
        "artifacts/README.md": "# artifacts/\n\nGenerated intermediate files that are not reviewed deliverables.\n",
        "artifacts/manifest.json": storage_manifest("artifacts", "summary-only"),
        "logs/README.md": "# logs/\n\nExecution traces. Rotate, truncate, and summarise before loading into model context.\n",
        "logs/manifest.json": storage_manifest("logs", "summary-only"),
        "outputs/README.md": "# outputs/\n\nReviewed deliverables only. Presence here does not itself authorise external sending or publishing.\n",
        "outputs/manifest.json": storage_manifest("outputs", "named-only"),
        "runtime-compatibility.json": (SKILL_ROOT / "pas" / "compatibility" / "runtime-compatibility.json").read_text(encoding="utf-8"),
        ".pas/runtime/locks/.gitkeep": "",
        ".pas/runtime/sessions/.gitkeep": "",
        ".gitignore": """# Secrets and private inputs
.env
.env.*
*.key
*.pem
*.p12
*.pfx
raw_data/**
**/raw_data/**
!raw_data/README.md
!**/raw_data/README.md
!raw_data/manifest.json
!**/raw_data/manifest.json

# Ephemeral harness state
.pas/runtime/locks/*
!.pas/runtime/locks/.gitkeep
logs/**
!logs/README.md
!logs/manifest.json
!**/logs/README.md
!**/logs/manifest.json
.pas/runtime/sessions/*
!.pas/runtime/sessions/.gitkeep

# Caches
__pycache__/
.DS_Store
""",
    }
    files.update(runtime_hook_configs(root))
    for script_name in ESSENTIAL_SCRIPTS:
        files[f".pas/bin/{script_name}"] = (SKILL_ROOT / "scripts" / script_name).read_text(encoding="utf-8")
    return files


def agent_files(agent: dict[str, Any], config: dict[str, Any]) -> dict[str, str]:
    today = date.today().isoformat()
    values = {
        "AGENT_NAME": agent["name"],
        "SYSTEM_NAME": str(config["system_name"]).strip(),
        "PURPOSE": agent["purpose"],
        "AUDIENCE": agent["audience"],
        "LANGUAGE": str(config.get("language") or "English").strip(),
        "ROUTING_DESCRIPTION": agent["routing_description"],
        "EXCLUSIONS": "\n".join(f"- {item}" for item in agent["exclusions"]),
        "DATE": today,
    }
    files = {
        "AGENTS.md": render("domain-agent/AGENTS.md", values),
        "CLAUDE.md": render("domain-agent/CLAUDE.md", values),
        "GEMINI.md": render("domain-agent/GEMINI.md", values),
        "IDENTITY.md": render("domain-agent/IDENTITY.md", values),
        "RULES.md": render("domain-agent/RULES.md", values),
        "MEMORY.md": render("domain-agent/MEMORY.md", values),
        "README.md": f"# {agent['name']}\n\n{agent['purpose']}\n",
        "knowledge/README.md": "# knowledge/\n\nStable domain references loaded on demand.\n",
        "skills/README.md": "# skills/\n\nReusable domain workflows with tested descriptions.\n",
        "tasks/README.md": "# tasks/\n\nAuthoritative domain task contracts.\n",
        "raw_data/README.md": "# raw_data/\n\nOriginal inputs. Read only explicitly named files. Index files above 256 KiB with `context_policy: never-auto-load`.\n",
        "raw_data/manifest.json": storage_manifest("raw_data", "never-auto-load"),
        "workspace/current.md": "# Current workspace\n\nActive drafts and intermediate work.\n",
        "artifacts/README.md": "# artifacts/\n\nGenerated intermediates, caches, and calculations.\n",
        "artifacts/manifest.json": storage_manifest("artifacts", "summary-only"),
        "logs/README.md": "# logs/\n\nRotated execution traces; never treat the whole directory as model context.\n",
        "logs/manifest.json": storage_manifest("logs", "summary-only"),
        "outputs/README.md": "# outputs/\n\nReviewed deliverables. External release still requires applicable approval.\n",
        "outputs/manifest.json": storage_manifest("outputs", "named-only"),
        "archive/README.md": "# archive/\n\nClosed or superseded material. Prefer archival over destructive deletion.\n",
    }
    if agent["vault"]:
        files["vault/HOME.md"] = f"# {agent['name']} vault\n\nReviewed long-term notes; not automatic startup context.\n"
        for directory in VAULT_DIRS:
            files[f"vault/{directory}/README.md"] = f"# {directory}\n\nVault section for `{agent['name']}`.\n"
    return files


def planned_paths(root: Path, agents: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "root": str(root),
        "agents": [{"name": a["name"], "slug": a["slug"], "path": str(root / a["folder"])} for a in agents],
    }


def write_files(root: Path, files: dict[str, str], force: bool, created: list[str]) -> None:
    for rel_path, content in files.items():
        target = root / rel_path
        if target.exists() and not force:
            raise ScaffoldError(f"Refusing to overwrite existing file: {target}")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        created.append(str(target))


def scaffold(root: Path, config: dict[str, Any], force: bool) -> dict[str, Any]:
    agents = normalize_agents(config)
    created: list[str] = []
    write_files(root, root_files(config, agents, root), force, created)
    for agent in agents:
        write_files(root / agent["folder"], agent_files(agent, config), force, created)
    status_path = root / "STATUS.md"
    status_path.write_text(render_status(root), encoding="utf-8")
    summary = planned_paths(root, agents)
    summary.update({"created_count": len(created), "created": created})
    return summary


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a portable local-first agent harness.")
    parser.add_argument("--root", required=True, type=Path)
    parser.add_argument("--config", required=True, type=Path)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--force", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    try:
        config = load_config(args.config)
        agents = normalize_agents(config)
        if args.dry_run:
            plan = planned_paths(args.root, agents)
            plan["mode"] = "dry-run"
            print(json.dumps(plan, ensure_ascii=False, indent=2))
            return 0
        print(json.dumps(scaffold(args.root, config, args.force), ensure_ascii=False, indent=2))
        return 0
    except ScaffoldError as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

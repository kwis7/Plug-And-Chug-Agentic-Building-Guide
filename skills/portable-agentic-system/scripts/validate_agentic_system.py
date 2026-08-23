#!/usr/bin/env python3
"""Validate entrypoints, task contracts, budgets, paths, and privacy basics."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from check_budgets import check as check_budgets
from check_descriptions import check as check_descriptions
from adapter_smoke import smoke as adapter_smoke

from pas_common import (
    SUCCESS_STATUSES,
    TERMINAL_STATUSES,
    discover_agents,
    discover_task_manifests,
    load_manifest,
    read_text,
    task_owner_root,
    validate_task_shape,
    within,
)


ROOT_FILES = [
    "AGENTS.md",
    "CLAUDE.md",
    "GEMINI.md",
    "IDENTITY.md",
    "RULES.md",
    "MEMORY.md",
    "SYSTEM_MAP.md",
    "STATUS.md",
    "knowledge/README.md",
    "skills/README.md",
    "tasks/README.md",
    "workspace/current.md",
    "raw_data/README.md",
    "raw_data/manifest.json",
    "artifacts/README.md",
    "artifacts/manifest.json",
    "logs/README.md",
    "logs/manifest.json",
    "outputs/README.md",
    "outputs/manifest.json",
    "routing-evals.json",
    ".pas/bin/runtime_hook_gate.py",
    ".codex/hooks.json",
    ".claude/settings.json",
    ".gemini/settings.json",
]
AGENT_FILES = [
    "AGENTS.md",
    "CLAUDE.md",
    "GEMINI.md",
    "IDENTITY.md",
    "RULES.md",
    "MEMORY.md",
    "knowledge/README.md",
    "skills/README.md",
    "tasks/README.md",
    "workspace/current.md",
    "raw_data/README.md",
    "raw_data/manifest.json",
    "artifacts/README.md",
    "artifacts/manifest.json",
    "logs/README.md",
    "logs/manifest.json",
    "outputs/README.md",
    "outputs/manifest.json",
    "archive/README.md",
]
LEGACY_AGENT_FILES = [
    "AGENTS.md",
    "CLAUDE.md",
    "IDENTITY.md",
    "RULES.md",
    "MEMORY.md",
    "workspace/current.md",
]
PROJECT_AGENT_FILES = [
    "AGENTS.md",
    "CLAUDE.md",
    "README.md",
    "STATUS.md",
    "workspace/current.md",
]
SECRET_RE = re.compile(r"(api[_-]?key|secret[_-]?key|access[_-]?token|private[_-]?key|password)\s*[:=]", re.I)
ACTIVE_IMPORT_RE = re.compile(r"^\s*@import\s+", re.M)


def check_required(root: Path, paths: list[str], label: str, errors: list[str]) -> None:
    for rel in paths:
        if not (root / rel).exists():
            errors.append(f"{label} missing required file: {rel}")


def check_entrypoints(root: Path, label: str, errors: list[str]) -> None:
    agents = root / "AGENTS.md"
    claude = root / "CLAUDE.md"
    gemini = root / "GEMINI.md"
    for path in [agents, claude, gemini]:
        if path.exists() and ACTIVE_IMPORT_RE.search(read_text(path)):
            errors.append(f"{label}/{path.name} uses unsupported @import syntax")
    if agents.exists() and agents.stat().st_size > 24 * 1024:
        errors.append(f"{label}/AGENTS.md exceeds portable 24 KiB hard limit")
    if claude.exists():
        lines = [line.strip() for line in read_text(claude).splitlines() if line.strip()]
        if not lines or lines[0] != "@AGENTS.md":
            errors.append(f"{label}/CLAUDE.md must bridge with @AGENTS.md on its first operative line")
        if claude.stat().st_size > 4 * 1024:
            errors.append(f"{label}/CLAUDE.md exceeds 4 KiB delta limit")
    if gemini.exists():
        lines = [line.strip() for line in read_text(gemini).splitlines() if line.strip()]
        if not lines or lines[0] != "@./AGENTS.md":
            errors.append(f"{label}/GEMINI.md must bridge with @./AGENTS.md on its first operative line")
        if gemini.stat().st_size > 4 * 1024:
            errors.append(f"{label}/GEMINI.md exceeds 4 KiB delta limit")


def check_memory(path: Path, byte_limit: int, line_limit: int, errors: list[str]) -> None:
    if not path.exists():
        return
    lines = read_text(path).splitlines()
    if path.stat().st_size > byte_limit or len(lines) > line_limit:
        errors.append(f"{path} exceeds memory budget ({byte_limit} bytes/{line_limit} lines)")


def validate_tasks(root: Path, errors: list[str], warnings: list[str]) -> list[Path]:
    paths = discover_task_manifests(root)
    if not paths:
        errors.append("No task manifests found under **/tasks/**/task.yaml")
        return paths
    for path in paths:
        rel = path.relative_to(root)
        try:
            task = load_manifest(path)
        except (ValueError, OSError) as exc:
            errors.append(f"{rel} cannot be parsed: {exc}")
            continue
        errors.extend(f"{rel} {message}" for message in validate_task_shape(task))
        try:
            owner = task_owner_root(root, path, task)
        except ValueError as exc:
            errors.append(f"{rel} {exc}")
            continue
        status = str(task.get("status", "")).lower()
        for output in task.get("outputs", []):
            candidate = (owner / str(output)).resolve()
            if not within(candidate, owner):
                errors.append(f"{rel} output escapes owner root: {output}")
            if status in SUCCESS_STATUSES and not candidate.exists():
                errors.append(f"{rel} terminal output missing: {output}")
        if status in SUCCESS_STATUSES:
            if task.get("verification_state") != "passed":
                errors.append(f"{rel} successful terminal task must have verification_state: passed")
            verification = task.get("verification", {})
            if not isinstance(verification, dict) or not verification.get("receipts"):
                errors.append(f"{rel} successful terminal task requires verification receipts")
        if status in TERMINAL_STATUSES:
            handoff = task.get("handoff", {})
            if not isinstance(handoff, dict) or not handoff.get("summary"):
                errors.append(f"{rel} terminal task requires handoff.summary")
        elif task.get("verification_state") == "passed":
            warnings.append(f"{rel} is non-terminal but already marked verification_state: passed")
    return paths


def scan_secrets(root: Path, errors: list[str]) -> None:
    for path in root.glob("**/*"):
        if not path.is_file() or ".git" in path.parts or path.suffix.lower() not in {".md", ".yaml", ".yml", ".json"}:
            continue
        if path.stat().st_size > 512 * 1024:
            continue
        if SECRET_RE.search(read_text(path)):
            errors.append(f"secret-like assignment found in {path.relative_to(root)}")


def agent_mode(root: Path, agent: Path) -> str:
    """Return the optional mode declared for an Agent in SYSTEM_MAP.md."""

    source = root / "SYSTEM_MAP.md"
    if not source.exists():
        return "standard"
    for line in read_text(source).splitlines():
        if not line.startswith("|") or "---" in line:
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) < 5 or cells[0].lower() == "agent":
            continue
        candidate = cells[1].strip("` ").rstrip("/")
        if candidate == agent.name:
            return cells[4].lower() or "standard"
    return "standard"


def validate(root: Path, inherited_root: Path | None = None) -> dict[str, object]:
    root = root.resolve()
    errors: list[str] = []
    warnings: list[str] = []
    if not root.exists():
        errors.append(f"Root does not exist: {root}")
        return {"root": str(root), "valid": False, "error_count": 1, "warning_count": 0, "errors": errors, "warnings": warnings}
    check_required(root, ROOT_FILES, "root", errors)
    check_entrypoints(root, "root", errors)
    check_memory(root / "MEMORY.md", 12 * 1024, 120, errors)
    agents = discover_agents(root)
    if not agents:
        errors.append("No domain agent folders found")
    for agent in agents:
        mode = agent_mode(root, agent)
        if mode == "placeholder":
            continue
        required = PROJECT_AGENT_FILES if mode == "project" else LEGACY_AGENT_FILES if mode == "legacy" else AGENT_FILES
        check_required(agent, required, agent.name, errors)
        check_entrypoints(agent, agent.name, errors)
        check_memory(agent / "MEMORY.md", 8 * 1024, 100, errors)
    tasks = validate_tasks(root, errors, warnings)
    budget_report = check_budgets(root)
    errors.extend(f"budget/storage: {item}" for item in budget_report["violations"])
    description_report = check_descriptions(root)
    errors.extend(f"description/routing: {item}" for item in description_report["issues"])
    errors.extend(f"description collision: {item}" for item in description_report["collisions"])
    adapter_root = inherited_root.resolve() if inherited_root else root
    adapter_reports = [adapter_smoke(adapter_root, runtime) for runtime in ("codex", "claude-code", "gemini-cli")]
    for report in adapter_reports:
        failed_checks = [item["name"] for item in report["checks"] if not item["passed"]]
        if failed_checks:
            errors.append(f"{report['runtime']} static adapter failed: {', '.join(failed_checks)}")
    scan_secrets(root, errors)
    return {
        "root": str(root),
        "valid": not errors,
        "error_count": len(errors),
        "warning_count": len(warnings),
        "agent_count": len(agents),
        "task_count": len(tasks),
        "budget_files_checked": budget_report["checked"],
        "routing_agents_checked": description_report["routing_agents"],
        "adapter_static_reports": adapter_reports,
        "agents": [agent.name for agent in agents],
        "errors": errors,
        "warnings": warnings,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    args = parser.parse_args(argv or sys.argv[1:])
    report = validate(args.root)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

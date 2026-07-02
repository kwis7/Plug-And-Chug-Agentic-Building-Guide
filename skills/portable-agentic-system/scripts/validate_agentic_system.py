#!/usr/bin/env python3
"""Validate a local-first personal agentic system scaffold."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ROOT_FILES = [
    "AGENTS.md",
    "CLAUDE.md",
    "IDENTITY.md",
    "RULES.md",
    "MEMORY.md",
    "SYSTEM_MAP.md",
    "STATUS.md",
    "knowledge/README.md",
    "skills/README.md",
    "tasks/README.md",
    "workspace/current.md",
]

AGENT_FILES = [
    "AGENTS.md",
    "CLAUDE.md",
    "IDENTITY.md",
    "RULES.md",
    "MEMORY.md",
    "knowledge/README.md",
    "skills/README.md",
    "raw_data/README.md",
    "workspace/current.md",
    "outputs/README.md",
    "archive/README.md",
]

TASK_REQUIRED_KEYS = ["id", "owner", "status", "outputs", "verification", "next_action"]

VAULT_FILES = [
    "vault/HOME.md",
    "vault/00_Inbox/README.md",
    "vault/10_Digested/README.md",
    "vault/20_Concepts/README.md",
    "vault/30_Skills/README.md",
    "vault/40_Outputs/README.md",
    "vault/50_Reviews/README.md",
    "vault/90_Archive/README.md",
]

SECRET_RE = re.compile(
    r"(api[_-]?key|secret[_-]?key|access[_-]?token|private[_-]?key|password)\s*[:=]",
    re.IGNORECASE,
)

IMPORT_RE = re.compile(r"@import\s+(.+)")


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(errors="replace")


def check_required_files(root: Path, required: list[str], label: str, errors: list[str]) -> None:
    for rel_path in required:
        if not (root / rel_path).exists():
            errors.append(f"{label} missing required file: {rel_path}")


def check_imports(root: Path, rel_path: str, errors: list[str]) -> None:
    path = root / rel_path
    if not path.exists():
        return
    for line in read_text(path).splitlines():
        match = IMPORT_RE.search(line)
        if not match:
            continue
        imported = match.group(1).strip()
        target = (path.parent / imported).resolve()
        try:
            target.relative_to(root.resolve())
        except ValueError:
            errors.append(f"{rel_path} imports outside root: {imported}")
            continue
        if not target.exists():
            errors.append(f"{rel_path} imports missing file: {imported}")


def scan_secret_like_strings(root: Path, errors: list[str], warnings: list[str]) -> None:
    for rel_path in ["IDENTITY.md", "RULES.md", "MEMORY.md", "SYSTEM_MAP.md", "STATUS.md", "workspace/current.md"]:
        path = root / rel_path
        if path.exists() and SECRET_RE.search(read_text(path)):
            errors.append(f"Secret-like string found in {rel_path}")

    for agent in discover_agents(root):
        for rel_path in ["IDENTITY.md", "RULES.md", "MEMORY.md", "workspace/current.md"]:
            path = agent / rel_path
            if path.exists() and SECRET_RE.search(read_text(path)):
                warnings.append(f"Secret-like string found in {agent.name}/{rel_path}")


def registry_agent_paths(root: Path) -> list[Path]:
    source = root / "SYSTEM_MAP.md"
    if not source.exists():
        source = root / "MEMORY.md"
    if not source.exists():
        return []
    paths: list[Path] = []
    for line in read_text(source).splitlines():
        if not line.startswith("|") or "---" in line:
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) < 2 or cells[0].lower() == "agent":
            continue
        candidate = cells[1].strip("` ")
        if candidate.endswith("/"):
            candidate = candidate[:-1]
        if candidate:
            path = root / candidate
            if path.exists() and path.is_dir():
                paths.append(path)
    return paths


def discover_agents(root: Path) -> list[Path]:
    registered = registry_agent_paths(root)
    discovered = [path for path in root.glob("*-Agent") if path.is_dir()]
    combined: dict[str, Path] = {path.name: path for path in registered + discovered}
    return [combined[name] for name in sorted(combined)]


def parse_task_manifest(path: Path) -> dict[str, object]:
    manifest: dict[str, object] = {}
    current_list_key: str | None = None
    for raw_line in read_text(path).splitlines():
        line = raw_line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        if line.startswith("  - ") and current_list_key:
            value = line[4:].strip()
            manifest.setdefault(current_list_key, [])
            if isinstance(manifest[current_list_key], list):
                manifest[current_list_key].append(value)
            continue
        if ":" not in line or line.startswith(" "):
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value:
            manifest[key] = value.strip('"')
            current_list_key = None
        else:
            manifest[key] = []
            current_list_key = key
    return manifest


def discover_task_manifests(root: Path) -> list[Path]:
    return sorted(root.glob("tasks/**/task.yaml"))


def validate_task_manifests(root: Path, errors: list[str], warnings: list[str]) -> list[Path]:
    tasks = discover_task_manifests(root)
    if not tasks:
        warnings.append("No task manifests found under tasks/**/task.yaml")
        return tasks
    for task in tasks:
        manifest = parse_task_manifest(task)
        for key in TASK_REQUIRED_KEYS:
            if key not in manifest:
                errors.append(f"{task.relative_to(root)} missing required key: {key}")
        for key in ["outputs", "verification"]:
            if key in manifest and not manifest[key]:
                errors.append(f"{task.relative_to(root)} has empty {key}")
    return tasks


def validate(root: Path) -> dict[str, object]:
    errors: list[str] = []
    warnings: list[str] = []
    root = root.resolve()

    if not root.exists():
        errors.append(f"Root does not exist: {root}")
        return {
            "root": str(root),
            "valid": False,
            "error_count": len(errors),
            "warning_count": 0,
            "agent_count": 0,
            "task_count": 0,
            "errors": errors,
            "warnings": warnings,
        }

    check_required_files(root, ROOT_FILES, "root", errors)
    check_imports(root, "AGENTS.md", errors)
    check_imports(root, "CLAUDE.md", errors)
    tasks = validate_task_manifests(root, errors, warnings)

    agents = discover_agents(root)
    if not agents:
        errors.append("No domain agent folders found")

    for agent in agents:
        check_required_files(agent, AGENT_FILES, agent.name, errors)
        check_imports(agent, "AGENTS.md", errors)
        check_imports(agent, "CLAUDE.md", errors)
        missing_vault = [rel_path for rel_path in VAULT_FILES if not (agent / rel_path).exists()]
        if missing_vault:
            warnings.append(f"{agent.name} has incomplete or missing vault files: {', '.join(missing_vault)}")

    scan_secret_like_strings(root, errors, warnings)

    return {
        "root": str(root),
        "valid": not errors,
        "error_count": len(errors),
        "warning_count": len(warnings),
        "agent_count": len(agents),
        "task_count": len(tasks),
        "agents": [agent.name for agent in agents],
        "errors": errors,
        "warnings": warnings,
    }


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate a portable personal agentic system scaffold.")
    parser.add_argument("root", type=Path, help="System root to validate")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    report = validate(args.root)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

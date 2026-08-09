#!/usr/bin/env python3
"""Shared stdlib-only helpers for Portable Agentic System scripts."""

from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path
from typing import Any


SUCCESS_STATUSES = {"complete", "completed"}
UNSUCCESSFUL_TERMINAL_STATUSES = {"cancelled", "failed"}
TERMINAL_STATUSES = SUCCESS_STATUSES | UNSUCCESSFUL_TERMINAL_STATUSES
ACTIVE_STATUSES = {"active", "in_progress", "waiting_review", "blocked"}
TASK_REQUIRED_KEYS = {
    "schema_version",
    "id",
    "owner",
    "owner_root",
    "status",
    "objective",
    "scope",
    "inputs",
    "authority",
    "outputs",
    "completion_criteria",
    "failure_conditions",
    "verification",
    "verification_state",
    "execution",
    "handoff",
}


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(errors="replace")


def parse_scalar(value: str) -> Any:
    value = value.strip()
    if value in {"", "null", "Null", "NULL", "~"}:
        return None
    if value.lower() in {"true", "false"}:
        return value.lower() == "true"
    if value.startswith(("[", "{", "'", '"')):
        try:
            return ast.literal_eval(value)
        except (SyntaxError, ValueError):
            pass
    try:
        return int(value)
    except ValueError:
        return value.strip("\"'")


def parse_simple_yaml(text: str) -> dict[str, Any]:
    """Parse the conservative YAML subset used by PAS examples.

    JSON is preferred and is valid YAML. This fallback supports indented maps and
    scalar lists without requiring PyYAML in a new user's environment.
    """

    root: dict[str, Any] = {}
    stack: list[tuple[int, Any]] = [(-1, root)]
    lines = text.splitlines()
    for index, raw in enumerate(lines):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        line = raw.strip()
        while len(stack) > 1 and indent <= stack[-1][0]:
            stack.pop()
        parent = stack[-1][1]
        if line.startswith("- "):
            if not isinstance(parent, list):
                raise ValueError(f"List item without list parent on line {index + 1}")
            parent.append(parse_scalar(line[2:]))
            continue
        if ":" not in line or not isinstance(parent, dict):
            raise ValueError(f"Unsupported YAML syntax on line {index + 1}")
        key, raw_value = line.split(":", 1)
        key = key.strip()
        raw_value = raw_value.strip()
        if raw_value:
            parent[key] = parse_scalar(raw_value)
            continue
        next_nonempty = ""
        for candidate in lines[index + 1 :]:
            if candidate.strip() and not candidate.lstrip().startswith("#"):
                next_nonempty = candidate.strip()
                break
        child: Any = [] if next_nonempty.startswith("- ") else {}
        parent[key] = child
        stack.append((indent, child))
    return root


def load_manifest(path: Path) -> dict[str, Any]:
    text = read_text(path)
    try:
        value = json.loads(text)
    except json.JSONDecodeError:
        value = parse_simple_yaml(text)
    if not isinstance(value, dict):
        raise ValueError("manifest root must be an object")
    return value


def discover_task_manifests(root: Path) -> list[Path]:
    tasks = []
    for path in root.glob("**/tasks/**/task.yaml"):
        if ".git" not in path.parts and path.is_file():
            tasks.append(path)
    return sorted(tasks)


def find_task_by_id(root: Path, task_id: str) -> Path | None:
    matches = []
    for path in discover_task_manifests(root):
        try:
            if str(load_manifest(path).get("id")) == task_id:
                matches.append(path)
        except (OSError, ValueError):
            continue
    if len(matches) > 1:
        raise ValueError(f"task id is not unique: {task_id}")
    return matches[0] if matches else None


def discover_agents(root: Path) -> list[Path]:
    return sorted(path for path in root.glob("*-Agent") if path.is_dir())


def within(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
        return True
    except ValueError:
        return False


def task_owner_root(system_root: Path, task_path: Path, manifest: dict[str, Any]) -> Path:
    declared = str(manifest.get("owner_root") or ".")
    candidate = (system_root / declared).resolve()
    if not within(candidate, system_root):
        raise ValueError(f"owner_root escapes system root: {declared}")
    return candidate


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_task_shape(manifest: dict[str, Any]) -> list[str]:
    errors = [f"missing required key: {key}" for key in sorted(TASK_REQUIRED_KEYS - set(manifest))]
    if manifest.get("schema_version") != 2:
        errors.append("schema_version must be 2")
    for key in ["inputs", "outputs", "completion_criteria", "failure_conditions"]:
        if key in manifest and not isinstance(manifest[key], list):
            errors.append(f"{key} must be a list")
    for key in ["scope", "authority", "verification", "execution", "handoff"]:
        if key in manifest and not isinstance(manifest[key], dict):
            errors.append(f"{key} must be an object")
    authority = manifest.get("authority")
    if isinstance(authority, dict):
        for key in ["allowed_reads", "allowed_writes", "allowed_tools", "prohibited_actions"]:
            if key not in authority or not isinstance(authority.get(key), list):
                errors.append(f"authority.{key} must be a list")
    verification = manifest.get("verification")
    if isinstance(verification, dict):
        for key in ["commands", "receipts"]:
            if key not in verification or not isinstance(verification.get(key), list):
                errors.append(f"verification.{key} must be a list")
    execution = manifest.get("execution")
    if isinstance(execution, dict):
        if not isinstance(execution.get("resources", []), list):
            errors.append("execution.resources must be a list")
        if execution.get("parallel_write") and not execution.get("worktree"):
            errors.append("execution.worktree is required when parallel_write is true")
    return errors

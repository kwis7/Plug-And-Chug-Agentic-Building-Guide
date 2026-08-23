#!/usr/bin/env python3
"""Report harness health without overstating runtime verification."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

import validate_agentic_system as validator
from adapter_smoke import smoke as adapter_smoke
from pas_common import ACTIVE_STATUSES, SUCCESS_STATUSES, discover_task_manifests, load_manifest


SENSITIVE_SUFFIXES = {".pem", ".key", ".p12", ".pfx"}


def sensitive_tracked_path(value: str) -> bool:
    """Flag likely private payloads without rejecting public-safe metadata files."""

    path = Path(value.replace("\\", "/"))
    lowered_parts = [part.lower() for part in path.parts]
    name = path.name.lower()
    if name == ".env" or name.startswith(".env.") or path.suffix.lower() in SENSITIVE_SUFFIXES:
        return True
    if "private" in lowered_parts:
        return True
    if "raw_data" in lowered_parts and name not in {"readme.md", "manifest.json", ".gitkeep"}:
        return True
    return False


def tracked_sensitive(root: Path) -> list[str]:
    result = subprocess.run(["git", "-C", str(root), "ls-files"], text=True, capture_output=True, check=False)
    if result.returncode != 0:
        return []
    return [line for line in result.stdout.splitlines() if sensitive_tracked_path(line)]


def _effective_errors(root: Path, inherited_root: Path | None, errors: list[str]) -> list[str]:
    if inherited_root is None:
        return errors
    effective = []
    for error in errors:
        if error.startswith("root missing required file: "):
            rel = error.removeprefix("root missing required file: ")
            if (inherited_root / rel).exists():
                continue
        if error == "No domain agent folders found":
            continue
        if error == "No task manifests found under **/tasks/**/task.yaml":
            continue
        if error.startswith(("codex static adapter failed:", "claude-code static adapter failed:", "gemini-cli static adapter failed:")):
            continue
        effective.append(error)
    return effective


def health(root: Path, inherited_root: Path | None = None) -> dict[str, object]:
    inherited_root = inherited_root.resolve() if inherited_root else None
    validation = validator.validate(root, inherited_root)
    effective_errors = _effective_errors(root, inherited_root, list(validation.get("errors", [])))
    effective_validation = {
        **validation,
        "errors": effective_errors,
        "error_count": len(effective_errors),
        "valid": not effective_errors,
    }
    sensitive = tracked_sensitive(root)
    tasks = []
    active = 0
    terminal_without_receipts = 0
    for path in discover_task_manifests(root):
        task = load_manifest(path)
        status = str(task.get("status") or "").lower()
        active += status in ACTIVE_STATUSES
        verification = task.get("verification") if isinstance(task.get("verification"), dict) else {}
        if status in SUCCESS_STATUSES and not verification.get("receipts"):
            terminal_without_receipts += 1
        tasks.append({"id": task.get("id"), "status": status, "verification_state": task.get("verification_state")})
    adapter_root = inherited_root or root
    adapter_reports = [adapter_smoke(adapter_root, runtime) for runtime in ("codex", "claude-code", "gemini-cli")]
    adapter_failures = [report["runtime"] for report in adapter_reports if not report["passed"]]
    deductions = int(effective_validation.get("error_count", 0)) * 12 + int(validation.get("warning_count", 0)) * 3
    deductions += len(adapter_failures) * 12
    deductions += len(sensitive) * 20 + terminal_without_receipts * 15
    score = max(0, min(100, 100 - deductions))
    return {
        "root": str(root),
        "inherited_root": str(inherited_root) if inherited_root else None,
        "score": score,
        "static_valid": effective_validation.get("valid", False) and not sensitive and not adapter_failures,
        "runtime_verification": "not_run",
        "agent_count": validation.get("agent_count", 0),
        "task_count": len(tasks),
        "active_tasks": active,
        "terminal_tasks_without_receipts": terminal_without_receipts,
        "sensitive_files_tracked": sensitive,
        "adapter_static_reports": adapter_reports,
        "adapter_static_failures": adapter_failures,
        "errors": effective_errors,
        "warnings": validation.get("warnings", []),
        "tasks": tasks,
        "note": "A static score never proves native runtime loading, hook execution, external delivery, or deployment.",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("--inherit-root", type=Path, help="Shared control-center root inherited by a lightweight leaf Agent")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv or sys.argv[1:])
    report = health(args.root.resolve(), args.inherit_root)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"Static harness health: {report['score']}/100")
        print(f"Runtime verification: {report['runtime_verification']}")
        for error in report["errors"]:
            print(f"ERROR: {error}")
        for warning in report["warnings"]:
            print(f"WARNING: {warning}")
        print(report["note"])
    return 0 if report["static_valid"] and report["score"] >= 80 else 1


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Run a lightweight health check for a personal agentic harness."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

import validate_agentic_system as validator


SENSITIVE_TRACKED_PATTERNS = (
    ".env",
    "raw_data/",
    "/raw_data/",
    "private/",
    "/private/",
    ".pem",
    ".key",
    ".p12",
    ".pfx",
)


def git_tracked_files(root: Path) -> list[str]:
    result = subprocess.run(
        ["git", "-C", str(root), "ls-files"],
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        return []
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def sensitive_tracked_files(root: Path) -> list[str]:
    tracked = git_tracked_files(root)
    sensitive: list[str] = []
    for rel_path in tracked:
        normalized = rel_path.replace("\\", "/")
        if any(pattern in normalized for pattern in SENSITIVE_TRACKED_PATTERNS):
            sensitive.append(rel_path)
    return sensitive


def task_status_counts(root: Path) -> tuple[int, int, int]:
    active = 0
    missing_verification = 0
    missing_next_action = 0
    for task_path in validator.discover_task_manifests(root):
        manifest = validator.parse_task_manifest(task_path)
        status = str(manifest.get("status", "")).strip().lower()
        if status in {"active", "waiting_review", "blocked", "in_progress"}:
            active += 1
        if not manifest.get("verification"):
            missing_verification += 1
        if not manifest.get("next_action"):
            missing_next_action += 1
    return active, missing_verification, missing_next_action


def score_report(
    validation: dict[str, object],
    sensitive_files: list[str],
    tasks_without_verification: int,
    tasks_without_next_action: int,
) -> int:
    score = 100
    score -= int(validation.get("error_count", 0)) * 12
    score -= int(validation.get("warning_count", 0)) * 4
    score -= len(sensitive_files) * 20
    score -= tasks_without_verification * 10
    score -= tasks_without_next_action * 8
    return max(0, min(100, score))


def health_check(root: Path) -> dict[str, object]:
    root = root.resolve()
    validation = validator.validate(root)
    sensitive_files = sensitive_tracked_files(root)
    active_tasks, tasks_without_verification, tasks_without_next_action = task_status_counts(root)
    errors = list(validation.get("errors", []))
    broken_references = len([error for error in errors if "missing" in error.lower() or "imports" in error.lower()])

    report = {
        "root": str(root),
        "score": score_report(validation, sensitive_files, tasks_without_verification, tasks_without_next_action),
        "valid": validation.get("valid", False) and not sensitive_files,
        "agent_count": validation.get("agent_count", 0),
        "task_count": validation.get("task_count", 0),
        "active_tasks": active_tasks,
        "broken_references": broken_references,
        "tasks_without_verification": tasks_without_verification,
        "tasks_without_next_action": tasks_without_next_action,
        "sensitive_files_tracked": len(sensitive_files),
        "sensitive_files": sensitive_files,
        "errors": validation.get("errors", []),
        "warnings": validation.get("warnings", []),
    }
    return report


def print_text(report: dict[str, object]) -> None:
    print(f"Harness health: {report['score']}/100")
    print(f"{report['broken_references']} broken references")
    print(f"{report['active_tasks']} active tasks")
    print(f"{report['tasks_without_verification']} tasks without verification")
    print(f"{report['sensitive_files_tracked']} sensitive files tracked by Git")
    if report["errors"]:
        print("\nErrors:")
        for error in report["errors"]:
            print(f"- {error}")
    if report["warnings"]:
        print("\nWarnings:")
        for warning in report["warnings"]:
            print(f"- {warning}")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a lightweight health check for a personal agentic harness.")
    parser.add_argument("root", type=Path, help="System root to check")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    report = health_check(args.root)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print_text(report)
    return 0 if report["score"] >= 80 and not report["errors"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

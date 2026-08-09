#!/usr/bin/env python3
"""Block terminal completion until outputs, receipts, status, and locks are valid."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from pas_common import SUCCESS_STATUSES, TERMINAL_STATUSES, load_manifest, task_owner_root, validate_task_shape, within


def gate(root: Path, task_path: Path) -> dict[str, object]:
    errors: list[str] = []
    task = load_manifest(task_path)
    errors.extend(validate_task_shape(task))
    status = str(task.get("status") or "").lower()
    if status not in TERMINAL_STATUSES:
        errors.append(f"task status is not terminal: {status}")
    owner = task_owner_root(root, task_path, task)
    if status in SUCCESS_STATUSES:
        for output in task.get("outputs", []):
            candidate = (owner / str(output)).resolve()
            if not within(candidate, owner):
                errors.append(f"output escapes owner root: {output}")
            elif not candidate.exists():
                errors.append(f"declared output missing: {output}")
        if not task.get("completion_criteria"):
            errors.append("completion_criteria is empty")
        if task.get("verification_state") != "passed":
            errors.append("verification_state must be passed")
    verification = task.get("verification") if isinstance(task.get("verification"), dict) else {}
    receipts = verification.get("receipts") if isinstance(verification, dict) else []
    if status in SUCCESS_STATUSES and not receipts:
        errors.append("verification receipts are required")
    elif receipts:
        for receipt in receipts:
            path = (owner / str(receipt)).resolve()
            if not within(path, owner) or not path.exists():
                errors.append(f"verification receipt missing or outside owner root: {receipt}")
    lock_dir = root / ".pas" / "runtime" / "locks"
    remaining = []
    if lock_dir.exists():
        for path in lock_dir.glob("*.lock.json"):
            try:
                lock = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                remaining.append(path.name)
                continue
            if str(lock.get("task_id")) == str(task.get("id")):
                remaining.append(path.name)
    if remaining:
        errors.append(f"exclusive/resource locks remain: {', '.join(sorted(remaining))}")
    status_check = subprocess.run(
        [sys.executable, str(Path(__file__).with_name("generate_status.py")), str(root), "--check"],
        text=True,
        capture_output=True,
        check=False,
    )
    if status_check.returncode != 0:
        errors.append("STATUS.md is stale")
    budget_check = subprocess.run(
        [sys.executable, str(Path(__file__).with_name("check_budgets.py")), str(root)],
        text=True,
        capture_output=True,
        check=False,
    )
    if budget_check.returncode != 0:
        errors.append("instruction, memory, or storage budget check failed")
    handoff = task.get("handoff") if isinstance(task.get("handoff"), dict) else {}
    if not handoff.get("summary"):
        errors.append("handoff.summary is required for terminal closeout")
    return {"task": str(task_path), "passed": not errors, "errors": errors}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("task", type=Path)
    args = parser.parse_args(argv or sys.argv[1:])
    root = args.root.resolve()
    task = args.task if args.task.is_absolute() else root / args.task
    report = gate(root, task.resolve())
    print(json.dumps(report, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Generate STATUS.md deterministically from task manifests."""

from __future__ import annotations

import argparse
import difflib
import sys
from pathlib import Path

from pas_common import discover_task_manifests, load_manifest


ORDER = ["active", "in_progress", "waiting_review", "blocked", "complete", "completed", "failed", "cancelled"]


def render_status(root: Path) -> str:
    grouped: dict[str, list[tuple[str, str, str, str]]] = {}
    for path in discover_task_manifests(root):
        task = load_manifest(path)
        status = str(task.get("status") or "unknown").lower()
        handoff = task.get("handoff") if isinstance(task.get("handoff"), dict) else {}
        grouped.setdefault(status, []).append(
            (
                str(task.get("id") or path.parent.name),
                str(task.get("owner") or "unknown"),
                str(task.get("objective") or ""),
                str(handoff.get("next_action") or ""),
            )
        )
    lines = ["# STATUS", "", "Generated from `**/tasks/**/task.yaml`. Do not edit by hand.", ""]
    statuses = ORDER + sorted(set(grouped) - set(ORDER))
    for status in statuses:
        if status not in grouped:
            continue
        lines.extend([f"## {status}", "", "| Task | Owner | Objective | Next action |", "|---|---|---|---|"])
        for task_id, owner, objective, next_action in sorted(grouped[status]):
            clean = lambda value: value.replace("|", "\\|").replace("\n", " ")
            lines.append(f"| {clean(task_id)} | {clean(owner)} | {clean(objective)} | {clean(next_action)} |")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv or sys.argv[1:])
    expected = render_status(args.root.resolve())
    path = args.root.resolve() / "STATUS.md"
    current = path.read_text(encoding="utf-8") if path.exists() else ""
    if args.check:
        if current == expected:
            print("STATUS.md is current")
            return 0
        print("".join(difflib.unified_diff(current.splitlines(True), expected.splitlines(True), fromfile="STATUS.md", tofile="generated")))
        return 1
    path.write_text(expected, encoding="utf-8")
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

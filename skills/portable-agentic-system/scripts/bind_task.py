#!/usr/bin/env python3
"""Bind one runtime session id to one portable task manifest."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from pas_common import load_manifest, within


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("task", type=Path)
    parser.add_argument("--session", required=True)
    args = parser.parse_args(argv or sys.argv[1:])
    root = args.root.resolve()
    if not re.fullmatch(r"[A-Za-z0-9._-]{1,200}", args.session):
        print("session must use only letters, numbers, dots, underscores, and hyphens", file=sys.stderr)
        return 1
    task = args.task if args.task.is_absolute() else root / args.task
    task = task.resolve()
    if not within(task, root) or task.name != "task.yaml" or not task.exists():
        print("task must be an existing task.yaml inside root", file=sys.stderr)
        return 1
    load_manifest(task)
    directory = root / ".pas" / "runtime" / "sessions"
    directory.mkdir(parents=True, exist_ok=True)
    target = directory / f"{args.session}.json"
    target.write_text(json.dumps({"schema_version": 1, "task": str(task.relative_to(root))}, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"bound": True, "session": args.session, "task": str(task.relative_to(root))}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

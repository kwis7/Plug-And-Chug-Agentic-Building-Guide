#!/usr/bin/env python3
"""Enforce portable instruction, memory, task, and contextual-file budgets."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


RULES = {
    "AGENTS.md": (24 * 1024, 400),
    "CLAUDE.md": (4 * 1024, 100),
    "GEMINI.md": (4 * 1024, 100),
    "MEMORY.md": (12 * 1024, 120),
    "task.yaml": (32 * 1024, 800),
}

CONTAINER_POLICIES = {
    "raw_data": "never-auto-load",
    "artifacts": "summary-only",
    "logs": "summary-only",
    "outputs": "named-only",
}
LARGE_FILE_BYTES = 256 * 1024


def load_storage_manifest(directory: Path) -> dict[str, object]:
    path = directory / "manifest.json"
    if not path.exists():
        return {}
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return value if isinstance(value, dict) else {}


def check(root: Path) -> dict[str, object]:
    violations = []
    checked = 0
    for path in root.glob("**/*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        name = "task.yaml" if path.name == "task.yaml" else path.name
        if name not in RULES:
            continue
        byte_limit, line_limit = RULES[name]
        checked += 1
        size = path.stat().st_size
        lines = len(path.read_text(encoding="utf-8", errors="replace").splitlines())
        if size > byte_limit or lines > line_limit:
            violations.append({"path": str(path.relative_to(root)), "bytes": size, "lines": lines, "limit_bytes": byte_limit, "limit_lines": line_limit})
    indexed_large_files = 0
    for directory_name, expected_policy in CONTAINER_POLICIES.items():
        for directory in root.glob(f"**/{directory_name}"):
            if not directory.is_dir() or ".git" in directory.parts:
                continue
            manifest = load_storage_manifest(directory)
            entries = manifest.get("entries") if isinstance(manifest.get("entries"), list) else []
            indexed = {
                str(item.get("path")): item
                for item in entries
                if isinstance(item, dict) and item.get("path")
            }
            for path in directory.rglob("*"):
                if not path.is_file() or path.name in {"README.md", "manifest.json"}:
                    continue
                if path.stat().st_size < LARGE_FILE_BYTES:
                    continue
                relative = str(path.relative_to(directory))
                entry = indexed.get(relative)
                if not entry:
                    violations.append({"path": str(path.relative_to(root)), "issue": "large file missing storage manifest entry", "threshold_bytes": LARGE_FILE_BYTES})
                    continue
                policy = str(entry.get("context_policy") or "")
                if policy != expected_policy:
                    violations.append({"path": str(path.relative_to(root)), "issue": "unsafe or incorrect context_policy", "expected": expected_policy, "actual": policy})
                    continue
                actual_size = path.stat().st_size
                if entry.get("size_bytes") != actual_size:
                    violations.append({"path": str(path.relative_to(root)), "issue": "storage manifest size_bytes is missing or stale", "actual_size_bytes": actual_size, "manifest_size_bytes": entry.get("size_bytes")})
                    continue
                if not str(entry.get("summary") or "").strip():
                    violations.append({"path": str(path.relative_to(root)), "issue": "storage manifest summary is required for large files"})
                    continue
                indexed_large_files += 1
    return {
        "root": str(root),
        "checked": checked,
        "indexed_large_files": indexed_large_files,
        "valid": not violations,
        "violations": violations,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    args = parser.parse_args(argv or sys.argv[1:])
    report = check(args.root.resolve())
    print(json.dumps(report, indent=2))
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

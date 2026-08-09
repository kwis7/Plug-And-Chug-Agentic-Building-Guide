#!/usr/bin/env python3
"""Translate the portable closeout gate into runtime-specific hook responses."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

from closeout_gate import gate
from pas_common import ACTIVE_STATUSES, TERMINAL_STATUSES, discover_task_manifests, load_manifest, within


TERMINAL_CLAIM_RE = re.compile(
    r"\b(?:completed|complete|done|finished|delivered|implemented)\b|(?:任务|工作|修改).{0,8}(?:完成|结束)|(?:已经|已)(?:完成|交付)",
    re.I,
)


def hook_message(payload: dict[str, object]) -> str:
    for key in ("last_assistant_message", "prompt_response"):
        value = payload.get(key)
        if isinstance(value, str):
            return value
    return ""


def resolve_task(root: Path, payload: dict[str, object]) -> tuple[Path | None, str | None]:
    explicit = os.environ.get("PAS_TASK")
    if explicit:
        path = Path(explicit)
        candidate = path if path.is_absolute() else root / path
        candidate = candidate.resolve()
        if not within(candidate, root) or candidate.name != "task.yaml":
            return None, "PAS_TASK must resolve to task.yaml inside the harness root"
        return candidate, None
    session_id = str(payload.get("session_id") or "")
    if session_id:
        if not re.fullmatch(r"[A-Za-z0-9._-]{1,200}", session_id):
            return None, "runtime session id contains unsupported path characters"
        binding = root / ".pas" / "runtime" / "sessions" / f"{session_id}.json"
        if binding.exists():
            try:
                relative = str(json.loads(binding.read_text(encoding="utf-8"))["task"])
                candidate = (root / relative).resolve()
                if not within(candidate, root) or candidate.name != "task.yaml":
                    return None, f"task binding escapes the harness root: {binding}"
                return candidate, None
            except (OSError, KeyError, json.JSONDecodeError):
                return None, f"invalid task binding: {binding}"
    active = []
    terminal = []
    for path in discover_task_manifests(root):
        try:
            status = str(load_manifest(path).get("status") or "").lower()
        except (OSError, ValueError):
            continue
        if status in ACTIVE_STATUSES:
            active.append(path)
        elif status in TERMINAL_STATUSES:
            terminal.append(path)
    if len(active) == 1:
        return active[0], None
    if len(active) > 1:
        return None, "multiple active tasks are available; bind this session to one task before claiming completion"
    if len(terminal) == 1:
        return terminal[0], None
    if not terminal:
        return None, "no task manifest available for closeout"
    return None, "multiple terminal tasks are available; bind this session to the task being reported"


def block(runtime: str, reason: str) -> dict[str, object]:
    if runtime == "gemini-cli":
        return {"decision": "deny", "reason": reason}
    return {"decision": "block", "reason": reason}


def evaluate(root: Path, runtime: str, payload: dict[str, object]) -> dict[str, object]:
    message = hook_message(payload)
    task_path, resolution_error = resolve_task(root, payload)
    if task_path is None:
        if TERMINAL_CLAIM_RE.search(message):
            return block(runtime, resolution_error or "cannot resolve active task")
        return {}
    try:
        task = load_manifest(task_path)
    except (OSError, ValueError) as exc:
        return block(runtime, f"cannot parse active task: {exc}")
    status = str(task.get("status") or "").lower()
    if status not in TERMINAL_STATUSES and not TERMINAL_CLAIM_RE.search(message):
        return {}
    report = gate(root, task_path)
    if report["passed"]:
        return {}
    details = "; ".join(str(item) for item in report["errors"])
    return block(runtime, f"Portable closeout gate failed for {task.get('id')}: {details}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--runtime", choices=["codex", "claude-code", "gemini-cli"], required=True)
    parser.add_argument("--root", type=Path, required=True)
    args = parser.parse_args(argv or sys.argv[1:])
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        payload = {}
    if not isinstance(payload, dict):
        payload = {}
    result = evaluate(args.root.resolve(), args.runtime, payload)
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Acquire, inspect, and release scoped, TTL-based resource locks."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

from pas_common import ACTIVE_STATUSES, find_task_by_id, load_manifest


def now() -> datetime:
    return datetime.now(timezone.utc)


def lock_path(root: Path, resource: str) -> Path:
    safe = "".join(char if char.isalnum() or char in "._-" else "-" for char in resource).strip("-")
    if not safe:
        raise ValueError("resource must contain a safe character")
    digest = hashlib.sha256(resource.encode("utf-8")).hexdigest()[:12]
    return root / ".pas" / "runtime" / "locks" / f"{safe[:80]}-{digest}.lock.json"


def read_lock(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def expired(lock: dict[str, object]) -> bool:
    return datetime.fromisoformat(str(lock["expires_at"])) <= now()


def acquire(root: Path, args: argparse.Namespace) -> int:
    try:
        task_path = find_task_by_id(root, args.task)
    except ValueError as exc:
        print(json.dumps({"acquired": False, "reason": str(exc)}, indent=2))
        return 1
    if task_path is None:
        print(json.dumps({"acquired": False, "reason": "task_not_found", "task_id": args.task}, indent=2))
        return 1
    task = load_manifest(task_path)
    status = str(task.get("status") or "").lower()
    if status not in ACTIVE_STATUSES:
        print(json.dumps({"acquired": False, "reason": "task_not_active", "status": status}, indent=2))
        return 1
    execution = task.get("execution") if isinstance(task.get("execution"), dict) else {}
    declared = [str(item) for item in execution.get("resources", [])]
    if args.resource not in declared:
        print(json.dumps({"acquired": False, "reason": "resource_not_declared_in_task", "resource": args.resource}, indent=2))
        return 1
    declared_writer = execution.get("writer")
    if declared_writer and args.writer != declared_writer:
        print(json.dumps({"acquired": False, "reason": "writer_mismatch", "declared": declared_writer}, indent=2))
        return 1
    declared_worktree = execution.get("worktree")
    if declared_worktree and args.worktree != declared_worktree:
        print(json.dumps({"acquired": False, "reason": "worktree_mismatch", "declared": declared_worktree}, indent=2))
        return 1
    path = lock_path(root, args.resource)
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        existing = read_lock(path)
        if not expired(existing):
            print(json.dumps({"acquired": False, "reason": "resource_locked", "lock": existing}, indent=2))
            return 1
        path.unlink()
    created = now()
    payload = {
        "schema_version": 1,
        "resource": args.resource,
        "mode": args.mode,
        "task_id": args.task,
        "session_id": args.session,
        "writer": args.writer,
        "worktree": args.worktree,
        "created_at": created.isoformat(),
        "heartbeat_at": created.isoformat(),
        "expires_at": (created + timedelta(minutes=args.ttl_minutes)).isoformat(),
    }
    try:
        descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    except FileExistsError:
        print(json.dumps({"acquired": False, "reason": "lock_race"}, indent=2))
        return 1
    with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
        json.dump(payload, stream, indent=2)
        stream.write("\n")
    print(json.dumps({"acquired": True, "path": str(path), "lock": payload}, indent=2))
    return 0


def release(root: Path, args: argparse.Namespace) -> int:
    path = lock_path(root, args.resource)
    if not path.exists():
        print(json.dumps({"released": False, "reason": "not_found"}, indent=2))
        return 1
    payload = read_lock(path)
    if payload.get("task_id") != args.task or payload.get("session_id") != args.session:
        print(json.dumps({"released": False, "reason": "owner_mismatch", "lock": payload}, indent=2))
        return 1
    path.unlink()
    print(json.dumps({"released": True, "resource": args.resource}, indent=2))
    return 0


def renew(root: Path, args: argparse.Namespace) -> int:
    path = lock_path(root, args.resource)
    if not path.exists():
        print(json.dumps({"renewed": False, "reason": "not_found"}, indent=2))
        return 1
    payload = read_lock(path)
    if payload.get("task_id") != args.task or payload.get("session_id") != args.session:
        print(json.dumps({"renewed": False, "reason": "owner_mismatch", "lock": payload}, indent=2))
        return 1
    timestamp = now()
    payload["heartbeat_at"] = timestamp.isoformat()
    payload["expires_at"] = (timestamp + timedelta(minutes=args.ttl_minutes)).isoformat()
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"renewed": True, "resource": args.resource, "expires_at": payload["expires_at"]}, indent=2))
    return 0


def inspect(root: Path) -> int:
    directory = root / ".pas" / "runtime" / "locks"
    locks = []
    for path in sorted(directory.glob("*.lock.json")) if directory.exists() else []:
        payload = read_lock(path)
        payload["expired"] = expired(payload)
        locks.append(payload)
    print(json.dumps({"locks": locks, "active": sum(not item["expired"] for item in locks)}, indent=2))
    return 0 if not any(item["expired"] for item in locks) else 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    sub = parser.add_subparsers(dest="command", required=True)
    acquire_parser = sub.add_parser("acquire")
    acquire_parser.add_argument("--resource", required=True)
    acquire_parser.add_argument("--task", required=True)
    acquire_parser.add_argument("--session", required=True)
    acquire_parser.add_argument("--writer", required=True)
    acquire_parser.add_argument("--mode", choices=["write", "read"], default="write")
    acquire_parser.add_argument("--worktree")
    acquire_parser.add_argument("--ttl-minutes", type=int, default=60)
    release_parser = sub.add_parser("release")
    release_parser.add_argument("--resource", required=True)
    release_parser.add_argument("--task", required=True)
    release_parser.add_argument("--session", required=True)
    renew_parser = sub.add_parser("renew")
    renew_parser.add_argument("--resource", required=True)
    renew_parser.add_argument("--task", required=True)
    renew_parser.add_argument("--session", required=True)
    renew_parser.add_argument("--ttl-minutes", type=int, default=60)
    sub.add_parser("check")
    args = parser.parse_args(argv or sys.argv[1:])
    root = args.root.resolve()
    if args.command == "acquire":
        return acquire(root, args)
    if args.command == "release":
        return release(root, args)
    if args.command == "renew":
        return renew(root, args)
    return inspect(root)


if __name__ == "__main__":
    raise SystemExit(main())

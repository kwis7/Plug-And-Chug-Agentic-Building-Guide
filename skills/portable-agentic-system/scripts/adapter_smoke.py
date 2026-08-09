#!/usr/bin/env python3
"""Run static adapter probes; never label them runtime verification."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def hook_command(config: dict[str, object], event: str) -> str:
    hooks = config.get("hooks") if isinstance(config.get("hooks"), dict) else {}
    matchers = hooks.get(event) if isinstance(hooks, dict) else None
    if not isinstance(matchers, list) or not matchers:
        return ""
    first = matchers[0] if isinstance(matchers[0], dict) else {}
    commands = first.get("hooks") if isinstance(first, dict) else None
    if not isinstance(commands, list) or not commands or not isinstance(commands[0], dict):
        return ""
    return str(commands[0].get("command") or "")


def load_json(path: Path) -> dict[str, object]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return value if isinstance(value, dict) else {}


def smoke(root: Path, runtime: str) -> dict[str, object]:
    checks: list[tuple[str, bool]] = []
    if runtime == "codex":
        text = (root / "AGENTS.md").read_text(encoding="utf-8")
        config = load_json(root / ".codex" / "hooks.json")
        command = hook_command(config, "Stop")
        checks = [("AGENTS.md exists", True), ("no @import", "@import" not in text), ("under 32 KiB runtime ceiling", len(text.encode()) <= 32 * 1024), ("Stop hook configured", "runtime_hook_gate.py" in command and "--runtime codex" in command)]
    elif runtime == "claude-code":
        text = (root / "CLAUDE.md").read_text(encoding="utf-8")
        config = load_json(root / ".claude" / "settings.json")
        command = hook_command(config, "Stop")
        checks = [("CLAUDE.md bridges AGENTS.md", text.lstrip().startswith("@AGENTS.md")), ("small delta", len(text.encode()) <= 4 * 1024), ("Stop hook configured", "runtime_hook_gate.py" in command and "--runtime claude-code" in command)]
    elif runtime == "gemini-cli":
        text = (root / "GEMINI.md").read_text(encoding="utf-8")
        config = load_json(root / ".gemini" / "settings.json")
        command = hook_command(config, "AfterAgent")
        checks = [("GEMINI.md imports AGENTS.md", text.lstrip().startswith("@./AGENTS.md")), ("small delta", len(text.encode()) <= 4 * 1024), ("AfterAgent hook configured", "runtime_hook_gate.py" in command and "--runtime gemini-cli" in command)]
    else:
        checks = [("runtime classified in compatibility manifest", runtime in (root / "runtime-compatibility.json").read_text(encoding="utf-8"))]
    wrapper = root / ".pas" / "bin" / "runtime_hook_gate.py"
    checks.append(("runtime hook translator exists", wrapper.exists()))
    return {"runtime": runtime, "verification_level": "static", "passed": all(value for _, value in checks), "checks": [{"name": name, "passed": value} for name, value in checks], "claim_limit": "configuration inspected; fresh-session loading and block/retry behavior not exercised"}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("--runtime", required=True)
    args = parser.parse_args(argv or sys.argv[1:])
    report = smoke(args.root.resolve(), args.runtime)
    print(json.dumps(report, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

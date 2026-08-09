#!/usr/bin/env python3
"""Check skill descriptions for trigger quality and near-duplicate collisions."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


STOP = {"the", "and", "for", "with", "when", "use", "this", "that", "from", "into", "your", "agent", "skill"}
TRIGGER_RE = re.compile(r"\b(?:use|run|choose)\b.{0,30}\bwhen\b|(?:适用于|当.+时|用于)", re.I)
BOUNDARY_RE = re.compile(r"\b(?:do not use|not for|exclude)\b|(?:不适用于|不要用于|排除)", re.I)


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    values = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip().strip('"')
    return values


def tokens(text: str) -> set[str]:
    return {word for word in re.findall(r"[a-z0-9-]+", text.lower()) if len(word) > 2 and word not in STOP}


def check(root: Path) -> dict[str, object]:
    entries = []
    issues = []
    for path in sorted(root.glob("**/SKILL.md")):
        relative_parts = path.relative_to(root).parts
        if any(part.startswith(".") for part in relative_parts) or "templates" in relative_parts:
            continue
        meta = frontmatter(path)
        name = meta.get("name", "")
        description = meta.get("description", "")
        entries.append((path, name, description, tokens(description)))
        if not name or not description:
            issues.append({"path": str(path), "issue": "missing name or description"})
            continue
        if len(description) < 80:
            issues.append({"path": str(path), "issue": "description shorter than 80 characters"})
        lowered = description.lower()
        if not TRIGGER_RE.search(description):
            issues.append({"path": str(path), "issue": "description lacks explicit use/when trigger language"})
        if not BOUNDARY_RE.search(description):
            issues.append({"path": str(path), "issue": "description lacks a negative boundary"})
    collisions = []
    for index, first in enumerate(entries):
        for second in entries[index + 1 :]:
            union = first[3] | second[3]
            score = len(first[3] & second[3]) / len(union) if union else 0
            if score >= 0.65:
                collisions.append({"first": first[1], "second": second[1], "score": round(score, 3)})
    routing_path = root / "routing-evals.json"
    routing_agents = 0
    if routing_path.exists():
        try:
            routing = json.loads(routing_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            issues.append({"path": str(routing_path), "issue": f"invalid routing eval JSON: {exc}"})
            routing = {}
        suites = routing.get("suites") if isinstance(routing, dict) else None
        if not isinstance(suites, list) or not suites:
            issues.append({"path": str(routing_path), "issue": "routing suites are missing"})
        else:
            seen_prompts: dict[str, str] = {}
            for suite in suites:
                if not isinstance(suite, dict):
                    issues.append({"path": str(routing_path), "issue": "routing suite is not an object"})
                    continue
                routing_agents += 1
                agent = str(suite.get("agent") or "")
                description = str(suite.get("description") or "")
                exclusions = suite.get("exclusions")
                positive = suite.get("positive")
                negative = suite.get("negative")
                if not agent:
                    issues.append({"path": str(routing_path), "issue": "routing suite missing agent"})
                if len(description) < 80:
                    issues.append({"agent": agent, "issue": "routing description shorter than 80 characters"})
                if not isinstance(exclusions, list) or not exclusions:
                    issues.append({"agent": agent, "issue": "routing exclusions are missing"})
                if not isinstance(positive, list) or len(positive) < 2:
                    issues.append({"agent": agent, "issue": "fewer than two positive routing examples"})
                if not isinstance(negative, list) or len(negative) < 2:
                    issues.append({"agent": agent, "issue": "fewer than two negative routing examples"})
                for example in positive if isinstance(positive, list) else []:
                    prompt = str(example.get("prompt") or "").strip() if isinstance(example, dict) else ""
                    normalized = re.sub(r"\s+", " ", prompt.lower())
                    if not normalized:
                        issues.append({"agent": agent, "issue": "empty positive routing prompt"})
                    elif normalized in seen_prompts and seen_prompts[normalized] != agent:
                        collisions.append({"first": seen_prompts[normalized], "second": agent, "prompt": prompt})
                    else:
                        seen_prompts[normalized] = agent
    return {"root": str(root), "skills": len(entries), "routing_agents": routing_agents, "valid": not issues and not collisions, "issues": issues, "collisions": collisions}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    args = parser.parse_args(argv or sys.argv[1:])
    report = check(args.root.resolve())
    print(json.dumps(report, indent=2))
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

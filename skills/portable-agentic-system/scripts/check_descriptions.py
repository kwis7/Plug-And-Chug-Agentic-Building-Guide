#!/usr/bin/env python3
"""Check portable Skill metadata and description routing without dependencies.

Accept PAS's conservative YAML maps/scalars plus quoted and block strings.
Unsupported YAML constructs produce diagnostics instead of guessed metadata.
This is not a general-purpose YAML parser or a behavioral routing evaluation.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


STOP = {"the", "and", "for", "with", "when", "use", "this", "that", "from", "into", "your", "agent", "skill"}
TRIGGER_RE = re.compile(r"\b(?:use|run|choose)\b.{0,30}\bwhen\b|(?:适用于|当.+时|用于)", re.I)
BOUNDARY_RE = re.compile(r"\b(?:do not use|not for|exclude)\b|(?:不适用于|不要用于|排除)", re.I)


def scalar_value(value: str) -> str | None:
    """Read the documented scalar subset without coercing YAML types to text."""
    if value.startswith('"'):
        try:
            decoded, end = json.JSONDecoder().raw_decode(value)
        except ValueError as exc:
            raise ValueError("unsupported double-quoted scalar; use JSON-compatible escapes") from exc
        if not isinstance(decoded, str) or (value[end:].strip() and not re.fullmatch(r"\s+#.*", value[end:])):
            raise ValueError("invalid quoted scalar")
        return decoded
    if value.startswith("'"):
        match = re.fullmatch(r"'((?:[^']|'')*)'(?:\s+#.*)?\s*", value)
        if not match:
            raise ValueError("invalid single-quoted scalar")
        return match[1].replace("''", "'")
    value = re.split(r"\s+#", value, maxsplit=1)[0].rstrip()
    if value.startswith("#"):
        return None
    if value.startswith(("&", "*", "!", "{", "[", "]", "}", "|", ">", "@", "`", "%")) or re.match(r"[-?:](?:\s|$)", value):
        raise ValueError("unsupported YAML construct; use a quoted scalar or indented map")
    if re.search(r":(?:\s|$)", value):
        raise ValueError("plain scalar contains a mapping separator; quote the value")
    numeric = r"[-+]?(?:0[xX][0-9a-fA-F_]+|0[oO][0-7_]+|0[bB][01_]+|(?:[0-9][0-9_]*(?:\.[0-9_]*)?|\.[0-9_]+)(?:[eE][-+]?[0-9]+)?|\.inf|\.nan)"
    if value.lower() in {"true", "false", "null", "~"} or re.fullmatch(numeric, value, re.I):
        return None
    return value or None


def block_value(raw: list[str], style: str, chomp: str, key: str) -> str:
    """Support implicit indentation, literal/folded strings and YAML chomping."""
    nonempty = [row for row in raw if row.strip()]
    if not nonempty:
        return "\n" * len(raw) if chomp == "+" else ""
    indent = len(nonempty[0]) - len(nonempty[0].lstrip(" "))
    if any(len(row) - len(row.lstrip(" ")) < indent for row in nonempty):
        raise ValueError(f"inconsistent block indentation for {key}")
    first = next(index for index, row in enumerate(raw) if row.strip())
    if any(len(row) > indent for row in raw[:first]):
        raise ValueError(f"leading blank line exceeds block indentation for {key}")
    rows = [row[indent:] if len(row) >= indent else "" for row in raw]
    if style == "|":
        content = "\n".join(rows) + "\n"
    else:
        positions = [index for index, row in enumerate(rows) if row]
        content = "\n" * positions[0] + rows[positions[0]]
        for previous, current in zip(positions, positions[1:]):
            gap = current - previous - 1
            indented = rows[previous].startswith((" ", "\t")) or rows[current].startswith((" ", "\t"))
            separator = "\n" * (gap + int(indented)) if gap else ("\n" if indented else " ")
            content += separator + rows[current]
        content += "\n" * (len(rows) - positions[-1])
    if chomp == "-":
        return content.rstrip("\n")
    return content if chomp == "+" else content.rstrip("\n") + "\n"


def frontmatter(path: Path) -> dict[str, object]:
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("missing YAML frontmatter opening delimiter")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError("missing YAML frontmatter closing delimiter") from exc
    root: dict[str, object] = {}
    stack: list[tuple[int, dict[str, object]]] = [(0, root)]
    pending: tuple[int, dict[str, object], str] | None = None
    index = 1
    while index < end:
        line = lines[index]
        index += 1
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match = re.fullmatch(r"( *)([A-Za-z0-9_-]+):(?: +(.*)| *)", line)
        if not match:
            raise ValueError(f"unsupported YAML on line {index}; use indented maps and scalar values")
        prefix, key, value = match[1], match[2], match[3] or ""
        indent = len(prefix)
        if indent > stack[-1][0]:
            if pending is None or pending[0] != stack[-1][0]:
                raise ValueError(f"unexpected indentation on line {index}")
            child: dict[str, object] = {}
            pending[1][pending[2]] = child
            stack.append((indent, child))
        while indent < stack[-1][0]:
            stack.pop()
        if indent != stack[-1][0]:
            raise ValueError(f"inconsistent mapping indentation on line {index}")
        parent = stack[-1][1]
        if key in parent:
            raise ValueError(f"duplicate frontmatter key: {key}")
        pending = None
        block = re.fullmatch(r"([>|])([-+]?)(?: +#.*)?", value)
        if block:
            raw = []
            while index < end and (not lines[index].strip() or len(lines[index]) - len(lines[index].lstrip(" ")) > indent):
                raw.append(lines[index])
                index += 1
            parent[key] = block_value(raw, block[1], block[2], key)
        elif not value or value.startswith("#"):
            parent[key] = None
            pending = (indent, parent, key)
        else:
            parent[key] = scalar_value(value)
    return root


def tokens(text: str) -> set[str]:
    return {word for word in re.findall(r"[a-z0-9-]+", text.lower()) if len(word) > 2 and word not in STOP}


def check(root: Path) -> dict[str, object]:
    entries = []
    issues = []
    warnings = []
    for path in sorted(root.glob("**/SKILL.md")):
        relative_parts = path.relative_to(root).parts
        if any(part.startswith(".") for part in relative_parts) or "templates" in relative_parts:
            continue
        try:
            meta = frontmatter(path)
        except (OSError, ValueError) as exc:
            issues.append({"path": str(path), "issue": str(exc)})
            continue
        name = meta.get("name", "")
        description = meta.get("description", "")
        if not isinstance(name, str) or not name or not isinstance(description, str) or not description.strip():
            issues.append({"path": str(path), "issue": "name and description must be non-empty strings"})
            continue
        entries.append((path, name, description, tokens(description)))
        if len(name) > 64 or name != name.lower() or any(not (char.isalnum() or char == "-") for char in name) or name.startswith("-") or name.endswith("-") or "--" in name:
            issues.append({"path": str(path), "issue": "name must use 1-64 lowercase alphanumeric characters and single hyphens"})
        if name != path.parent.name:
            issues.append({"path": str(path), "issue": "name must match its parent directory"})
        if len(description) > 1024:
            issues.append({"path": str(path), "issue": "description exceeds 1024 characters"})
        compatibility = meta.get("compatibility")
        if "compatibility" in meta and (not isinstance(compatibility, str) or not 1 <= len(compatibility) <= 500):
            issues.append({"path": str(path), "issue": "compatibility must be a string of 1-500 characters"})
        metadata = meta.get("metadata")
        if "metadata" in meta and (not isinstance(metadata, dict) or any(not isinstance(item, str) for item in metadata.values())):
            issues.append({"path": str(path), "issue": "metadata must be a map of strings"})
        if len(description) < 80:
            warnings.append({"path": str(path), "issue": "short description: review its scope using routing examples"})
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
    return {"root": str(root), "skills": len(entries), "routing_agents": routing_agents, "valid": not issues and not collisions, "issues": issues, "warnings": warnings, "collisions": collisions, "evidence": "static metadata and routing fixtures; runtime behavior not tested"}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    args = parser.parse_args(argv or sys.argv[1:])
    report = check(args.root.resolve())
    print(json.dumps(report, indent=2))
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

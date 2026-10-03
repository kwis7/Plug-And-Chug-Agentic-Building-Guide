#!/usr/bin/env python3
"""Read-only checks for optional preference, model-combination and evidence records.

Reads only explicitly supplied JSON files. Does not follow paths/URLs in records,
activate preferences, contact providers, or prove that a runtime loaded a file.
"""
from __future__ import annotations

import argparse
from datetime import date
import json
import math
from pathlib import Path

COMMON_CHECKS = {"instruction_loading", "tool_round_trip", "uncertainty", "recovery"}


class Audit:
    def __init__(self):
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, path, message):
        self.errors.append(f"{path}: {message}")

    def obj(self, value, path):
        if not isinstance(value, dict):
            self.error(path, "expected an object")
            return {}
        return value

    def string(self, value, path, nullable=False):
        if nullable and value is None:
            return
        if not isinstance(value, str) or not value.strip():
            self.error(path, "expected a nonempty string")

    def integer(self, value, path, minimum=1, nullable=False):
        if nullable and value is None:
            return
        if type(value) is not int or value < minimum:
            self.error(path, f"expected an integer >= {minimum}")

    def number(self, value, path):
        if value is None:
            return
        if type(value) not in (int, float) or (type(value) is float and not math.isfinite(value)) or value < 0:
            self.error(path, "expected a finite nonnegative number or null")

    def choice(self, value, path, choices):
        if not isinstance(value, str) or value not in choices:
            self.error(path, "unsupported or missing value")

    def strings(self, value, path, nonempty=False):
        if not isinstance(value, list):
            self.error(path, "expected a list of strings")
            return []
        if nonempty and not value:
            self.error(path, "list must not be empty")
        for i, item in enumerate(value):
            self.string(item, f"{path}[{i}]")
        if all(isinstance(item, str) for item in value) and len(set(value)) != len(value):
            self.error(path, "duplicate entries")
        return value

    def day(self, value, path, nullable=False):
        if nullable and value is None:
            return
        try:
            if not isinstance(value, str) or date.fromisoformat(value).isoformat() != value:
                raise ValueError
        except ValueError:
            self.error(path, "expected YYYY-MM-DD")

    def older(self, value, version, path):
        self.integer(value, path, nullable=True)
        if type(value) is int and type(version) is int and value >= version:
            self.error(path, "must precede the current version")

    def preference(self, record, path):
        version = record.get("version")
        self.integer(version, path + ".version")
        self.choice(record.get("state"), path + ".state", {"proposed", "trial", "active", "retired"})
        scope = self.obj(record.get("scope"), path + ".scope")
        includes = self.strings(scope.get("include_task_types"), path + ".scope.include_task_types", True)
        excludes = self.strings(scope.get("exclude_task_types"), path + ".scope.exclude_task_types")
        if all(isinstance(x, str) for x in includes + excludes) and set(includes) & set(excludes):
            self.error(path + ".scope", "same task type included and excluded")
        self.string(record.get("behavior"), path + ".behavior")
        source = self.obj(record.get("source"), path + ".source")
        self.choice(source.get("kind"), path + ".source.kind", {"explicit_future_instruction", "repeated_correction", "one_off"})
        self.string(source.get("reference"), path + ".source.reference")
        self.day(source.get("recorded_at"), path + ".source.recorded_at")
        if type(record.get("retention_authorized")) is not bool:
            self.error(path + ".retention_authorized", "expected a boolean")
        self.choice(record.get("conflict_review"), path + ".conflict_review", {"pending", "passed", "conflict"})
        self.older(record.get("supersedes_version"), version, path + ".supersedes_version")
        self.string(record.get("retirement_reason"), path + ".retirement_reason", True)
        evidence = self.obj(record.get("evidence"), path + ".evidence")
        self.choice(evidence.get("mode"), path + ".evidence.mode", {"illustrative", "observed"})
        self.strings(evidence.get("receipt_refs"), path + ".evidence.receipt_refs", evidence.get("mode") == "observed")
        rollback = self.obj(record.get("rollback"), path + ".rollback")
        self.older(rollback.get("restore_version"), version, path + ".rollback.restore_version")
        self.string(rollback.get("reason"), path + ".rollback.reason", True)
        if rollback.get("restore_version") is not None and not rollback.get("reason"):
            self.error(path + ".rollback.reason", "restore requires a reason")
        if record.get("state") == "active":
            if record.get("retention_authorized") is not True:
                self.error(path + ".state", "active preference requires retention authorization")
            if source.get("kind") == "one_off":
                self.error(path + ".state", "one-off instruction cannot become an active preference")
            if record.get("conflict_review") != "passed":
                self.error(path + ".state", "active preference requires passed conflict review")
        if record.get("state") == "retired" and not record.get("retirement_reason"):
            self.error(path + ".retirement_reason", "retirement requires a reason")

    def combination(self, record, path):
        for field, keys in (("client", ("name", "version")), ("runtime", ("name", "version")),
                            ("provider", ("name", "endpoint_type", "region"))):
            obj = self.obj(record.get(field), path + "." + field)
            for key in keys:
                self.string(obj.get(key), f"{path}.{field}.{key}")
        model = self.obj(record.get("model"), path + ".model")
        self.string(model.get("requested_id"), path + ".model.requested_id")
        self.string(model.get("resolved_id"), path + ".model.resolved_id", True)
        self.day(model.get("verification_date"), path + ".model.verification_date", True)
        overlay = self.obj(record.get("overlay"), path + ".overlay")
        self.string(overlay.get("id"), path + ".overlay.id")
        self.integer(overlay.get("version"), path + ".overlay.version")
        evidence = self.obj(record.get("evidence"), path + ".evidence")
        self.choice(evidence.get("mode"), path + ".evidence.mode", {"illustrative", "observed"})
        capabilities = self.obj(record.get("capabilities"), path + ".capabilities")
        required = self.strings(capabilities.get("required"), path + ".capabilities.required")
        observations = self.obj(capabilities.get("observations"), path + ".capabilities.observations")
        for capability, observation in observations.items():
            self.string(capability, path + ".capabilities.key")
            obj = self.obj(observation, path + ".capabilities.observation")
            self.choice(obj.get("status"), path + ".capabilities.status", {"documented", "observed", "unknown", "unsupported"})
            self.string(obj.get("source_ref"), path + ".capabilities.source_ref", True)
            if obj.get("status") in ("documented", "observed") and not obj.get("source_ref"):
                self.error(path + ".capabilities.source_ref", "documented/observed claim requires a reference")
        for capability in required:
            if isinstance(capability, str) and capability not in observations:
                self.error(path + ".capabilities.required", "required capability lacks an observation entry")
        context = self.obj(record.get("context"), path + ".context")
        self.integer(context.get("documented_limit_tokens"), path + ".context.documented_limit_tokens", nullable=True)
        self.string(context.get("observed_compaction"), path + ".context.observed_compaction", True)
        parameters = self.obj(record.get("parameters"), path + ".parameters")
        groups = [self.strings(parameters.get(key), path + ".parameters." + key) for key in ("supported", "ignored", "unsupported")]
        if all(isinstance(x, str) for group in groups for x in group):
            if len(set(x for group in groups for x in group)) != sum(map(len, groups)):
                self.error(path + ".parameters", "parameter belongs to conflicting groups")
        acceptance = self.obj(record.get("acceptance"), path + ".acceptance")
        self.choice(acceptance.get("status"), path + ".acceptance.status", {"not_run", "partial", "passed", "failed"})
        self.strings(acceptance.get("receipt_refs"), path + ".acceptance.receipt_refs")
        self.string(record.get("fallback_combination_id"), path + ".fallback_combination_id", True)
        rollback = self.obj(record.get("rollback"), path + ".rollback")
        self.string(rollback.get("previous_combination_id"), path + ".rollback.previous_combination_id", True)
        self.string(rollback.get("trigger"), path + ".rollback.trigger")
        if acceptance.get("status") == "passed":
            if evidence.get("mode") != "observed" or not acceptance.get("receipt_refs"):
                self.error(path + ".acceptance", "passed requires observed evidence and receipts")
            if model.get("verification_date") is None:
                self.error(path + ".model.verification_date", "passed combination requires a verification date")
            for capability in required:
                observation = observations.get(capability) if isinstance(capability, str) else None
                if not isinstance(observation, dict) or observation.get("status") != "observed":
                    self.error(path + ".capabilities.required", "passed combination requires observed required capabilities")

    def receipt(self, record, path):
        self.choice(record.get("mode"), path + ".mode", {"illustrative", "observed"})
        self.day(record.get("recorded_at"), path + ".recorded_at")
        self.string(record.get("fixture_id"), path + ".fixture_id")
        self.string(record.get("combination_id"), path + ".combination_id")
        preference = record.get("preference")
        if preference is not None:
            obj = self.obj(preference, path + ".preference")
            self.string(obj.get("id"), path + ".preference.id")
            self.integer(obj.get("version"), path + ".preference.version")
        checks = record.get("checks")
        if not isinstance(checks, list) or not checks:
            self.error(path + ".checks", "expected a nonempty list")
            checks = []
        names = []
        for i, check in enumerate(checks):
            field = f"{path}.checks[{i}]"
            obj = self.obj(check, field)
            self.string(obj.get("id"), field + ".id")
            self.choice(obj.get("status"), field + ".status", {"pass", "fail", "not_run", "not_applicable"})
            self.string(obj.get("evidence_ref"), field + ".evidence_ref", True)
            if record.get("mode") == "observed" and obj.get("status") in ("pass", "fail") and not obj.get("evidence_ref"):
                self.error(field + ".evidence_ref", "observed result requires a reference")
            if isinstance(obj.get("id"), str):
                names.append(obj["id"])
        if len(set(names)) != len(names):
            self.error(path + ".checks", "duplicate check IDs")
        metrics = self.obj(record.get("metrics"), path + ".metrics")
        for key in ("latency_ms", "estimated_cost"):
            self.number(metrics.get(key), path + ".metrics." + key)
        for key in ("input_tokens", "output_tokens"):
            self.integer(metrics.get(key), path + ".metrics." + key, 0, True)
        self.day(metrics.get("pricing_date"), path + ".metrics.pricing_date", True)
        if metrics.get("estimated_cost") is not None and metrics.get("pricing_date") is None:
            self.error(path + ".metrics.pricing_date", "estimated cost requires a pricing date")
        self.strings(record.get("limitations"), path + ".limitations", True)


def validate_records(records):
    """Validate supplied objects and their declared cross-record claims, without I/O."""
    audit = Audit()
    by_id = {}
    for i, value in enumerate(records):
        path = f"records[{i}]"
        record = audit.obj(value, path)
        if type(record.get("schema_version")) is not int or record.get("schema_version") != 1:
            audit.error(path + ".schema_version", "expected version 1")
        audit.string(record.get("id"), path + ".id")
        identifier = record.get("id")
        if isinstance(identifier, str):
            if identifier in by_id:
                audit.error(path + ".id", "duplicate record ID; supply one current version per ID")
            else:
                by_id[identifier] = record
        kind = record.get("kind")
        if kind in ("preference", "model_combination"):
            audit.string(record.get("owner"), path + ".owner")
        if kind == "preference":
            audit.preference(record, path)
        elif kind == "model_combination":
            audit.combination(record, path)
        elif kind == "evaluation_receipt":
            audit.receipt(record, path)
        else:
            audit.error(path + ".kind", "unsupported record type")
    for i, record in enumerate(records):
        if not isinstance(record, dict):
            continue
        path = f"records[{i}]"
        kind = record.get("kind")
        section = record.get("acceptance" if kind == "model_combination" else "evidence", {})
        refs = section.get("receipt_refs", []) if isinstance(section, dict) else []
        passed_checks = set()
        for ref in refs if isinstance(refs, list) else []:
            receipt = by_id.get(ref) if isinstance(ref, str) else None
            if receipt is None:
                strict = (kind == "model_combination" and section.get("status") == "passed") or (kind == "preference" and section.get("mode") == "observed")
                target = audit.errors if strict else audit.warnings
                target.append(path + ".receipt_refs: referenced receipt not supplied")
                continue
            if receipt.get("kind") != "evaluation_receipt":
                audit.error(path + ".receipt_refs", "reference must identify an evaluation receipt")
                continue
            if kind == "preference":
                pref = receipt.get("preference")
                if not isinstance(pref, dict) or pref.get("id") != record.get("id") or pref.get("version") != record.get("version"):
                    audit.error(path + ".receipt_refs", "receipt identifies a different preference/version")
                if section.get("mode") == "observed" and receipt.get("mode") != "observed":
                    audit.error(path + ".evidence", "illustration cannot support an observed claim")
            elif kind == "model_combination":
                if receipt.get("combination_id") != record.get("id"):
                    audit.error(path + ".receipt_refs", "receipt identifies a different combination")
                if section.get("status") == "passed":
                    if receipt.get("mode") != "observed":
                        audit.error(path + ".acceptance", "illustration cannot support passed acceptance")
                    checks = receipt.get("checks", [])
                    for check in checks if isinstance(checks, list) else []:
                        if isinstance(check, dict) and check.get("status") == "fail":
                            audit.error(path + ".acceptance", "referenced receipt contains a failed check")
                        if isinstance(check, dict) and check.get("status") == "pass" and isinstance(check.get("id"), str):
                            passed_checks.add(check["id"])
        if kind == "model_combination" and isinstance(section, dict) and section.get("status") == "passed":
            capabilities = record.get("capabilities", {})
            required = capabilities.get("required", []) if isinstance(capabilities, dict) else []
            required = {x for x in required if isinstance(x, str)} if isinstance(required, list) else set()
            if not (COMMON_CHECKS | required).issubset(passed_checks):
                audit.error(path + ".acceptance", "mandatory checks missing or not passed")
    return audit.errors, audit.warnings


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", type=Path, help="Explicit public-safe JSON records or bundles")
    args = parser.parse_args(argv)
    records = []
    for path in args.files:
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, ValueError):
            parser.exit(1, f"Cannot read valid UTF-8 JSON: {path}\n")
        if isinstance(value, dict) and "records" in value:
            if type(value.get("schema_version")) is not int or value.get("schema_version") != 1 or not isinstance(value["records"], list) or not value["records"]:
                parser.exit(1, f"Invalid version-1 record bundle: {path}\n")
            records.extend(value["records"])
        else:
            records.append(value)
    errors, warnings = validate_records(records)
    for message in warnings:
        print("WARNING " + message)
    for message in errors:
        print("ERROR " + message)
    if errors:
        return 1
    print(f"Static records valid: {len(records)}. Runtime loading, evidence authenticity and authorization remain separate checks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

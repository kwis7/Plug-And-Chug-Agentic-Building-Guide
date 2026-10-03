"""Regression checks for evidence overclaims and unsafe preference promotion."""
from copy import deepcopy
import contextlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import check_workspace_records as records


def preference():
    return {
        "schema_version": 1, "kind": "preference", "id": "comparison-format", "owner": "example-owner",
        "version": 2, "state": "active", "scope": {"include_task_types": ["comparison"], "exclude_task_types": ["exploration"]},
        "behavior": "Recommendation, then evidence and unknowns.",
        "source": {"kind": "explicit_future_instruction", "reference": "synthetic-feedback-02", "recorded_at": "2026-10-02"},
        "retention_authorized": True, "conflict_review": "passed", "supersedes_version": 1,
        "retirement_reason": None, "evidence": {"mode": "illustrative", "receipt_refs": []},
        "rollback": {"restore_version": None, "reason": None},
    }


def combination():
    return {
        "schema_version": 1, "kind": "model_combination", "id": "candidate", "owner": "example-owner",
        "evidence": {"mode": "observed"}, "client": {"name": "test-client", "version": "1"},
        "runtime": {"name": "test-runtime", "version": "1"},
        "provider": {"name": "test-provider", "endpoint_type": "test-wire", "region": "test-region"},
        "model": {"requested_id": "test-model", "resolved_id": None, "verification_date": "2026-10-02"},
        "overlay": {"id": "minimal", "version": 1},
        "capabilities": {"required": ["tool_round_trip"], "observations": {"tool_round_trip": {"status": "observed", "source_ref": "synthetic-receipt"}}},
        "context": {"documented_limit_tokens": None, "observed_compaction": None},
        "parameters": {"supported": [], "ignored": [], "unsupported": []},
        "acceptance": {"status": "passed", "receipt_refs": ["synthetic-receipt"]},
        "fallback_combination_id": None, "rollback": {"previous_combination_id": None, "trigger": "Required check fails."},
    }


def receipt():
    # Authored testing fixture, not a live runtime receipt.
    return {
        "schema_version": 1, "kind": "evaluation_receipt", "id": "synthetic-receipt", "mode": "observed",
        "recorded_at": "2026-10-02", "fixture_id": "synthetic-comparison-v1",
        "preference": {"id": "comparison-format", "version": 2}, "combination_id": "candidate",
        "checks": [{"id": key, "status": "pass", "evidence_ref": "synthetic-result"} for key in sorted(records.COMMON_CHECKS)],
        "metrics": {"latency_ms": None, "input_tokens": None, "output_tokens": None, "estimated_cost": None, "pricing_date": None},
        "limitations": ["Synthetic unit-test data; validator does not authenticate evidence."],
    }


class WorkspaceRecordTests(unittest.TestCase):
    def test_declared_observed_bundle_is_consistent_not_authenticated(self):
        self.assertEqual(records.validate_records([preference(), combination(), receipt()]), ([], []))

    def test_permission_and_conflict_checks_before_preference_activation(self):
        for key, value in (("retention_authorized", False), ("conflict_review", "conflict")):
            record = preference()
            record[key] = value
            with self.subTest(key=key):
                self.assertTrue(records.validate_records([record])[0])
        record = preference()
        record["source"]["kind"] = "one_off"
        self.assertTrue(records.validate_records([record])[0])

    def test_rollback_and_retirement_are_explained_and_versioned(self):
        record = preference()
        record["state"] = "retired"
        self.assertTrue(records.validate_records([record])[0])
        record["retirement_reason"] = "User withdrew the preference."
        record["rollback"] = {"restore_version": 2, "reason": "Restore earlier behavior."}
        self.assertTrue(records.validate_records([record])[0])
        record["rollback"]["restore_version"] = 1
        self.assertFalse(records.validate_records([record])[0])

    def test_receipt_must_identify_adopted_preference_version(self):
        record = preference()
        record["evidence"]["receipt_refs"] = ["synthetic-receipt"]
        evidence = receipt()
        evidence["preference"]["version"] = 1
        self.assertTrue(records.validate_records([record, evidence])[0])

    def test_observed_preference_requires_supplied_observed_receipt(self):
        record = preference()
        record["evidence"]["mode"] = "observed"
        self.assertTrue(records.validate_records([record])[0])
        record["evidence"]["receipt_refs"] = ["synthetic-receipt"]
        self.assertTrue(records.validate_records([record])[0])
        evidence = receipt()
        evidence["mode"] = "illustrative"
        self.assertTrue(records.validate_records([record, evidence])[0])
        evidence["mode"] = "observed"
        self.assertFalse(records.validate_records([record, evidence])[0])

    def test_illustrative_results_do_not_pass_model_acceptance(self):
        record, evidence = combination(), receipt()
        evidence["mode"] = "illustrative"
        self.assertTrue(records.validate_records([record, evidence])[0])
        evidence["mode"] = "observed"
        record["evidence"]["mode"] = "illustrative"
        self.assertTrue(records.validate_records([record, evidence])[0])

    def test_missing_failed_and_unrun_checks_prevent_acceptance(self):
        for status in ("fail", "not_run", "not_applicable"):
            evidence = receipt()
            evidence["checks"][0]["status"] = status
            with self.subTest(status=status):
                self.assertTrue(records.validate_records([combination(), evidence])[0])
        self.assertTrue(records.validate_records([combination()])[0])

    def test_documentation_does_not_substitute_for_observed_capability(self):
        record = combination()
        record["capabilities"]["observations"]["tool_round_trip"]["status"] = "documented"
        self.assertTrue(records.validate_records([record, receipt()])[0])

    def test_receipt_for_another_combination_cannot_satisfy_acceptance(self):
        evidence = receipt()
        evidence["combination_id"] = "different-candidate"
        self.assertTrue(records.validate_records([combination(), evidence])[0])

    def test_observed_checks_need_evidence_and_metrics_are_finite(self):
        for value in (True, -1, float("nan"), float("inf")):
            evidence = receipt()
            evidence["metrics"]["latency_ms"] = value
            with self.subTest(value=value):
                self.assertTrue(records.validate_records([evidence])[0])
        evidence = receipt()
        evidence["checks"][0]["evidence_ref"] = None
        self.assertTrue(records.validate_records([evidence])[0])

    def test_unknown_pending_combination_and_unresolved_optional_refs(self):
        record = combination()
        record["evidence"]["mode"] = "illustrative"
        record["acceptance"] = {"status": "not_run", "receipt_refs": ["not-supplied"]}
        record["model"]["verification_date"] = None
        record["capabilities"]["observations"]["tool_round_trip"] = {"status": "unknown", "source_ref": None}
        errors, warnings = records.validate_records([record])
        self.assertFalse(errors)
        self.assertTrue(warnings)

    def test_duplicate_record_and_check_ids_are_rejected(self):
        self.assertTrue(records.validate_records([preference(), deepcopy(preference())])[0])
        evidence = receipt()
        evidence["checks"].append(deepcopy(evidence["checks"][0]))
        self.assertTrue(records.validate_records([evidence])[0])

    def test_malformed_field_types_fail_without_traceback(self):
        for field in ("kind", "schema_version", "id", "state", "scope", "source", "evidence", "rollback"):
            record = preference()
            record[field] = ["unexpected"]
            with self.subTest(field=field):
                self.assertTrue(records.validate_records([record])[0])
        evidence = receipt()
        evidence["checks"][0]["status"] = {}
        self.assertTrue(records.validate_records([evidence])[0])

    def test_cli_reads_only_explicit_files_and_never_mutates_them(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "records.json"
            record = preference()
            record["source"]["reference"] = "https://invalid.example/never-follow"
            record["evidence"]["receipt_refs"] = ["../../do-not-open"]
            original = json.dumps({"schema_version": 1, "records": [record]}).encode()
            path.write_bytes(original)
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(records.main([str(path)]), 0)
            self.assertEqual(path.read_bytes(), original)

    def test_shipped_optional_templates_and_example_stay_valid(self):
        paths = [ROOT / "skills/portable-agentic-system/pas/templates" / name for name in ("preference-record.json", "model-combination.json")]
        paths.append(ROOT / "examples/long-term-workspace/example-records.json")
        with contextlib.redirect_stdout(io.StringIO()):
            for path in paths:
                with self.subTest(path=path.name):
                    self.assertEqual(records.main([str(path)]), 0)


if __name__ == "__main__":
    unittest.main()

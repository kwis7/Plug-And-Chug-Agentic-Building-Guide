import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SKILL = REPO / "skills" / "portable-agentic-system"
SCRIPTS = SKILL / "scripts"


class RuntimeHookRecoveryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "Recovery Harness"
        self.env = os.environ.copy()
        self.env.pop("PAS_TASK", None)
        created = self.command(
            SCRIPTS / "create_agentic_system.py", "--root", self.root,
            "--config", SKILL / "pas" / "examples" / "starter-config.json",
        )
        self.assertEqual(created.returncode, 0, created.stderr + created.stdout)
        self.bin = self.root / ".pas" / "bin"
        self.task_path = self.root / "tasks" / "T-000-bootstrap" / "task.yaml"
        self.task = json.loads(self.task_path.read_text(encoding="utf-8"))

    def command(self, *args, input_text=None):
        return subprocess.run(
            [sys.executable, *map(str, args)], cwd=REPO, env=self.env,
            text=True, input=input_text, capture_output=True, check=False,
        )

    def save_task(self):
        self.task_path.write_text(json.dumps(self.task, indent=2), encoding="utf-8")
        status = self.command(self.bin / "generate_status.py", self.root)
        self.assertEqual(status.returncode, 0, status.stderr + status.stdout)

    def invalid_terminal_task(self):
        self.task["status"] = "complete"
        self.task["verification_state"] = "passed"
        self.task["handoff"]["summary"] = "Synthetic fixture awaiting a required receipt."
        self.save_task()

    def repair_receipt(self):
        receipt = self.root / "artifacts" / "verification.json"
        receipt.write_text('{"passed": true}\n', encoding="utf-8")
        self.task["verification"]["receipts"] = ["artifacts/verification.json"]
        self.save_task()

    def hook(self, runtime, payload=None, input_text=None):
        if input_text is None:
            input_text = json.dumps(payload)
        result = self.command(
            self.bin / "runtime_hook_gate.py", "--runtime", runtime,
            "--root", self.root, input_text=input_text,
        )
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        return json.loads(result.stdout)

    def test_repeated_failed_stop_halts_and_preserves_every_rejection(self):
        self.invalid_terminal_task()
        original = self.task_path.read_bytes()
        for runtime in ("codex", "claude-code"):
            with self.subTest(runtime=runtime):
                first = self.hook(runtime, {
                    "stop_hook_active": False, "last_assistant_message": "The task is complete.",
                })
                self.assertEqual(set(first), {"decision", "reason"})
                self.assertEqual(first["decision"], "block")
                self.assertIn("verification receipts are required", first["reason"])
                for _ in range(3):
                    retry = self.hook(runtime, {
                        "stop_hook_active": True, "last_assistant_message": "The receipt is still unavailable.",
                    })
                    self.assertEqual(retry["decision"], "block")
                    self.assertEqual(retry["reason"], first["reason"])
                    self.assertIs(retry["continue"], False)
                    self.assertIn("remains rejected", retry["stopReason"])
                    self.assertIn(first["reason"], retry["systemMessage"])
        self.assertEqual(self.task_path.read_bytes(), original)

    def test_continued_stop_checks_locks_and_accepts_only_repaired_gate(self):
        self.invalid_terminal_task()
        lock = self.root / ".pas" / "runtime" / "locks" / "fixture.lock.json"
        lock.write_text(json.dumps({"task_id": self.task["id"]}), encoding="utf-8")
        for runtime in ("codex", "claude-code"):
            self.assertEqual(self.hook(runtime, {"last_assistant_message": "The task is complete."})["decision"], "block")
        self.repair_receipt()
        for runtime in ("codex", "claude-code"):
            retry = self.hook(runtime, {"stop_hook_active": True})
            self.assertEqual(retry["decision"], "block")
            self.assertIs(retry["continue"], False)
            self.assertIn("locks remain", retry["reason"])
        lock.unlink()
        for runtime in ("codex", "claude-code"):
            self.assertEqual(self.hook(runtime, {"stop_hook_active": True}), {})
            self.assertEqual(self.hook(runtime, {"stop_hook_active": False}), {})

    def test_active_repair_and_failed_handoff_are_evaluated_honestly(self):
        for runtime in ("codex", "claude-code"):
            self.assertEqual(self.hook(runtime, {"last_assistant_message": "Progress update."}), {})
            retry = self.hook(runtime, {"stop_hook_active": True, "last_assistant_message": "A required input is unavailable."})
            self.assertEqual(retry["decision"], "block")
            self.assertIs(retry["continue"], False)
            self.assertIn("status is not terminal", retry["reason"])
        self.task["status"] = "failed"
        self.task["handoff"]["summary"] = "Required synthetic input unavailable; work stopped without success."
        self.save_task()
        for runtime in ("codex", "claude-code"):
            self.assertEqual(self.hook(runtime, {"stop_hook_active": True}), {})
        self.assertEqual(json.loads(self.task_path.read_text(encoding="utf-8"))["status"], "failed")

    def test_gemini_repeated_failures_keep_native_deny_schema(self):
        self.invalid_terminal_task()
        for continued in (False, True, True):
            result = self.hook("gemini-cli", {"stop_hook_active": continued, "prompt_response": "The task is complete."})
            self.assertEqual(set(result), {"decision", "reason"})
            self.assertEqual(result["decision"], "deny")
            self.assertIn("verification receipts are required", result["reason"])
        self.repair_receipt()
        self.assertEqual(self.hook("gemini-cli", {"prompt_response": "The task is complete."}), {})

    def test_malformed_payload_cannot_silently_pass(self):
        for runtime, decision in (("codex", "block"), ("claude-code", "block"), ("gemini-cli", "deny")):
            for malformed in ('{"stop_hook_active":', '[]', 'null', '{"stop_hook_active": "true"}'):
                with self.subTest(runtime=runtime, malformed=malformed):
                    result = self.hook(runtime, input_text=malformed)
                    self.assertEqual(result["decision"], decision)
                    self.assertNotIn("continue", result)

    def test_session_binding_selects_task_and_rejects_invalid_binding(self):
        self.invalid_terminal_task()
        second = self.root / "tasks" / "T-other" / "task.yaml"
        second.parent.mkdir()
        second_task = dict(self.task, id="T-other", status="active")
        second.write_text(json.dumps(second_task), encoding="utf-8")
        self.save_task()
        bound = self.command(self.bin / "bind_task.py", self.root, self.task_path, "--session", "S-fixture")
        self.assertEqual(bound.returncode, 0, bound.stderr + bound.stdout)
        binding = self.root / ".pas" / "runtime" / "sessions" / "S-fixture.json"
        for runtime in ("codex", "claude-code"):
            result = self.hook(runtime, {"session_id": "S-fixture", "stop_hook_active": True})
            self.assertIn("T-000-bootstrap", result["reason"])
            self.assertIn("verification receipts", result["reason"])
        self.repair_receipt()
        for runtime in ("codex", "claude-code"):
            self.assertEqual(self.hook(runtime, {"session_id": "S-fixture", "stop_hook_active": True}), {})
        for malformed in ('[]', '{"task": "../outside/task.yaml"}', '{"task":'):
            binding.write_text(malformed, encoding="utf-8")
            for runtime in ("codex", "claude-code"):
                result = self.hook(runtime, {"session_id": "S-fixture", "stop_hook_active": True})
                self.assertEqual(result["decision"], "block")
                self.assertIs(result["continue"], False)
                self.assertIn("binding", result["reason"])

    def test_malformed_task_gate_failure_is_returned_in_runtime_schema(self):
        self.invalid_terminal_task()
        self.task["outputs"] = 1
        self.task_path.write_text(json.dumps(self.task), encoding="utf-8")
        for runtime in ("codex", "claude-code"):
            result = self.hook(runtime, {"stop_hook_active": True})
            self.assertEqual(result["decision"], "block")
            self.assertIs(result["continue"], False)
            self.assertIn("cannot evaluate portable closeout gate", result["reason"])


if __name__ == "__main__":
    unittest.main()

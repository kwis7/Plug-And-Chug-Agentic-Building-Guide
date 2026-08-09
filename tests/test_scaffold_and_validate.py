import json
import re
import subprocess
import sys
import tempfile
import unittest
import urllib.parse
import zipfile
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SKILL = REPO / "skills" / "portable-agentic-system"
SCRIPTS = SKILL / "scripts"
CREATE = SCRIPTS / "create_agentic_system.py"
VALIDATE = SCRIPTS / "validate_agentic_system.py"
HEALTH = SCRIPTS / "harness_health_check.py"
STATUS = SCRIPTS / "generate_status.py"
GATE = SCRIPTS / "closeout_gate.py"
BUDGETS = SCRIPTS / "check_budgets.py"
LOCKS = SCRIPTS / "check_locks.py"
SMOKE = SCRIPTS / "adapter_smoke.py"
HOOK = SCRIPTS / "runtime_hook_gate.py"
DESCRIPTIONS = SCRIPTS / "check_descriptions.py"


class ScaffoldTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.root = self.base / "My Harness"
        self.config = self.base / "config.json"
        self.config.write_text(
            json.dumps(
                {
                    "system_name": "My Harness",
                    "owner_label": "a test user",
                    "language": "English",
                    "agents": [
                        {
                            "name": "Research Agent",
                            "purpose": "Research and source review.",
                            "audience": "research work",
                            "vault": True,
                            "routing_description": "Use when a request needs evidence collection, source comparison, literature synthesis, or uncertainty tracking. The agent owns research notes and citations, but final packaging and visual production belong to the Report Agent.",
                            "exclusions": ["final report layout", "external publication"],
                            "positive_examples": ["Compare the evidence behind two policy claims.", "Build a source ledger for this research question."],
                            "negative_examples": ["Lay out the final PDF.", "Publish this brief to the website."],
                        },
                        {
                            "name": "Report Agent",
                            "purpose": "Review and package reports.",
                            "audience": "report recipients",
                            "vault": False,
                            "routing_description": "Use when reviewed findings must become a clear report, diagram, slide deck, or delivery package. The agent owns presentation quality and release checks, but it does not invent evidence or replace domain research.",
                            "exclusions": ["primary research", "unsupported factual claims"],
                            "positive_examples": ["Turn the reviewed findings into a PDF report.", "Create a system diagram from this approved architecture."],
                            "negative_examples": ["Find current filings for this company.", "Decide whether an unsupported claim is true."],
                        },
                    ],
                }
            ),
            encoding="utf-8",
        )

    def run_cmd(self, *args):
        return subprocess.run([sys.executable, *map(str, args)], cwd=REPO, text=True, capture_output=True, check=False)

    def run_cmd_with_input(self, payload, *args):
        return subprocess.run([sys.executable, *map(str, args)], cwd=REPO, text=True, input=json.dumps(payload), capture_output=True, check=False)

    def create(self):
        result = self.run_cmd(CREATE, "--root", self.root, "--config", self.config)
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        return json.loads(result.stdout)

    def test_scaffold_uses_real_runtime_entrypoints(self):
        summary = self.create()
        self.assertGreater(summary["created_count"], 30)
        agents = (self.root / "AGENTS.md").read_text(encoding="utf-8")
        claude = (self.root / "CLAUDE.md").read_text(encoding="utf-8")
        gemini = (self.root / "GEMINI.md").read_text(encoding="utf-8")
        self.assertNotIn("@import", agents)
        self.assertTrue(claude.startswith("@AGENTS.md"))
        self.assertTrue(gemini.startswith("@./AGENTS.md"))
        self.assertIn("generated", (self.root / "STATUS.md").read_text(encoding="utf-8").lower())

    def test_scaffold_validates_and_health_is_static_only(self):
        self.create()
        validate = self.run_cmd(VALIDATE, self.root)
        self.assertEqual(validate.returncode, 0, validate.stderr + validate.stdout)
        report = json.loads(validate.stdout)
        self.assertTrue(report["valid"])
        health = self.run_cmd(HEALTH, self.root, "--json")
        self.assertEqual(health.returncode, 0, health.stderr + health.stdout)
        health_report = json.loads(health.stdout)
        self.assertEqual(health_report["runtime_verification"], "not_run")
        self.assertIn("never proves", health_report["note"])

    def test_false_import_fixture_fails(self):
        self.create()
        path = self.root / "AGENTS.md"
        path.write_text(path.read_text(encoding="utf-8") + "\n@import MEMORY.md\n", encoding="utf-8")
        validate = self.run_cmd(VALIDATE, self.root)
        self.assertNotEqual(validate.returncode, 0)
        self.assertIn("unsupported @import", validate.stdout)

    def test_status_is_generated_and_staleness_fails(self):
        self.create()
        current = self.run_cmd(STATUS, self.root, "--check")
        self.assertEqual(current.returncode, 0, current.stdout)
        (self.root / "STATUS.md").write_text("stale\n", encoding="utf-8")
        stale = self.run_cmd(STATUS, self.root, "--check")
        self.assertNotEqual(stale.returncode, 0)
        generated = self.run_cmd(STATUS, self.root)
        self.assertEqual(generated.returncode, 0, generated.stderr)

    def test_terminal_task_requires_receipts(self):
        self.create()
        path = self.root / "tasks" / "T-000-bootstrap" / "task.yaml"
        task = json.loads(path.read_text(encoding="utf-8"))
        task["status"] = "complete"
        task["verification_state"] = "passed"
        task["handoff"]["summary"] = "Bootstrap reviewed."
        path.write_text(json.dumps(task, indent=2), encoding="utf-8")
        self.run_cmd(STATUS, self.root)
        failed = self.run_cmd(GATE, self.root, path.relative_to(self.root))
        self.assertNotEqual(failed.returncode, 0)
        self.assertIn("receipts", failed.stdout)

    def test_valid_terminal_task_passes_closeout_gate(self):
        self.create()
        receipt = self.root / "artifacts" / "verification.json"
        receipt.write_text('{"passed": true}\n', encoding="utf-8")
        path = self.root / "tasks" / "T-000-bootstrap" / "task.yaml"
        task = json.loads(path.read_text(encoding="utf-8"))
        task["status"] = "complete"
        task["verification_state"] = "passed"
        task["verification"]["receipts"] = ["artifacts/verification.json"]
        task["handoff"]["summary"] = "Bootstrap reviewed and verified."
        path.write_text(json.dumps(task, indent=2), encoding="utf-8")
        self.run_cmd(STATUS, self.root)
        passed = self.run_cmd(GATE, self.root, path.relative_to(self.root))
        self.assertEqual(passed.returncode, 0, passed.stdout + passed.stderr)

    def test_memory_budget_is_enforced(self):
        self.create()
        (self.root / "MEMORY.md").write_text("x\n" * 130, encoding="utf-8")
        budget = self.run_cmd(BUDGETS, self.root)
        self.assertNotEqual(budget.returncode, 0)
        self.assertIn("MEMORY.md", budget.stdout)

    def test_resource_lock_has_owner_and_release_guard(self):
        self.create()
        task_path = self.root / "tasks" / "T-000-bootstrap" / "task.yaml"
        task = json.loads(task_path.read_text(encoding="utf-8"))
        task["execution"]["resources"] = ["SYSTEM_MAP.md"]
        task["execution"]["writer"] = "agent-a"
        task_path.write_text(json.dumps(task, indent=2), encoding="utf-8")
        acquired = self.run_cmd(LOCKS, self.root, "acquire", "--resource", "SYSTEM_MAP.md", "--task", "T-000-bootstrap", "--session", "S-1", "--writer", "agent-a")
        self.assertEqual(acquired.returncode, 0, acquired.stdout)
        renewed = self.run_cmd(LOCKS, self.root, "renew", "--resource", "SYSTEM_MAP.md", "--task", "T-000-bootstrap", "--session", "S-1")
        self.assertEqual(renewed.returncode, 0, renewed.stdout)
        blocked = self.run_cmd(LOCKS, self.root, "acquire", "--resource", "SYSTEM_MAP.md", "--task", "T-000-bootstrap", "--session", "S-2", "--writer", "agent-a")
        self.assertNotEqual(blocked.returncode, 0)
        wrong = self.run_cmd(LOCKS, self.root, "release", "--resource", "SYSTEM_MAP.md", "--task", "T-000-bootstrap", "--session", "S-2")
        self.assertNotEqual(wrong.returncode, 0)
        released = self.run_cmd(LOCKS, self.root, "release", "--resource", "SYSTEM_MAP.md", "--task", "T-000-bootstrap", "--session", "S-1")
        self.assertEqual(released.returncode, 0, released.stdout)

    def test_undeclared_resource_lock_is_rejected(self):
        self.create()
        result = self.run_cmd(LOCKS, self.root, "acquire", "--resource", "SYSTEM_MAP.md", "--task", "T-000-bootstrap", "--session", "S-1", "--writer", "agent-a")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("resource_not_declared_in_task", result.stdout)

    def test_large_context_file_requires_manifest_policy(self):
        self.create()
        large = self.root / "raw_data" / "large.txt"
        large.write_text("x" * (300 * 1024), encoding="utf-8")
        failed = self.run_cmd(BUDGETS, self.root)
        self.assertNotEqual(failed.returncode, 0)
        manifest_path = self.root / "raw_data" / "manifest.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest["entries"].append({"path": "large.txt", "size_bytes": large.stat().st_size, "context_policy": "never-auto-load", "summary": "Synthetic large-file fixture; load only by explicit test request."})
        manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
        passed = self.run_cmd(BUDGETS, self.root)
        self.assertEqual(passed.returncode, 0, passed.stdout)

    def test_failed_task_can_close_without_success_receipts(self):
        self.create()
        path = self.root / "tasks" / "T-000-bootstrap" / "task.yaml"
        task = json.loads(path.read_text(encoding="utf-8"))
        task["status"] = "failed"
        task["handoff"]["summary"] = "Stopped because the required upstream input was unavailable."
        path.write_text(json.dumps(task, indent=2), encoding="utf-8")
        self.run_cmd(STATUS, self.root)
        result = self.run_cmd(GATE, self.root, path.relative_to(self.root))
        self.assertEqual(result.returncode, 0, result.stdout)

        health = self.run_cmd(HEALTH, self.root, "--json")
        self.assertEqual(health.returncode, 0, health.stdout)
        self.assertEqual(json.loads(health.stdout)["terminal_tasks_without_receipts"], 0)

    def test_runtime_hook_translates_invalid_completion_to_block(self):
        self.create()
        for runtime, decision in [("codex", "block"), ("claude-code", "block"), ("gemini-cli", "deny")]:
            result = self.run_cmd_with_input({"last_assistant_message": "The task is complete."}, HOOK, "--runtime", runtime, "--root", self.root)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout)["decision"], decision)

    def test_static_adapter_smokes_are_explicit(self):
        self.create()
        for runtime in ["codex", "claude-code", "gemini-cli"]:
            result = self.run_cmd(SMOKE, self.root, "--runtime", runtime)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertEqual(json.loads(result.stdout)["verification_level"], "static")

        config_path = self.root / ".codex" / "hooks.json"
        config = json.loads(config_path.read_text(encoding="utf-8"))
        config["hooks"].pop("Stop")
        config_path.write_text(json.dumps(config, indent=2), encoding="utf-8")
        validate = self.run_cmd(VALIDATE, self.root)
        self.assertNotEqual(validate.returncode, 0)
        self.assertIn("codex static adapter failed", validate.stdout)

    def test_agent_descriptions_and_route_evals_pass(self):
        self.create()
        result = self.run_cmd(DESCRIPTIONS, self.root)
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertEqual(json.loads(result.stdout)["routing_agents"], 2)
        identity = (self.root / "research-Agent" / "IDENTITY.md").read_text(encoding="utf-8")
        self.assertIn("Use when a request needs evidence collection", identity)

    def test_runtime_compatibility_classifies_every_named_product(self):
        manifest = json.loads((SKILL / "pas" / "compatibility" / "runtime-compatibility.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["schema_version"], 2)
        products = {item["id"]: item for item in manifest["products"]}
        expected = {
            "codex", "claude-code", "gemini-cli", "openclaw", "hermes-agent", "mimo-code", "mimo-claw",
            "claude-cowork", "chatgpt-projects", "custom-gpt", "tencent-workbuddy", "cc-switch",
            "deepseek", "qwen", "minimax", "glm", "xiaomi-mimo-api", "tencent-hunyuan", "direct-api",
        }
        self.assertEqual(set(products), expected)
        self.assertEqual(products["cc-switch"]["category"], "switchboard")
        self.assertEqual(products["deepseek"]["status"], "provider_only")
        self.assertEqual(products["mimo-claw"]["status"], "provisional")
        self.assertEqual(products["openclaw"]["status"], "documented_only")
        self.assertEqual(products["hermes-agent"]["status"], "documented_only")
        self.assertEqual(products["mimo-code"]["status"], "documented_only")
        self.assertEqual(products["direct-api"]["status"], "reference_pattern")
        for runtime in ["codex", "claude-code", "gemini-cli"]:
            self.assertIn("runtime_hook_gate.py", " ".join(products[runtime]["generated_configuration"]))
            self.assertEqual(products[runtime]["fresh_session_verification"], "not_run")

    def test_scaffold_refuses_overwrite_and_dry_run_is_read_only(self):
        dry = self.run_cmd(CREATE, "--root", self.root, "--config", self.config, "--dry-run")
        self.assertEqual(dry.returncode, 0, dry.stderr)
        self.assertFalse(self.root.exists())
        self.create()
        second = self.run_cmd(CREATE, "--root", self.root, "--config", self.config)
        self.assertNotEqual(second.returncode, 0)
        self.assertIn("Refusing to overwrite", second.stderr)

    def test_skill_is_progressive_and_has_trigger_evaluations(self):
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        self.assertLess(len(text.splitlines()), 500)
        self.assertIn("description:", text)
        self.assertTrue((SKILL / "pas" / "references" / "master-build-playbook.md").exists())
        self.assertTrue((SKILL / "pas" / "references" / "description-routing-evals.md").exists())

    def test_system_map_assets_and_long_guide_exist(self):
        assets = REPO / "docs" / "assets"
        for name in [
            "harness-concept-map.html", "harness-concept-map.png", "harness-concept-map.svg",
            "harness-concept-map.zh-CN.html", "harness-concept-map.zh-CN.png", "harness-concept-map.zh-CN.svg",
            "anonymised-agent-system-map.html", "anonymised-agent-system-map.png", "anonymised-agent-system-map.svg",
            "anonymised-agent-system-map.zh-CN.html", "anonymised-agent-system-map.zh-CN.png", "anonymised-agent-system-map.zh-CN.svg",
        ]:
            self.assertTrue((assets / name).exists(), name)
        guide = SKILL / "pas" / "references" / "master-build-playbook.md"
        self.assertGreater(len(guide.read_text(encoding="utf-8").split()), 10000)

    def test_local_markdown_links_resolve(self):
        broken = []
        for path in REPO.rglob("*.md"):
            if ".git" in path.parts:
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            for target in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", text):
                target = target.strip().split()[0].strip("<>")
                if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                    continue
                relative = urllib.parse.unquote(target.split("#", 1)[0])
                if not (path.parent / relative).resolve().exists():
                    broken.append(f"{path.relative_to(REPO)} -> {target}")
        self.assertEqual(broken, [])

    def test_downloadable_guide_has_at_least_30_pages(self):
        docx = REPO / "docs" / "downloads" / "Agentic-System-Building-Guide.docx"
        pdf = REPO / "docs" / "downloads" / "Agentic-System-Building-Guide.pdf"
        self.assertTrue(docx.exists())
        self.assertTrue(pdf.exists())
        with zipfile.ZipFile(docx) as archive:
            self.assertIn("@kwis7", archive.read("docProps/core.xml").decode("utf-8"))
        try:
            from pypdf import PdfReader
        except ImportError:
            self.skipTest("pypdf not installed")
        self.assertGreaterEqual(len(PdfReader(str(pdf)).pages), 30)


if __name__ == "__main__":
    unittest.main()

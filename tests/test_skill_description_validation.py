"""Regression cases for portable metadata and truthful static routing checks."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "skills/portable-agentic-system/scripts"
sys.path.insert(0, str(SCRIPTS))
import check_descriptions


class SkillDescriptionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.skill = self.root / "source-review" / "SKILL.md"
        self.skill.parent.mkdir()

    def write(self, fields):
        self.skill.write_text("---\n" + fields + "\n---\n\n# Source review\n", encoding="utf-8")

    def report(self):
        return check_descriptions.check(self.root)

    def test_folded_description_keeps_triggers_and_boundaries(self):
        self.write("name: source-review\ndescription: >-\n  Compare supplied sources. Use when checking evidence\n  and tracking unknowns. Do not use for external publication.\nmetadata:\n  author: 'O''Brien'\ncompatibility: Python 3.10 or later")
        fields = check_descriptions.frontmatter(self.skill)
        self.assertEqual(fields["description"], "Compare supplied sources. Use when checking evidence and tracking unknowns. Do not use for external publication.")
        self.assertEqual(fields["metadata"], {"author": "O'Brien"})
        self.assertTrue(self.report()["valid"], self.report())

    def test_literal_description_preserves_line_breaks(self):
        self.write("name: source-review\ndescription: |\n  Use when checking sources.\n  Do not use for publishing.")
        self.assertEqual(check_descriptions.frontmatter(self.skill)["description"], "Use when checking sources.\nDo not use for publishing.\n")
        self.assertTrue(self.report()["valid"], self.report())

    def test_folded_paragraphs_and_more_indented_lines(self):
        self.write("name: source-review\ndescription: >-\n  First paragraph.\n\n  Second paragraph.\n    Keep this indented.\n  Last line.")
        self.assertEqual(check_descriptions.frontmatter(self.skill)["description"], "First paragraph.\nSecond paragraph.\n  Keep this indented.\nLast line.")

    def test_quoted_colons_hashes_and_inline_comments(self):
        description = 'Use when reviewing sources: retain # labels. Do not use for sending.'
        self.write("name: source-review # identity\ndescription: " + json.dumps(description) + " # note")
        self.assertEqual(check_descriptions.frontmatter(self.skill)["description"], description)
        self.assertTrue(self.report()["valid"], self.report())
        self.assertTrue(self.report()["warnings"])

    def test_boundary_limits_and_directory_identity(self):
        for fields, issue in [
            ("name: " + "a" * 65 + "\ndescription: Use when reviewing sources. Do not use for sending.", "1-64"),
            ("name: Source-Review\ndescription: Use when reviewing sources. Do not use for sending.", "lowercase"),
            ("name: source--review\ndescription: Use when reviewing sources. Do not use for sending.", "single hyphens"),
            ("name: wrong-folder\ndescription: Use when reviewing sources. Do not use for sending.", "parent directory"),
            ("name: source-review\ndescription: " + "x" * 1025, "1024"),
            ("name: source-review\ndescription: Use when reviewing sources. Do not use for sending.\ncompatibility: " + "x" * 501, "1-500"),
        ]:
            with self.subTest(issue=issue):
                self.write(fields)
                report = self.report()
                self.assertFalse(report["valid"])
                self.assertIn(issue, str(report["issues"]))

    def test_exact_maximum_description_and_compatibility_pass(self):
        description = "Use when reviewing sources. Do not use for sending. "
        description += "x" * (1024 - len(description))
        self.write("name: source-review\ndescription: " + description + "\ncompatibility: " + "x" * 500)
        self.assertTrue(self.report()["valid"], self.report())

    def test_malformed_metadata_reports_instead_of_crashing(self):
        for fields in [
            "name: source-review\nname: second\ndescription: Use when reviewing sources.",
            "name: source-review\ndescription: true",
            "name: source-review\ndescription: &alias unsafe",
            "name: source-review\ndescription: [one, two]",
            "name: source-review\ndescription: \"unclosed",
            "name: source-review\ndescription: \"Use when checking. Do not use for sending.\"#comment",
            "name: source-review\ndescription: 'Use when checking. Do not use for sending.'#comment",
            "name: source-review\ndescription: >-\n  This first line sets indentation.\n This line has inconsistent indentation.",
        ]:
            with self.subTest(fields=fields):
                self.write(fields)
                report = self.report()
                self.assertFalse(report["valid"])
                self.assertTrue(report["issues"])

    def test_mapping_scopes_and_indentation_are_not_guessed(self):
        prefix = "name: source-review\ndescription: Use when reviewing sources. Do not use for sending.\n"
        self.write(prefix + "metadata:\n  author: First\nextra:\n  author: Second")
        fields = check_descriptions.frontmatter(self.skill)
        self.assertEqual(fields["metadata"], {"author": "First"})
        self.assertEqual(fields["extra"], {"author": "Second"})
        self.assertTrue(self.report()["valid"], self.report())
        for fields in [
            "metadata:\n  author: First\n    nested: Value",
            "metadata:\n    author: First\n  version: Second",
            "metadata:\n  author: First\n  author: Second",
            "  extra: Value",
            "description: Use when reviewing: sources. Do not use for sending.",
        ]:
            with self.subTest(fields=fields):
                self.write(prefix + fields)
                self.assertFalse(self.report()["valid"], self.report())

    def test_empty_metadata_is_null_until_a_map_entry_exists(self):
        prefix = "name: source-review\ndescription: Use when reviewing sources. Do not use for sending.\n"
        for value in ["metadata:", "metadata: # empty", "metadata: null"]:
            with self.subTest(value=value):
                self.write(prefix + value)
                self.assertIsNone(check_descriptions.frontmatter(self.skill)["metadata"])
                self.assertFalse(self.report()["valid"], self.report())

    def test_non_string_yaml_scalars_cannot_be_metadata_strings(self):
        prefix = "name: source-review\ndescription: Use when reviewing sources. Do not use for sending.\nmetadata:\n  version: "
        for value in ["0x1", "0o7", "0b10", ".nan", "+.inf", "1e3", "1_000", "1.2", "false", "null"]:
            with self.subTest(value=value):
                self.write(prefix + value)
                self.assertFalse(self.report()["valid"], self.report())
                self.write(prefix + json.dumps(value))
                self.assertTrue(self.report()["valid"], self.report())

    def test_block_chomping_and_empty_content(self):
        prefix = "name: source-review\ndescription: "
        for style in [">", "|"]:
            for chomp, expected in [("-", "Use when checking. Do not use for sending."), ("", "Use when checking. Do not use for sending.\n"), ("+", "Use when checking. Do not use for sending.\n\n")]:
                with self.subTest(style=style, chomp=chomp):
                    self.write(prefix + style + chomp + "\n  Use when checking. Do not use for sending.\n")
                    self.assertEqual(check_descriptions.frontmatter(self.skill)["description"], expected)
            for chomp, expected in [("-", ""), ("", ""), ("+", "\n")]:
                with self.subTest(empty=True, style=style, chomp=chomp):
                    self.write(prefix + style + chomp + "\n")
                    self.assertEqual(check_descriptions.frontmatter(self.skill)["description"], expected)

    def test_folded_blank_runs_preserve_more_indented_boundaries(self):
        self.write("name: source-review\ndescription: >+\n\n  Normal text.\n\n    Indented text.\n\n  Last text.\n")
        self.assertEqual(check_descriptions.frontmatter(self.skill)["description"], "\nNormal text.\n\n  Indented text.\n\nLast text.\n\n")

    def test_missing_closing_delimiter_is_a_cli_diagnostic(self):
        self.skill.write_text("---\nname: source-review\n", encoding="utf-8")
        result = subprocess.run([sys.executable, str(SCRIPTS / "check_descriptions.py"), str(self.root)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn("closing delimiter", str(json.loads(result.stdout)["issues"]))
        self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()

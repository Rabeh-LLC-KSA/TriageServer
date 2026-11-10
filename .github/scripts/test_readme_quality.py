import tempfile
import unittest
from pathlib import Path

import readme_quality as quality


def sample():
    return "\n".join(quality.REQUIRED) + "\n" + quality.START + "\n" + (
        "**README version:** `1.0.0` · **Last updated:** `2026-11-10`\n"
        "**Last change:** Initial standard.\n"
    ) + quality.END + "\n\n## README change log\n\n| Version | Date | Changes |\n| --- | --- | --- |\n| 1.0.0 | 2026-11-10 | Initial standard. |\n"


class ReadmeQualityTests(unittest.TestCase):
    def test_update_preserves_body_and_history(self):
        text = sample() + "\nTechnical detail stays unchanged.\n"
        updated = quality.update_text(text, "1.0.1", "2026-11-10", "Correct setup command.")
        self.assertEqual(quality.metadata(updated)["version"], "1.0.1")
        self.assertIn("| 1.0.0 | 2026-11-10 | Initial standard. |", updated)
        self.assertIn("Technical detail stays unchanged.", updated)
        quality.check_revision(text, updated)

    def test_changed_readme_needs_version_bump(self):
        with self.assertRaisesRegex(ValueError, "increment"):
            quality.check_revision(sample(), sample() + "new detail")

    def test_unchanged_readme_keeps_version(self):
        quality.check_revision(sample(), sample())

    def test_rejects_invalid_and_nonincreasing_versions(self):
        for version in ["v1.0.1", "1.0", "01.2.3", "1.0.0", "0.9.0"]:
            with self.subTest(version=version), self.assertRaises(ValueError):
                quality.update_text(sample(), version, "2026-11-10", "Change.")

    def test_rejects_invalid_dates_and_notes(self):
        for date, note in [("2026-11-09", "Change."), ("9999-01-01", "Change."), ("20261110", "Change."), ("2026-11-10", ""), ("2026-11-10", "a|b")]:
            with self.subTest(date=date, note=note), self.assertRaises(ValueError):
                quality.update_text(sample(), "1.0.1", date, note)

    def test_missing_slogan_or_pillar_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            for required in quality.REQUIRED:
                with self.subTest(required=required), self.assertRaisesRegex(ValueError, "brand/pillar"):
                    quality.check_text(sample().replace(required, ""), "README.md", Path(directory))

    def test_links_are_relative_to_the_readme(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "docs").mkdir()
            (root / "README.md").write_text("target")
            quality.check_text(sample() + "[root](../README.md)", "docs/README.md", root)
            with self.assertRaisesRegex(ValueError, "broken relative link"):
                quality.check_text(sample() + "[missing](missing.md)", "docs/README.md", root)

    def test_fences_and_history_are_required(self):
        with tempfile.TemporaryDirectory() as directory:
            for text in [sample() + "\n```python\n", sample().replace("| 1.0.0 |", "| 0.9.0 |")]:
                with self.assertRaises(ValueError):
                    quality.check_text(text, "README.md", Path(directory))


if __name__ == "__main__":
    unittest.main()

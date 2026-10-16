import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_script(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ReplyFormattingTests(unittest.TestCase):
    def setUp(self):
        self.check = load_script("check_gmail_html").check

    def test_blank_paragraph_separator(self):
        self.assertFalse(self.check("<div>Hello!</div><div><br></div><div>Thank you!</div>"))

    def test_missing_separator(self):
        self.assertTrue(self.check("<div>Hello!</div><div>Thank you!</div>"))

    def test_margin_is_not_a_blank_line(self):
        self.assertTrue(self.check('<p style="margin:0 0 16px">Hello!</p>'))

    def test_trailing_blank_line(self):
        self.assertTrue(self.check("<div>Thank you!</div><div><br></div>"))

    def test_extra_break_inside_closing(self):
        self.assertTrue(self.check("<div>Thank you!<br></div>"))

    def test_voice_settings_are_optional(self):
        self.assertFalse(self.check("<div>Hi Sam!</div>"))
        self.assertTrue(self.check("<div>Hi Sam!</div>", english_greeting="Hey"))
        self.assertFalse(self.check("<div>Hello :) More text</div>"))
        self.assertTrue(self.check("<div>Hello :) More text</div>", emoticon_ends_paragraph=True))


class ExportTests(unittest.TestCase):
    def test_allowlist_excludes_private_data_and_history(self):
        exporter = load_script("export_core")
        with tempfile.TemporaryDirectory() as temporary:
            destination = Path(temporary) / "public-core"
            exporter.export_core(destination)
            actual = {str(p.relative_to(destination)) for p in destination.rglob("*") if p.is_file()}
            self.assertEqual(actual, set(exporter.PUBLIC_FILES))
            self.assertFalse((destination / "personalization").exists())
            self.assertFalse((destination / ".git").exists())

    def test_refuses_to_overwrite_files(self):
        exporter = load_script("export_core")
        with tempfile.TemporaryDirectory() as temporary:
            destination = Path(temporary) / "public-core"
            destination.mkdir()
            marker = destination / "keep.txt"
            marker.write_text("Keep this file")
            with self.assertRaises(ValueError):
                exporter.export_core(destination)
            self.assertEqual(marker.read_text(), "Keep this file")


if __name__ == "__main__":
    unittest.main()

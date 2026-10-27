"""Akzeptanztests für die kleine Live-Aufgabe."""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.projektstart import describe_project


class ProjektstartTests(unittest.TestCase):
    def test_name_and_visible_directories(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "beispielprojekt"
            root.mkdir()
            (root / "data").mkdir()
            (root / "scripts").mkdir()
            (root / ".git").mkdir()
            (root / "README.md").write_text("Demo", encoding="utf-8")
            self.assertEqual(describe_project(root), ("beispielprojekt", ["data", "scripts"]))


if __name__ == "__main__":
    unittest.main()

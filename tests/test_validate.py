"""Tests für die Datenvalidierung. Ein Test scheitert vor dem Bugfix."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.validate import invalid_rows, validate_date


class DateValidationTests(unittest.TestCase):
    def test_valid_date(self):
        self.assertTrue(validate_date("1742-03-14"))

    def test_invalid_calendar_dates(self):
        self.assertFalse(validate_date("1742-02-29"))
        self.assertFalse(validate_date("1743-06-31"))

    def test_invalid_format(self):
        self.assertFalse(validate_date("14.03.1742"))

    def test_corpus_has_two_invalid_dates(self):
        self.assertEqual({row["id"] for row in invalid_rows()}, {"B003", "B018"})


if __name__ == "__main__":
    unittest.main()

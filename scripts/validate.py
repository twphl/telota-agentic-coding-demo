"""Validierung eines fiktiven historischen Briefkorpus (nur Standardbibliothek)."""
import csv
from datetime import datetime
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "documents.csv"


def validate_date(value: str) -> bool:
    """Prüfe, ob ein Datum im Format YYYY-MM-DD kalendarisch gültig ist."""
    # Absichtlicher Demo-Bug: Ein Formatvergleich prüft keine echten Kalendertage.
    return len(value) == 10 and value[4] == "-" and value[7] == "-"


def invalid_rows(path: Path = DATA_FILE) -> list[dict[str, str]]:
    with Path(path).open(newline="", encoding="utf-8") as stream:
        return [row for row in csv.DictReader(stream) if not validate_date(row["date"])]


def main() -> None:
    errors = invalid_rows()
    print(f"Ungültige Datumsangaben: {len(errors)}")
    for row in errors:
        print(f'{row["id"]}: {row["date"]}')


if __name__ == "__main__":
    main()

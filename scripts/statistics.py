"""Kleine, unabhängige Korpusstatistik."""
import csv
from collections import Counter
from pathlib import Path

SOURCE = Path(__file__).resolve().parents[1] / "data" / "documents.csv"


def main() -> None:
    with SOURCE.open(newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream))
    print(f"Briefe: {len(rows)}")
    for year, count in sorted(Counter(row["date"][:4] for row in rows).items()):
        print(f"{year}: {count}")


if __name__ == "__main__":
    main()

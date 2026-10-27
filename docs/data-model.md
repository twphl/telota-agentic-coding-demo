# Datenmodell

Fiktiver Briefkorpus mit 20 Einträgen (1742–1743). Keine echten historischen Quellen.

| Spalte | Bedeutung |
| --- | --- |
| id | Eindeutige Briefkennung |
| date | Datum im ISO-Format YYYY-MM-DD |
| sender | Absender:in |
| recipient | Empfänger:in |
| place | Ort |
| title | Kurztitel |

Die Daten enthalten absichtlich zwei unmögliche Kalendertage. Die Demo soll diese **erkennen**, nicht die Quelldaten verändern. Das Skript `scripts/validate.py` enthält einen absichtlichen Validierungsfehler.

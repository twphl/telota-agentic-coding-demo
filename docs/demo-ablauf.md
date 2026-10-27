# OMP-Live-Demo: 10 Minuten maximal

| Zeit | Aktion | Gezeigte Fähigkeit |
| --- | --- | --- |
| 0:00–2:00 | Repo, AGENTS.md, CSV und Skripte erkunden | Projektkontext und Werkzeuge |
| 2:00–4:00 | Issue #1 lesen und zunächst nur Plan erstellen | Planung und Steuerung |
| 4:00–8:00 | Validierungsfehler beheben, Tests ausführen | Agentic Loop |
| 8:00–10:00 | Ausgabe und Git-Diff kontrollieren | Menschliche Prüfung |

**Startprompt:** „Lies README.md und AGENTS.md. Untersuche das Repository und Issue #1. Erkläre kurz deinen Plan, aber ändere noch keine Dateien.“

**Umsetzung:** „Implementiere den kleinsten sinnvollen Fix für Issue #1. Verändere keine Quelldaten. Führe die Tests und das Validierungsskript aus und zeige den Diff.“

**Optional nur bei Zeitreserve:** „Die Fehler sollen zusätzlich in einen separaten CSV-Bericht exportiert werden. Ändere die Quelldaten nicht.“ (Issue #2)

**Fallback:** `scripts/projektstart.py` und `tests/test_projektstart.py` sind die frühere, einfachere Demo. Nicht beide live durchführen.

**Wichtig:** Der Workshop selbst startet danach mit dem separaten GitLab-Kit und dem TEI-Korpus.

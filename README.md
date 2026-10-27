# TELOTA Agentic Coding Demo

Ein bewusst unvollständiges Mini-Forschungsprojekt für die **maximal zehnminütige** OMP-Live-Demo am 28.10.2026. Die 20 historischen Briefe sind vollständig fiktiv.

## Start

```bash
git clone https://github.com/twphl/telota-agentic-coding-demo.git
cd telota-agentic-coding-demo
python -m unittest discover -s tests -v
omp
```

## Hauptdemo: Datumsvalidierung (Issue #1)

- Zuerst Repository und `AGENTS.md` untersuchen, noch nichts ändern.
- `scripts/validate.py` prüft derzeit nur das Zeichenformat, nicht die kalendarische Gültigkeit.
- `data/documents.csv` enthält zwei unmögliche Daten; sie dürfen **nicht korrigiert** werden.
- Plan erstellen, minimalen Bugfix implementieren, Tests und Skript ausführen, Git-Diff kontrollieren.
- **Optionale Nachforderung:** Fehler als CSV-Bericht ausgeben, ohne Quelldaten zu verändern (Issue #2).

Die Tests schlagen im Ausgangszustand absichtlich fehl. `scripts/statistics.py` bietet eine kleine funktionierende Vergleichsaufgabe. `scripts/projektstart.py` ist eine separate, einfachere Fallback-Demo.

## Zeitbudget

2 Minuten Orientierung, 2 Minuten Plan, 4 Minuten Umsetzung, 2 Minuten Prüfung. Nach Minute 8 keine neue Aufgabe beginnen. `docs/demo-ablauf.md` enthält die Moderation.

## Abgrenzung

Das eigentliche Workshop-Kit mit Copier und TEI-Korpus liegt separat in GitLab. Dieses GitHub-Repository ist nur die Live-Demo.

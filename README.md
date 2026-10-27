# TELOTA Agentic Coding Demo

Kleines, bewusst unvollständiges Übungsrepository für die OMP-Live-Demo am 28.10.2026 (Folien 10–14). **Nicht** das eigentliche Workshop-Kit oder der Otter-Korpus.

## Start

```bash
git clone https://github.com/twphl/telota-agentic-coding-demo.git
cd telota-agentic-coding-demo
python -m unittest discover -s tests -v
omp
```

## Live-Auftrag

1. Projektstruktur und `AGENTS.md` lesen, zunächst nichts ändern.
2. `scripts/projektstart.py` ergänzen: Projektordnername und sichtbare direkte Unterordner ausgeben.
3. Nur Python-Standardbibliothek; Quelldaten nicht verändern; keine Abhängigkeiten ergänzen.
4. Skript ausführen, Ausgabe mit Ordnerstruktur vergleichen.
5. **Nachforderung live:** Skript muss auch aus einem anderen Arbeitsverzeichnis funktionieren.

Die Datei `scripts/projektstart.py` ist absichtlich unvollständig. Die Tests beschreiben das gewünschte Verhalten und schlagen vor der Umsetzung fehl. Die Nachforderung sollte erst im Live-Teil genannt werden.

## Abgrenzung

Der eigentliche Workshop verwendet das separate GitLab-Workshop-Kit, Copier und TEI-Daten unter `data/corpus/tei/`. Dieses GitHub-Repository dient nur der kurzen OMP-Vorführung.

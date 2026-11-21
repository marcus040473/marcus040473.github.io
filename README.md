# Layerling – meine Fassung

Unter **https://marcus040473.github.io** läuft eine Fassung von
[Layerling](https://github.com/henmedia/layerling), dem 3D-CAD für den
3D-Druck von Stefan (henmedia), mit dem Werkzeug **Oberfläche**: Rillen,
Rändel, Waben und Noppen auf jedem Körper, mit Masken und nachträglich
änderbar.

- **Quellcode dieser Fassung:** zurzeit [marcus040473/layerling_msto, Zweig `claude/hopeful-dirac-sj8lu3`](https://github.com/marcus040473/layerling_msto/tree/claude/hopeful-dirac-sj8lu3) (Arbeitszweig, bis er in [marcus040473/layerling, Zweig `marcus`](https://github.com/marcus040473/layerling/tree/marcus) zusammengeführt ist)
- **Lizenz:** Layerling steht unter der AGPL-3.0; diese Fassung ebenso.
- **Entwürfe** werden im eigenen Browser gespeichert, nicht auf dieser Seite.
  Zum Sichern im Export-Fenster als `.lyl`-Entwurf speichern (danach Strg+S).

## Wie die Seite entsteht

Dieses Repo enthält nur den Bauauftrag
[`.github/workflows/layerling.yml`](.github/workflows/layerling.yml): Er holt
den Zweig `marcus`, baut die statische Fassung (`npm run export`) und stellt
sie auf GitHub Pages. Er läuft bei jeder Änderung hier, einmal in der Nacht
und von Hand unter **Actions → Layerling-Webseite → Run workflow**.

## Teständerungen

Änderungen, die noch nicht bei Stefan sind, liegen als Datei im Ordner
[`testaenderungen/`](testaenderungen/) und werden beim Bauen dazugenommen –
so lassen sie sich hier schon ausprobieren. Zurzeit:

- `1917-gridfinity-groesse.patch` – Gridfinity-Behälter und -Tabletts so groß,
  wie das gewählte Druckbett reicht (Discussion #1917; Zweig
  `gridfinity-larger-boxes-1917` in marcus040473/layerling).

Ausbauen: die Datei löschen. Passt eine Datei nicht mehr, wird sie übersprungen
(Warnung unter Actions), die Seite wird trotzdem gebaut.

# Layerling – meine Fassung

Unter **https://marcus040473.github.io** läuft eine Fassung von
[Layerling](https://github.com/henmedia/layerling), dem 3D-CAD für den
3D-Druck von Stefan (henmedia), mit dem Werkzeug **Oberfläche**: Rillen,
Rändel, Waben und Noppen auf jedem Körper, mit Masken und nachträglich
änderbar.

- **Quellcode dieser Fassung:** [marcus040473/layerling, Zweig `marcus`](https://github.com/marcus040473/layerling/tree/marcus)
- **Lizenz:** Layerling steht unter der AGPL-3.0; diese Fassung ebenso.
- **Entwürfe** werden im eigenen Browser gespeichert, nicht auf dieser Seite.
  Zum Sichern im Export-Fenster als `.lyl`-Entwurf speichern (danach Strg+S).

## Wie die Seite entsteht

Dieses Repo enthält nur den Bauauftrag
[`.github/workflows/layerling.yml`](.github/workflows/layerling.yml): Er holt
den Zweig `marcus`, baut die statische Fassung (`npm run export`) und stellt
sie auf GitHub Pages. Er läuft bei jeder Änderung hier, einmal in der Nacht
und von Hand unter **Actions → Layerling-Webseite → Run workflow**.

# Sitio personal — Dariel Amador

Sitio estático (sin build). Todo el contenido se edita en `contenido.js`.

## Agregar contenido
- PDF: copiá el archivo a `contenido/pdf/` y agregá `{ tipo: "pdf", titulo, descripcion, archivo: "contenido/pdf/nombre.pdf" }`.
- Markdown: copiá el `.md` a `contenido/md/` y agregá `{ tipo: "md", ... archivo: "contenido/md/nombre.md" }`. Soporta LaTeX con `$...$` y `$$...$$`.
- Nueva sección del portafolio: `{ tipo: "seccion", id: "sin-espacios", titulo, descripcion, items: [ ... ] }`.

## Ver localmente
`python3 -m http.server` en esta carpeta y abrí http://localhost:8000 (abrir el index con doble clic no carga los Markdown).

## Publicar en GitHub Pages
1. Creá el repo `darielamador.github.io` y subí el contenido de esta carpeta.
2. Settings → Pages → Deploy from branch → `main` / root.
3. Queda en https://darielamador.github.io

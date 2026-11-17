# AGENTS.md — marchant-lab-web

Sitio web público del laboratorio, no es un análisis: no aplican scripts numerados ni `data/`/`results/`.

- Contenido solo en `_data/*.yml`; las páginas viven en `_includes/paginas/` y `index.html`, `*.html` y `en/*.html`
  son envoltorios. Todo texto nuevo en español necesita su traducción en `_data/traduccion_en.yml`
  (`python scripts/revisar_traducciones.py` debe salir sin faltantes).
- Todo lo que se publique aquí es **público**: no poner datos sin publicar, códigos de estudiante,
  correos personales ni nombres de personas que no hayan aceptado aparecer.
- Antes de commitear: `jekyll build` sin errores y revisar `python scripts/capturas.py` (capturas en /tmp/capturas) en el entorno conda `marchant-lab-web`.
- Commits en español, imperativo (`contenido: agrega egresado X`, `diseño: …`).
- Todo texto libre se muestra con `{% include cursiva.html t=... %}` (nombres científicos en cursiva);
  `python scripts/revisar_cursivas.py` debe salir sin problemas.

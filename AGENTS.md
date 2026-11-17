# AGENTS.md — marchant-lab-web

Sitio web público del laboratorio, no es un análisis: no aplican scripts numerados ni `data/`/`results/`.

- Contenido solo en `_data/*.yml`; las páginas (`*.md`) y `_layouts/` solo leen esos datos.
- Todo lo que se publique aquí es **público**: no poner datos sin publicar, códigos de estudiante,
  correos personales ni nombres de personas que no hayan aceptado aparecer.
- Antes de commitear: `jekyll build` sin errores en el entorno conda `marchant-lab-web`.
- Commits en español, imperativo (`contenido: agrega egresado X`, `diseño: …`).

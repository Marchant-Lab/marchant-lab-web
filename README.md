# marchant-lab-web

Página web del Marchant Lab (UIS). Sitio estático hecho con [Jekyll](https://jekyllrb.com/).

## Actualizar contenidos

Todo el contenido está en `_data/`. Se edita el YAML, se hace commit y push, y el sitio se reconstruye solo.

| Qué cambiar | Archivo | Clave |
|---|---|---|
| Líneas de investigación | `_data/lineas.yml` | `nombre`, `descripcion` |
| Proyectos actuales / pasados | `_data/proyectos.yml` | `estado: actual` o `estado: pasado` |
| Estudiantes actuales / egresados | `_data/personas.yml` | `estado: actual` o `estado: egresado` (+ `anio`) |
| Perfil del investigador (bio, formación, foto) | `_data/investigador.yml` | |
| Tesis de egresados (título y resumen) | `_data/tesis.json` | se regenera con `python3 scripts/actualizar_tesis.py` (lee Noesis); se enlaza con `noesis:` en `personas.yml` |
| Publicaciones | `_data/publicaciones.json` | se regenera con `python3 scripts/actualizar_publicaciones.py` (lee ORCID) |
| Cómo vincularse | `_data/vinculacion.yml` y `vinculate.md` | |
| Correo, título, descripción | `_config.yml` | `contacto`, `title`, `description` |

- Cuando alguien se gradúa: cambiar `estado: actual` → `estado: egresado` y agregar `anio: 2026`.
- Cuando un proyecto termina: cambiar `estado: actual` → `estado: pasado`.
- Fotos: guardarlas en `assets/fotos/` y poner `foto: /assets/fotos/nombre.jpg`.

## Vista previa local

```bash
conda activate marchant-lab-web
jekyll serve        # abre http://localhost:4000
```

## Publicación

Publicado con GitHub Pages desde la rama `main`: https://marchant-lab.github.io/marchant-lab-web/
Cada push a `main` reconstruye el sitio en 1–2 minutos.

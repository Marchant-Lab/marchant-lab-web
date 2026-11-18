# marchant-lab-web

Página web del Marchant Lab (UIS). Sitio estático hecho con [Jekyll](https://jekyllrb.com/).

## Actualizar contenidos

Todo el contenido está en `_data/`. Se edita el YAML, se hace commit y push, y el sitio se reconstruye solo.

| Qué cambiar | Archivo | Clave |
|---|---|---|
| Noticias (portada muestra las 3 más recientes) | `_data/noticias.yml` | más reciente arriba; `fecha`, `categoria`, `titulo`, `texto`, `enlace`, `foto` opcional |
| Líneas de investigación | `_data/lineas.yml` | `nombre`, `descripcion` |
| Proyectos actuales / pasados | `_data/proyectos.yml` | `estado: actual` o `estado: pasado` |
| Estudiantes actuales / egresados | `_data/personas.yml` | `estado: actual` o `estado: egresado` (+ `anio`) |
| Perfil del investigador (bio, formación, foto) | `_data/investigador.yml` | |
| Tesis de egresados (título y resumen) | `_data/tesis.json` | se regenera con `python3 scripts/actualizar_tesis.py` (lee Noesis); se enlaza con `noesis:` en `personas.yml` |
| Publicaciones que no están en ORCID | `_data/publicaciones_extra.yml` | se suman a la lista de ORCID |
| Publicaciones | `_data/publicaciones.json` | se regenera con `python3 scripts/actualizar_publicaciones.py` (lee ORCID) |
| Congresos (ponencias y pósteres) | `_data/congresos.yml` | `ambito: internacional` o `nacional`; países se traducen en `traduccion_en.yml` |
| Infraestructura (portada) | `_data/infraestructura.yml` | sede, espacios y equipos del iBGA en Guatiguará; sin números de inventario |
| Galerías de fotos (portada, investigador, equipo) | `_data/galeria.yml` + `assets/fotos/` | `pagina: inicio` (grupos y campo), `investigador` o `equipo`; quitar metadatos y GPS a las fotos antes de subirlas |
| Docencia (cursos, diplomados, divulgación) | `_data/docencia.yml` | |
| Cómo vincularse | `_data/vinculacion.yml` y `vinculate.md` | |
| Correo, título, descripción | `_config.yml` | `contacto`, `title`, `description` |

### Nombres científicos en cursiva

Los géneros y especies listados en `_data/especies.yml` se ponen en cursiva solos en todo el sitio
(también en títulos y resúmenes que vienen de ORCID y Noesis). Si un texto nuevo trae una especie que
no está en la lista, agregarla ahí. `python scripts/revisar_cursivas.py` (tras `jekyll build`) revisa el resultado.

### Versión en inglés

El sitio tiene una versión en inglés en `/en/` (botón **EN/ES** en la barra). Los datos son los mismos:

- Textos de la interfaz (menú, títulos, botones): `_data/ui.yml`, secciones `es` y `en`.
- Contenido (proyectos, líneas, bio, roles, docencia…): `_data/traduccion_en.yml`, con el formato
  `"texto exacto en español": "English text"`. Si un texto no está ahí, la versión en inglés lo muestra en español.
- Después de agregar o cambiar contenido, correr `python scripts/revisar_traducciones.py`: lista lo que falta traducir.
- Resúmenes de tesis en inglés: vienen de Noesis con `scripts/actualizar_tesis.py`.
- Títulos de tesis y publicaciones no se traducen.

- Cuando alguien se gradúa: cambiar `estado: actual` → `estado: egresado` y agregar `anio: 2026`.
- Cuando un proyecto termina: cambiar `estado: actual` → `estado: pasado`.
- Fotos: guardarlas en `assets/fotos/` y poner `foto: /assets/fotos/nombre.jpg`.

## Vista previa local

```bash
conda activate marchant-lab-web
jekyll serve        # abre http://localhost:4000
python scripts/capturas.py   # capturas de todas las páginas (escritorio y celular) en /tmp/capturas
```

## Publicación

Publicado con GitHub Pages desde la rama `main`: https://marchant-lab.github.io/marchant-lab-web/
Cada push a `main` reconstruye el sitio en 1–2 minutos.

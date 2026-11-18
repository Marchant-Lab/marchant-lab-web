"""Lista los textos de _data/ que no tienen traducción en _data/traduccion_en.yml, y las
traducciones que ya no corresponden a ningún texto (porque el español cambió).

Uso (desde la raíz, entorno conda marchant-lab-web): python scripts/revisar_traducciones.py
Sale con código 1 si falta algo.
"""
import re
import sys
import yaml

def cargar(nombre):
    with open(f"_data/{nombre}.yml", encoding="utf-8") as f:
        return yaml.safe_load(f)

def textos(items, campos):
    for it in items:
        for c in campos:
            v = it.get(c)
            for x in (v if isinstance(v, list) else [v]):
                if isinstance(x, str) and re.search(r"[A-Za-zÁÉÍÓÚáéíóúñÑ]", x):
                    yield x

inv = cargar("investigador")
doc = cargar("docencia")
usados = set()
usados |= set(textos(cargar("lineas"), ["nombre", "descripcion"]))
usados |= set(textos(cargar("proyectos"), ["titulo", "descripcion", "rol", "socios", "financiador"]))
usados |= set(textos(cargar("personas"), ["rol", "modalidad"]))
usados |= set(textos(cargar("vinculacion"), ["modalidad", "detalle"]))
usados |= set(textos(cargar("congresos"), ["pais"]))
usados |= set(textos(cargar("noticias"), ["titulo", "texto"]))
usados |= set(textos(cargar("galeria"), ["pie"]))
infra = cargar("infraestructura")
usados |= set(textos([infra], ["sede", "espacios"])) | set(textos(infra["grupos"], ["nombre", "equipos"]))
usados |= set(textos([inv], ["cargo", "categoria", "grupo", "bio", "formacion", "trayectoria", "distinciones"]))
for seccion in doc.values():
    usados |= set(textos(seccion, ["nombre", "nivel", "periodos", "descripcion"]))

traducidos = set(cargar("traduccion_en"))
# En YAML de una línea ({titulo: ..., subtitulo: ...}) una coma sin comillas corta el texto.
cortados = [f"{l}/{k}" for l, v in cargar("ui").items() for k, x in v["paginas"].items()
            if x.get("subtitulo") and not x["subtitulo"].endswith(".")]
for c in cortados:
    print("CORTADO: subtítulo de", c, "(¿coma sin comillas en _data/ui.yml?)")
faltan, sobran = sorted(usados - traducidos), sorted(traducidos - usados)
for t in faltan:
    print("FALTA :", t)
for t in sobran:
    print("SOBRA :", t)
print(f"{len(usados)} textos, {len(faltan)} sin traducir, {len(sobran)} traducciones sin uso")
sys.exit(1 if faltan or cortados else 0)

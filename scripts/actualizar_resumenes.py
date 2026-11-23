"""Busca en OpenAlex el resumen y el enlace de acceso abierto de cada DOI de _data/publicaciones.json
y _data/publicaciones_extra.yml, y escribe _data/resumenes.json (clave = DOI en minúsculas).
Las traducciones de los resúmenes se escriben a mano en _data/resumenes_traduccion.yml.

Uso (desde la raíz, entorno conda marchant-lab-web; correr después de actualizar_publicaciones.py):
    python scripts/actualizar_resumenes.py
"""
import json
import re
import urllib.parse
import urllib.request

import yaml

# Palabras que OpenAlex pega donde la revista tenía cursivas (mismo enfoque que actualizar_tesis.py).
CORRECCIONES = {
    "nematode,Trichodorus": "nematode, Trichodorus", "Florida,T. obtususcauses": "Florida, T. obtusus causes",
    "ofT. obtususwere": "of T. obtusus were", "genusTrichodorus": "genus Trichodorus",
    "barnaclePollicipes elegansfrom": "barnacle Pollicipes elegans from", "ofP. elegansfrom": "of P. elegans from",
    "duringENSOevents": "during ENSO events",
}


def corregir(texto):
    for mal, bien in CORRECCIONES.items():
        texto = texto.replace(mal, bien)
    return re.sub(r" ([.,])(?=\s|$)", r"\1", texto)  # espacio que queda tras una cursiva: "Symphylella ."


def openalex(doi):
    url = "https://api.openalex.org/works/doi:" + urllib.parse.quote(doi, safe="/")
    w = json.load(urllib.request.urlopen(url, timeout=30))
    inv = w.get("abstract_inverted_index") or {}
    resumen = " ".join(p for _, p in sorted((i, p) for p, pos in inv.items() for i in pos))
    if resumen.endswith("[...]"):  # a veces OpenAlex solo tiene la primera frase
        resumen = ""
    oa = w.get("open_access") or {}
    locs = [w.get("best_oa_location") or {}] + [l for l in w.get("locations", []) if l.get("is_oa")]
    return {
        "resumen": corregir(" ".join(resumen.split())) or None,
        "idioma": w.get("language"),
        "pdf": next((l["pdf_url"] for l in locs if l.get("pdf_url")), None),
        # verde = copia en un repositorio; esos enlaces suelen estar caídos, solo se marca lo libre en la revista
        "abierto": oa.get("oa_status") in ("diamond", "gold", "hybrid", "bronze"),
    }


pubs = json.load(open("_data/publicaciones.json", encoding="utf-8"))
pubs += yaml.safe_load(open("_data/publicaciones_extra.yml", encoding="utf-8"))
dois = sorted({p["doi"].lower() for p in pubs if p.get("doi")})
resumenes = {d: openalex(d) for d in dois}
assert any(r["resumen"] for r in resumenes.values()), "OpenAlex no devolvió resúmenes"

with open("_data/resumenes.json", "w", encoding="utf-8") as f:
    json.dump(resumenes, f, ensure_ascii=False, indent=1)
con = lambda k: sum(1 for r in resumenes.values() if r[k])
print(f"{len(dois)} DOI en _data/resumenes.json: {con('resumen')} con resumen, {con('pdf')} con PDF libre")

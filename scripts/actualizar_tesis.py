"""Descarga de Noesis (repositorio UIS) las tesis dirigidas o codirigidas por Sergio Marchant
y escribe _data/tesis.json. equipo.md las une a los egresados por el campo `noesis` (handle).

Uso (desde la raíz del repo): python3 scripts/actualizar_tesis.py
"""
import json
import urllib.parse
import urllib.request

API = "https://noesis.uis.edu.co/server/api/discover/search/objects"

def valor(meta, campo):
    v = meta.get(campo)
    return " ".join(v[0]["value"].split()) if v else None

# Erratas de Noesis en nombres científicos (género con mayúscula, epíteto bien escrito, autor con mayúscula).
CORRECCIONES = {
    "elaeis oleifera (kunth) cortes": "Elaeis oleifera (Kunth) Cortés",
    "Astaena pygidialis kirsch": "Astaena pygidialis Kirsch",
    "A. pygydialis": "A. pygidialis",
    "A. pyidialis": "A. pygidialis",
}

def corregir(texto):
    for mal, bien in CORRECCIONES.items():
        texto = texto.replace(mal, bien) if texto else texto
    return texto

tesis, pagina = [], 0
while True:
    url = API + "?" + urllib.parse.urlencode(
        {"query": "Marchant", "dsoType": "ITEM", "size": 100, "page": pagina})
    res = json.load(urllib.request.urlopen(url, timeout=60))["_embedded"]["searchResult"]
    for o in res["_embedded"]["objects"]:
        it = o["_embedded"]["indexableObject"]
        m = it["metadata"]
        directores = [x["value"] for x in m.get("dc.contributor.advisor", [])]
        if not any("Marchant" in d for d in directores):  # la búsqueda es de texto completo
            continue
        tesis.append({
            "handle": it["handle"],
            "titulo": corregir(valor(m, "dc.title")),
            "autor": valor(m, "dc.contributor.author"),
            "anio": int(valor(m, "dc.date.issued")[:4]),
            "grado": valor(m, "dc.description.degreename"),
            "directores": directores,
            "resumen": corregir(valor(m, "dc.description.abstract")),
            "resumen_en": corregir(valor(m, "dc.description.abstractenglish")),
        })
    pagina += 1
    if pagina >= res["page"]["totalPages"]:
        break

tesis.sort(key=lambda t: (-t["anio"], t["autor"]))
assert tesis and all(t["titulo"] and t["anio"] for t in tesis), "Noesis no devolvió tesis válidas"
with open("_data/tesis.json", "w", encoding="utf-8") as f:
    json.dump(tesis, f, ensure_ascii=False, indent=1)
print(f"{len(tesis)} tesis escritas en _data/tesis.json")

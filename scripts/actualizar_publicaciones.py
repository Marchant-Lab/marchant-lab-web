"""Descarga las publicaciones del ORCID público y escribe _data/publicaciones.json.

Uso (desde la raíz del repo): python3 scripts/actualizar_publicaciones.py
"""
import json
import urllib.request

ORCID = "0000-0002-7362-3626"
TIPOS = {"journal-article": "Artículo", "book": "Libro", "book-chapter": "Capítulo",
         "conference-proceedings": "Memorias de congreso", "conference-paper": "Ponencia"}

req = urllib.request.Request(f"https://pub.orcid.org/v3.0/{ORCID}/works",
                             headers={"Accept": "application/json"})
grupos = json.load(urllib.request.urlopen(req, timeout=30))["group"]

pubs = []
for g in grupos:
    w = g["work-summary"][0]  # ORCID ordena primero la versión preferida
    ids = (w.get("external-ids") or {}).get("external-id", [])
    doi = next((i["external-id-value"] for i in ids if i["external-id-type"] == "doi"), None)
    pubs.append({
        "anio": int(((w.get("publication-date") or {}).get("year") or {}).get("value") or 0),
        "titulo": w["title"]["title"]["value"],
        "revista": (w.get("journal-title") or {}).get("value"),
        "tipo": TIPOS.get(w["type"], w["type"]),
        "doi": doi,
    })
pubs.sort(key=lambda p: -p["anio"])
assert pubs and all(p["titulo"] for p in pubs), "ORCID no devolvió publicaciones válidas"

with open("_data/publicaciones.json", "w", encoding="utf-8") as f:
    json.dump(pubs, f, ensure_ascii=False, indent=1)
print(f"{len(pubs)} publicaciones escritas en _data/publicaciones.json")

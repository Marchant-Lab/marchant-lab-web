"""Revisa en el sitio generado (_site/) que los nombres de _data/especies.yml estén en cursiva
y que no haya cursivas anidadas. Detecta textos que se muestran sin pasar por _includes/cursiva.html.

Uso (desde la raíz, tras `jekyll build`, entorno conda marchant-lab-web): python scripts/revisar_cursivas.py
Sale con código 1 si encuentra problemas.
"""
import glob
import re
import sys
import yaml

esp = yaml.safe_load(open("_data/especies.yml", encoding="utf-8"))
problemas = 0
for f in glob.glob("_site/**/*.html", recursive=True):
    s = open(f, encoding="utf-8").read()
    s = re.sub(r"<(head|script|style)[\s\S]*?</\1>", "", s)
    s = re.sub(r'\s(href|content|alt|title)="[^"]*"', "", s)  # atributos: no se muestran como texto
    if re.search(r"<em>[^<]*<em>", s):
        print("ANIDADO      :", f)
        problemas += 1
    for g in esp["generos"]:
        for m in re.finditer(r"(?<!<em>)\b" + g + r"\b", s):
            print("SIN CURSIVA  :", f, "|", s[max(0, m.start() - 40):m.end() + 30].replace("\n", " "))
            problemas += 1
    for g in esp["generos"]:  # género escrito en minúscula (p. ej. "elaeis oleifera")
        for m in re.finditer(r"(?<![\w/])" + g.lower() + r"\s+[a-z]{4,}", s):
            print("MINÚSCULA    :", f, "|", m.group(0))
            problemas += 1
    for e in esp.get("cf", []):
        if f"cf. {e}" in s:
            print("CF SIN CURSIVA:", f, "|", e)
            problemas += 1
    for e in esp["especies"]:
        g, resto = e.split(" ", 1)
        if f"<em>{g}</em> {resto}" in s:
            print("EPÍTETO FUERA:", f, "|", e)
            problemas += 1
print(f"{problemas} problemas")
sys.exit(1 if problemas else 0)

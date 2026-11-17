---
layout: default
title: Publicaciones
permalink: /publicaciones/
---
# Publicaciones

Lista generada desde [ORCID](https://orcid.org/0000-0002-7362-3626).

{% assign por_anio = site.data.publicaciones | group_by: "anio" %}
{% for g in por_anio %}
## {{ g.name }}
{% for p in g.items %}
- {% if p.doi %}[{{ p.titulo }}](https://doi.org/{{ p.doi }}){% else %}{{ p.titulo }}{% endif %}{% if p.revista %}. *{{ p.revista }}*{% endif %}. {{ p.tipo }}.{% endfor %}
{% endfor %}

---
layout: default
title: Proyectos
permalink: /proyectos/
---
{% assign grupos = "actual:Proyectos actuales,pasado:Proyectos pasados" | split: "," %}
{% for g in grupos %}{% assign par = g | split: ":" %}
## {{ par[1] }}
{% for p in site.data.proyectos %}{% if p.estado == par[0] %}
### {{ p.titulo }}{% if p.anios %} <small>({{ p.anios }})</small>{% endif %}
{{ p.descripcion }}{% if p.socios %} *Socios: {{ p.socios }}.*{% endif %}
{% endif %}{% endfor %}
{% endfor %}

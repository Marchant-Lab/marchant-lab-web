---
layout: default
title: Docencia
permalink: /docencia/
---
# Docencia
{% assign d = site.data.docencia %}
{% assign secciones = "cursos:Cursos en la UIS,formacion_continua:Formación continua,divulgacion:Divulgación y museo" | split: "," %}
{% for s in secciones %}{% assign par = s | split: ":" %}
## {{ par[1] }}
{% assign clave = par[0] %}{% for c in d[clave] %}
### {% if c.url %}[{{ c.nombre }}]({{ c.url }}){% else %}{{ c.nombre }}{% endif %}{% if c.codigo %} <small>({{ c.codigo }})</small>{% endif %}
{% if c.nivel or c.periodos %}*{{ c.nivel }}{% if c.nivel and c.periodos %} · {% endif %}{{ c.periodos }}*{% endif %}

{{ c.descripcion }}
{% endfor %}
{% endfor %}

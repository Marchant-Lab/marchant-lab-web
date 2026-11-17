---
layout: default
title: Vincúlate
permalink: /vinculate/
---
# Vincúlate al laboratorio

{% for v in site.data.vinculacion %}
### {{ v.modalidad }}
{{ v.detalle }}
{% endfor %}

## ¿Cómo aplicar?

Escribe a **{{ site.contacto }}** con tu hoja de vida, la línea de investigación que te interesa y tu disponibilidad.

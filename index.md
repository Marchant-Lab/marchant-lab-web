---
layout: default
---
# {{ site.title }}

{{ site.description }}.

## Líneas de investigación

{% for l in site.data.lineas %}
### {{ l.nombre }}
{{ l.descripcion }}
{% endfor %}

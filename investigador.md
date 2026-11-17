---
layout: default
title: Investigador
permalink: /investigador/
---
{% assign i = site.data.investigador %}
# {{ i.nombre }}
{% if i.foto != "" %}<img class="retrato" src="{{ i.foto | relative_url }}" alt="{{ i.nombre }}">{% endif %}
**{{ i.cargo }}**<br>{{ i.categoria }}<br>{{ i.grupo }}

{% for p in i.bio %}
{{ p }}
{% endfor %}

## Formación
{% for f in i.formacion %}
- {{ f }}{% endfor %}

## Trayectoria
{% for t in i.trayectoria %}
- {{ t }}{% endfor %}

## Perfiles
{% for p in i.perfiles %}[{{ p.nombre }}]({{ p.url }}){% unless forloop.last %} · {% endunless %}{% endfor %}

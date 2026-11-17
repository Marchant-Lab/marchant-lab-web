---
layout: default
title: Equipo
permalink: /equipo/
---
{% assign grupos = "actual:Integrantes actuales,egresado:Egresados" | split: "," %}
{% for g in grupos %}{% assign par = g | split: ":" %}
## {{ par[1] }}
<div class="tarjetas">
{% for p in site.data.personas %}{% if p.estado == par[0] %}
  <div class="tarjeta">
    {% if p.foto %}<img src="{{ p.foto | relative_url }}" alt="{{ p.nombre }}">{% endif %}
    <strong>{% if p.enlace %}<a href="{{ p.enlace }}">{{ p.nombre }}</a>{% else %}{{ p.nombre }}{% endif %}</strong>
    <span>{{ p.rol }}{% if p.anio %} · {{ p.anio }}{% endif %}</span>
    {% if p.tesis %}<em>{{ p.tesis }}</em>{% endif %}
  </div>
{% endif %}{% endfor %}
</div>
{% endfor %}

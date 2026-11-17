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
    {% if p.noesis %}{% assign t = site.data.tesis | where: "handle", p.noesis | first %}
    <a href="https://noesis.uis.edu.co/handle/{{ t.handle }}"><em>{{ t.titulo }}</em></a>
    {% if t.resumen %}<details><summary>Resumen</summary><p>{{ t.resumen }}</p></details>{% endif %}
    {% elsif p.tesis %}<em>{{ p.tesis }}</em>{% endif %}
  </div>
{% endif %}{% endfor %}
</div>
{% endfor %}

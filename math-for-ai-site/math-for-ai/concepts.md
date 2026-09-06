---
layout: page
title: Concepts
permalink: /concepts/
---

Short entries, one per mathematical idea, in the style of [Algebrica](https://github.com/antoniolupetti/algebrica): a definition, the essential result, then where it shows up in an AI system. Copy `concepts/_template.md` to start a new one.

{% assign entries = site.pages | where: "kind", "concept" | sort: "title" %}
{% for c in entries %}
- [{{ c.title }}]({{ c.url | relative_url }}) — {{ c.summary }}
{% endfor %}

---
layout: page
title: Schedule
permalink: /schedule/
---

One page per week. Each lists the chapters to read (Core / Skim / Optional), where that mathematics appears in an AI system, and a Friday build exercise.

{% assign weeks = site.pages | where: "kind", "week" | sort: "week" %}
{% for w in weeks %}
- **Week {{ w.week }}** ({{ w.dates }}) — [{{ w.title }}]({{ w.url | relative_url }})
{% endfor %}

A standalone version with per-week checkboxes: [assets/math-for-ai-13-week-schedule.html]({{ '/assets/math-for-ai-13-week-schedule.html' | relative_url }}).

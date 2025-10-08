---
layout: page
title: Projects
permalink: /projects/
description: "A showcase of my development projects and experiments"
---

Here are some of the projects I've worked on. This collection includes both personal experiments and professional work.

{% for project in site.projects %}
  {% if project.featured %}
## [{{ project.title }}]({{ project.live_url }})

{{ project.description }}

**Technologies:** {{ project.technologies | join: ', ' }}

{% if project.github %}
[View on GitHub]({{ project.github }}) | 
{% endif %}
[Live Demo]({{ project.live_url }})

---
  {% endif %}
{% endfor %}

## All Projects

{% for project in site.projects %}
- **[{{ project.title }}]({{ project.url }})** - {{ project.description }}
{% endfor %}

*More projects coming soon! Have a project idea you'd like to collaborate on? [Get in touch](mailto:rlee@tokyo3.com)!*

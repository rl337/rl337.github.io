---
layout: page
title: Projects
permalink: /projects/
description: "Projects with documentation and other things to explore."
---

A selection of projects, with links to their published sites and source code.
Related Substack writing is linked where available.

<div class="project-grid">
{% assign featured_projects = site.data.projects | where: "featured", true %}
{% for project in featured_projects %}
<article class="project-card">
  <p class="eyebrow">{{ project.kind | escape }}</p>
  <h2><a href="{{ project.site_url | relative_url | escape }}">{{ project.title | escape }}</a></h2>
  <p>{{ project.description | escape }}</p>
  <ul class="project-links">
    <li><a href="{{ project.site_url | relative_url | escape }}">{{ project.site_label | escape }}</a></li>
    {% if project.repository %}<li><a href="{{ project.repository | escape }}">Source code</a></li>{% endif %}
    {% for tag in project.substack_tags %}
    <li><a href="{{ tag.url | escape }}">Substack: {{ tag.title | escape }}</a></li>
    {% endfor %}
    {% for post in project.substack_posts %}
    <li><a href="{{ post.url | escape }}">{{ post.title | escape }} · Substack</a></li>
    {% endfor %}
  </ul>
</article>
{% endfor %}
</div>

## More published sites

Other project sites, demos, and collections you can visit.

<ul class="project-preview">
{% assign other_projects = site.data.projects | where: "featured", false %}
{% for project in other_projects %}
<li><a href="{{ project.site_url | relative_url | escape }}">{{ project.title | escape }}</a>
<span>{{ project.summary | escape }}</span></li>
{% endfor %}
</ul>

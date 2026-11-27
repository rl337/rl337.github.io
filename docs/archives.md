---
layout: page
title: Archive
permalink: /archives/
description: "The original blog, and writing since."
---

The original rl337.org posts from 2011–2014 were recovered from the Wayback Machine.
They keep their original dates and addresses. Each restored post links to its source
capture; recovery notes identify missing media where known.

## Explore a subject

<nav class="topic-list" aria-label="Archive subjects">
  <a href="{{ '/categories/submediant/' | relative_url }}">Submediant</a>
  <a href="{{ '/categories/littlerobots/' | relative_url }}">Little Robots</a>
  <a href="{{ '/tags/blender/' | relative_url }}">Blender</a>
  <a href="{{ '/tags/arduino/' | relative_url }}">Arduino</a>
</nav>

## Browse by year

{% assign years = site.posts | group_by_exp: "post", "post.date | date: '%Y'" %}
<nav class="year-list" aria-label="Archive years">
{% for year in years %}
<a href="#year-{{ year.name }}">{{ year.name }}</a>
{% endfor %}
</nav>
{% for year in years %}
<section class="archive-year" aria-labelledby="year-{{ year.name }}">
<h2 id="year-{{ year.name }}">{{ year.name }}</h2>
<ul class="archive-list">
{% for post in year.items %}
  <li><time datetime="{{ post.date | date: '%Y-%m-%d' }}">{{ post.date | date: "%b %-d" }}</time>
    <a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a></li>
{% endfor %}
</ul>
</section>
{% endfor %}

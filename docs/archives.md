---
layout: page
title: Archives
permalink: /archives/
description: "Browse Richard Lee's current posts and the restored WordPress archive."
---

This archive brings back posts from the original rl337.org blog, from 2011 to 2014. Each restored post
keeps its original date and address and links to its Wayback Machine capture. Some old downloads
and embeds were not preserved.

Start with [Submediant](/categories/submediant/), [Little Robots](/categories/littlerobots/),
[Blender](/tags/blender/), or [Arduino](/tags/arduino/), or browse by year below.

{% assign years = site.posts | group_by_exp: "post", "post.date | date: '%Y'" %}
{% for year in years %}
<h2 id="year-{{ year.name }}">{{ year.name }}</h2>
<ul>
{% for post in year.items %}
  <li><time datetime="{{ post.date | date: '%Y-%m-%d' }}">{{ post.date | date: "%b %-d" }}</time>
    <a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a></li>
{% endfor %}
</ul>
{% endfor %}

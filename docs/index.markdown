---
layout: home
title: Welcome
description: "Richard's blog - where technology meets creativity"
---

# Welcome to rl337.org

Hey there! I'm Richard, and this is my digital space where I share thoughts on technology, development, and the occasional random idea that pops into my head.

## Featured Projects

Here are my most active and interesting projects:

{% assign featured_projects = site.projects | where: "featured", true | limit: 5 %}
{% for project in featured_projects %}
### [{{ project.title }}]({{ project.github }})
{{ project.description }}

**Tech:** {{ project.technologies | join: ', ' }} | **Status:** {{ project.activity_level | replace: '_', ' ' | capitalize }} | **⭐ {{ project.stars }}**

{% endfor %}

[View all projects →](/projects/)

## Latest Posts

Check out my most recent thoughts and projects below, or browse through the [archives](/archives/) to see everything I've written.

## What I'm About

- **Building things** that solve real problems
- **Learning continuously** and sharing what I discover
- **Exploring** the intersection of technology and creativity
- **Connecting** with fellow developers and tech enthusiasts

Want to know more? Check out my [about page](/about/) or get in touch via [email](mailto:rlee@tokyo3.com) or [Twitter](https://twitter.com/rl337).

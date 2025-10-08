---
layout: page
title: Projects
permalink: /projects/
description: "A showcase of my development projects and experiments"
---

Here are the projects I've worked on, automatically analyzed from my GitHub repositories. Projects are ranked by activity level, from most active to archived.

## 🔥 Very Active Projects

{% assign very_active = site.projects | where: "activity_level", "very_active" %}
{% for project in very_active %}
### [{{ project.title }}]({{ project.url }})

{{ project.description }}

**Technologies:** {{ project.technologies | join: ', ' }}  
**Status:** 🔥 Very Active | ⭐ {{ project.stars }} stars | 🍴 {{ project.forks }} forks  
**Last Updated:** {{ project.last_updated }}

{% if project.github %}[View on GitHub]({{ project.github }}){% endif %}{% if project.live_url %} | [Live Demo]({{ project.live_url }}){% endif %}

---
{% endfor %}

## ⚡ Active Projects

{% assign active = site.projects | where: "activity_level", "active" %}
{% for project in active %}
### [{{ project.title }}]({{ project.url }})

{{ project.description }}

**Technologies:** {{ project.technologies | join: ', ' }}  
**Status:** ⚡ Active | ⭐ {{ project.stars }} stars | 🍴 {{ project.forks }} forks  
**Last Updated:** {{ project.last_updated }}

{% if project.github %}[View on GitHub]({{ project.github }}){% endif %}{% if project.live_url %} | [Live Demo]({{ project.live_url }}){% endif %}

---
{% endfor %}

## 📈 Moderate Activity

{% assign moderate = site.projects | where: "activity_level", "moderate" %}
{% for project in moderate %}
- **[{{ project.title }}]({{ project.url }})** - {{ project.description }} (⭐ {{ project.stars }})
{% endfor %}

## 📉 Low Activity

{% assign low = site.projects | where: "activity_level", "low" %}
{% for project in low %}
- **[{{ project.title }}]({{ project.url }})** - {{ project.description }} (⭐ {{ project.stars }})
{% endfor %}

## 😴 Idle Projects

{% assign idle = site.projects | where: "activity_level", "idle" %}
{% for project in idle %}
- **[{{ project.title }}]({{ project.url }})** - {{ project.description }} (⭐ {{ project.stars }})
{% endfor %}

## 📦 Archived Projects

{% assign archived = site.projects | where: "activity_level", "archived" %}
{% for project in archived %}
- **[{{ project.title }}]({{ project.url }})** - {{ project.description }} (⭐ {{ project.stars }})
{% endfor %}

---

## Project Statistics

- **Total Projects:** {{ site.projects.size }}
- **Very Active:** {{ very_active.size }}
- **Active:** {{ active.size }}
- **Moderate:** {{ moderate.size }}
- **Low Activity:** {{ low.size }}
- **Idle:** {{ idle.size }}
- **Archived:** {{ archived.size }}

*This page is automatically updated from my GitHub repositories. Have a project idea you'd like to collaborate on? [Get in touch](mailto:rlee@tokyo3.com)!*

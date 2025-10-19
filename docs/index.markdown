---
layout: home
title: Welcome
description: "Richard's blog - where technology meets creativity"
---

# Welcome to rl337.org

Hey there! I'm Richard, and this is my digital space where I share thoughts on technology, development, and the occasional random idea that pops into my head.

<div class="sugar-glider-hero">
  <img src="{{ '/assets/images/sugar-gliders/sugar-glider-hero.png' | relative_url }}" 
       alt="Sugar Glider in Digital Landscape" 
       class="hero-image">
  <p><em>Meet my digital companion - always ready to explore the world of code and creativity! 🦎</em></p>
</div>

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

## Meet My Mascot 🦎🍓

You might have noticed the little sugar glider in my header - that's my unofficial logo! Just like Scrat from Ice Age is obsessed with his acorn, my sugar glider is completely fixated on strawberries. It represents my approach to coding: that same single-minded determination and passion for solving problems, even when they seem impossible (or deliciously out of reach).

The strawberry obsession? Well, sometimes the best solutions come from being a little bit obsessed with the things you love! 🍓

## What I'm About

- **Building things** that solve real problems
- **Learning continuously** and sharing what I discover
- **Exploring** the intersection of technology and creativity
- **Connecting** with fellow developers and tech enthusiasts

Want to know more? Check out my [about page](/about/) or get in touch via [email](mailto:rlee@tokyo3.com) or [Twitter](https://twitter.com/rl337).

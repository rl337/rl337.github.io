---
layout: post
title: "Metro: giving a city more than a grid"
date: 2025-01-15 13:00:00 -0500
categories: [projects, python, simulation, visualization]
tags: [python, simulation, matplotlib, demographics, visualization, urban-planning]
author: Richard Lee
permalink: /projects/python/simulation/visualization/2025/01/15/metro-metropolitan-simulation-framework.html
last_modified_at: 2026-11-27
---

<p class="post-meta">Revised November 27, 2026.</p>

When I was working on Project Mars, I wanted the population of the city to affect
the story. In [Martian Census Data]({{ '/2011/09/20/martian-census-data/' | relative_url }}),
I used a population model to explore the relationship between people born on
Earth and people born on Mars. The numbers were a way to get at the culture.

The layout raised a related question. In
[Naive City Planning]({{ '/2011/09/22/naive-city-planning/' | relative_url }}),
I worked backwards from the larger city to its first settlement. What would it
need, how much space would those things take, and how would the buildings affect
the people living in them?

<figure class="post-illustration">
  <img src="{{ '/assets/images/blog/metro-city-simulation.webp' | relative_url }}"
       alt="A crow overlooking a miniature city of paper and wooden blocks."
       width="1280" height="720" loading="eager" decoding="async">
  <figcaption>
    Crow illustration of exploring city layouts. Generated with Qwen-Image 2.1.
  </figcaption>
</figure>

[Metro](https://github.com/rl337/metro) has tools for two different parts of this
kind of experiment. There are geometric shapes and a renderer for putting things
on the page. There are also population-modeling components for working with
demographic assumptions. Drawing a plausible arrangement and deciding what that
arrangement represents are separate problems.

<figure>
  <img src="{{ '/assets/images/legacy-blog/2011/09/town-layout.png.webp' | relative_url }}"
       alt="The initial Martian settlement sketch from Naive City Planning."
       width="480" height="480" loading="lazy" decoding="async">
  <figcaption>The initial settlement sketch from <em>Naive City Planning</em> (2011).</figcaption>
</figure>

A renderer can tell you where a rectangle goes and whether a point is inside a
circle. It can't tell you how much farmland a settlement needs. A population
model can produce a distribution, but the result still depends on assumptions
about migration, births, and who is being counted.

The geometry part can be quite small. Here a circular park contains the first
point, while the second lies outside it:

```python
from metro.model.point2d import Point2D
from metro.model.shapes.circle import Circle

park = Circle(Point2D(40, 40), radius=12)
print(park.contains(Point2D(45, 40)))
print(park.contains(Point2D(60, 40)))
```

Output:

```text
True
False
```

That answers a question about space. It says nothing yet about how many people
use the park or whether this city has enough parks.

Those assumptions were visible in the old posts, including the parts I hadn't
worked out. In the settlement sketch, I still needed to separate education from
administration and work out the food requirements. Getting a picture on the
screen made those questions easier to point at. It didn't answer them.

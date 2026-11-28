---
layout: post
title: "Curioshelf: when a folder isn't enough"
date: 2025-01-15 12:00:00 -0500
categories: [projects, tools, python, game-development]
tags: [asset-management, 2d-games, python, pyside6, game-development]
author: Richard Lee
permalink: /projects/tools/python/game-development/2025/01/15/curioshelf-visual-asset-manager.html
last_modified_at: 2026-11-27
---

<p class="post-meta">Revised November 27, 2026.</p>

Having a front view of a character doesn't mean you have a character ready for a
game. There might still be a back view to draw, several walking frames to finish,
and a production version to make from the concept art. A folder can hold all of
those pictures without telling you what's missing.

[Curioshelf](https://github.com/rl337/curioshelf) is an asset manager built around
that distinction. It keeps the source image, the part of that image being used,
and the object that needs it connected.

<figure class="post-illustration">
  <img src="{{ '/assets/images/blog/curioshelf-interface.webp' | relative_url }}"
       alt="A crow arranging small game assets in neatly divided drawers."
       width="1280" height="720" loading="eager" decoding="async">
  <figcaption>
    Crow illustration of organizing visual assets. Generated with Qwen-Image 2.1.
  </figcaption>
</figure>

The useful unit here is a named view of an object. A template might say that a
character needs `front`, `back`, and `walk1`. A slice identifies a rectangle in a
source image and gives it one of those names. The object brings those pieces
together, while the layer distinguishes concept, working, and production art.

That gives the tool a fairly specific question to answer: which required views
are still missing? The [data model](https://github.com/rl337/curioshelf/blob/577c121b362e2d2fdf77d4b392797fb642e6dbde/curioshelf/models.py)
has a `get_missing_views()` method that compares the names in a template with the
names of the available slices. It doesn't need to guess from filenames or count
everything in a directory.

For example, this object has a front view but still needs a back view:

```python
from curioshelf.models import CurioObject, ObjectSlice, Template

views = Template("character", "Required views", ["front", "back"])
crow = CurioObject(id="crow", name="Crow")
crow.slices.append(ObjectSlice("front", "sheet-1", 0, 0, 64, 64))

print(crow.get_missing_views(views))
```

Output:

```text
['back']
```

The source ID and rectangle describe the slice. For this check, its name is
what matters.

There's a limit to what that tells you, though. A view called `walk1` can exist
and still be a bad animation frame. The completeness check compares names; it
doesn't judge the drawing or whether the sequence moves properly. Those are
different kinds of work, and the metadata can only account for one of them.

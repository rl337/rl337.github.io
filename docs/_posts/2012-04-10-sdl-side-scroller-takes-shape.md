---
layout: post
title: SDL side scroller takes shape
date: '2012-04-10'
author: Richard Lee
permalink: /2012/04/10/sdl-side-scroller-takes-shape/
legacy_archive: true
archive_source: https://web.archive.org/web/20120414122454/http://rl337.org/2012/04/10/sdl-side-scroller-takes-shape/
archive_original_timestamp: '2012-04-10T16:32:43+00:00'
---

In my [previous
post](/2012/03/13/layers-of-detail-with-blitting-in-sdl/) on
[SDL](http://libsdl.org), I talked a little bit about layering bitmaps to create a simple [side
scroller](http://en.wikipedia.org/wiki/Side-scrolling_video_game).

Here, I’ve actually gotten bitmap layering to work.  I’ve used the rough bitmaps that I drew for the
last blog post and built some code around it.   I haven’t gotten to the point where I can built a
distributable binary yet, but I’m hoping that it won’t be too tough.  I’m hoping to NOT have to
involve [xcode](https://developer.apple.com/xcode/)… but all literature I’ve found on building apple
distributables seem to center around that tool.

Here’s a screenshot of the resulting app.  Doesn’t look very different from my mockup… but that’s
probably a good thing.

[![sdlfun-screenshot](/assets/images/legacy-blog/2012/04/sdlfun-screenshot.png.webp)](/assets/images/legacy-blog/2012/04/sdlfun-screenshot.png.webp)

The
way this ended up being implemented was through a Level class.  The Level class has an array of
Layers and a current position (x axis).  Each layer has a coefficient that describes its motion
relative to the Level’s x position. Foreground objects have a coefficient of \> 1 and objects
further in the background have coefficients less than one.

Each Layer has an array of LayerObjects. Each LayerObject which includes a bitmap and a coordinate.
They’re arranged in the Array in increasing order of x.

I captured the SDLK_LEFT and SDLK_RIGHT key events.  When SDLK_RIGHT is pushed, I’d increment the
level’s x position until the key was released.  Similarly for the SDLK_LEFT button except the
position is decremented.

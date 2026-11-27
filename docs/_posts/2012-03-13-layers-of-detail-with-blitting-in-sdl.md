---
layout: post
title: Layers of Detail with Blitting in SDL
date: '2012-03-13'
author: Richard Lee
permalink: /2012/03/13/layers-of-detail-with-blitting-in-sdl/
legacy_archive: true
archive_source: https://web.archive.org/web/20120315184832/http://rl337.org/2012/03/13/layers-of-detail-with-blitting-in-sdl/
archive_original_timestamp: '2012-03-13T16:07:45+00:00'
---

[![example-composite](/assets/images/legacy-blog/2012/03/example-composite-300x225.jpg.webp)](/assets/images/legacy-blog/2012/03/example-composite.jpg.webp)

Continuing
with [my
efforts](/2012/02/28/screw-this-noise-libsdl-to-the-rescue/)
to learn [SDL](http://libsdl.org), I’ve drawn kind of a silly set of bitmaps that will be sewn
together to form a landscape.

To the left you see a composite of 11 distinct images.  Each image falls into one of 4 layers,
Foreground, Middleground, Background, Clouds, and Horizon.

The point of having multiple layers is to simulate depth in a simple
[side-scrolle](http://en.wikipedia.org/wiki/Side-scrolling_video_game)r.  The “closer” the layer is
to the user, the faster it’ll slide across the screen.  In the case of the “Clouds” layer, it has a
slow but constant motion of its own.  In my simple tileset, I imagine the player to be somewhere in
between the “Foreground” represented by the green/orange things stuck to the bottom of the screen
and the “Middleground” which are the bent looking rectangular structures in the middle of the image.

For the programming part of this exercise, I’ve been simply following this [SDL
Tutorial](http://www.sdltutorials.com/sdl-tutorial-basics).  That tutorial basically gets you a
class that manages the lifecycle of your game along with the [main()
method](http://en.wikipedia.org/wiki/Main_function#C_and_C.2B.2B).  I had a little bit of trouble
getting this to work in [OSX](http://www.apple.com/macosx/),
but it turned out that I simply needed to [RTFM](http://en.wikipedia.org/wiki/Rtfm).  If you’re
trying this on a Mac, be sure to copy SDLMain.h and SDLMain.m from the “Extras” folder in the
[.dmg](http://en.wikipedia.org/wiki/Apple_Disk_Image).

The lion’s share of the work in this
[SDL_BlitSurface][archive-link-1]().
This method is well described in the second [SDL
Tutorial](http://www.sdltutorials.com/sdl-coordinates-and-blitting).
[Blitting](http://en.wikipedia.org/wiki/Blitting) is really just the act of drawing one bitmap on
top of another.

To implement layers as described above, I’ll create a class called an ImageLayer which takes an
array of SDL_Surface objects (images) and an array of coordinates representing the upper left corner
of each instance of the image sorted by X coordinates.  As the layer gets scrolled left or right,
it’s a simple matter of keeping track of which image instances represent the extreme edges of what’s
visible. All images in between these extremes get rendered.

With multiple ImageLayers populated with images and where they are, you render each layer from
furthest to nearest.


[archive-link-1]: http://wiki.libsdl.org/moin.cgi/SDL_BlitSurface?highlight=%28\bCategoryAPI\b%29%7C%28SDLFunctionTemplate%29%7C%28SGFunctions%29

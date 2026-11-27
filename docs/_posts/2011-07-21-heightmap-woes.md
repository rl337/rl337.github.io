---
layout: post
title: Heightmap woes
date: '2011-07-21'
author: Richard Lee
permalink: /2011/07/21/heightmap-woes/
legacy_archive: true
archive_source: https://web.archive.org/web/20160605144713/http://rl337.org/2011/07/21/heightmap-woes/
archive_original_timestamp: '2011-07-21T15:07:36+00:00'
categories:
- mars
tags:
- 3d
- blender
- mars-2
---

Originally published on 2011-07-21.

[View the Wayback capture][legacy-source].

[legacy-source]: https://web.archive.org/web/20160605144713/http://rl337.org/2011/07/21/heightmap-woes/




I started toying with converting some of the mars bitmaps into [height
maps](http://en.wikipedia.org/wiki/Heightmap).

Here is my first render… This is that crazy canyon formation (called the [Valles
Marineris](http://en.wikipedia.org/wiki/Valles_Marineris)) that I mentioned in the previous post…
and I believe that’s [Olympus Mons](http://en.wikipedia.org/wiki/Olympus_mons) in the distance.

[![First 3-d render of Mars data via
Blender](/assets/images/legacy-blog/2011/07/render-300x202.png.webp)](/assets/images/legacy-blog/2011/07/render.png.webp)

You
can see right off the bat that there are a ton of random issues with this image.  The most troubling
for me, though was the very prominent [aliasing](http://en.wikipedia.org/wiki/Aliasing).  Now, I’m
working from a 24-bit [png](http://en.wikipedia.org/wiki/Portable_Network_Graphics)… so i had
assumed that aliasing wouldn’t be such a huge problem.   For those of you not familiar with
Aliasing, click on the thumbnail to the left and look for what look like ugly topology lines in the
flat surfaces.  Those should in fact be smooth.  It’ll take a little more monkeying with the
settings to get a satisfactory image…

Here is a section of the height map that’s visible in the rendering:

[![Height Map
Fragment](/assets/images/legacy-blog/2011/07/render-topology-300x161.png.webp)](/assets/images/legacy-blog/2011/07/render-topology.png.webp)

If you click on this image, you’ll totally see the color change lines that cause my aliasing issue.
I’ll probably need to dip into higher resolution images… those will have “rougher” grain and should
alias a lot less…

---
layout: post
title: Renders from Mars
date: '2011-07-19'
author: Richard Lee
permalink: /2011/07/19/renders-from-mars/
legacy_archive: true
archive_source: https://web.archive.org/web/20160605182739/http://rl337.org/2011/07/19/renders-from-mars/
archive_original_timestamp: '2011-07-19T17:27:24+00:00'
categories:
- mars
tags:
- data
- mars-2
---

I’ve started to put some thought into where the martian city is to be located.  To do that, I need
to study a little bit on martian martian topology.  It turns out that we have some raw
[data](http://pds-geosciences.wustl.edu/geo/mgs-m-mola-5-megdr-l3-v1/mgsl_300x/) from
the [Mars Orbiter Laser Altimeter](http://mola.gsfc.nasa.gov/).  Yeah, I know it’s really not raw
data… who knows what the MOLA instrumentation spits out, but it’s raw for me.

The data is available in a number of resolutions and is packed neatly enough in files containing
signed 16-bit integers… Well, I just needed to put the data into an image format. Easy peasy right?
It took me a few tries…

My first attempt was with [PHP](http://php.net) through its
[libgd](https://bitbucket.org/pierrejoye/gd-libgd) .  Unfortunately, i found no easy way to
produce a 24-bit greyscale image… so I ended up with something that looked pretty blah.  My next
stab at it was through [Java](http://www.oracle.com/technetwork/java/index.html)… the thing
about this was… I was too lazy to read up on exactly how to read a signed short from a file, so I
tried this:

`int msb = inputStream.read();`
`int lsb = inputStream.read();`
`int value = msb * 256 + lsb;`

As it turned out, this process doesn’t retain the signedness of the 16-bit value…  So after digging
a little I came up with the right solution:

`DataInputStream dataStream = new DataInputStream(inputStream);`
`int value = dataStream.readShort();`

I had to mess with the contrast a little, but in the end I got what i wanted… topology of mars
rendered as images… check it out:

[![mars-surface1](/assets/images/legacy-blog/2011/07/mars-surface1-300x225.jpg.webp)](/assets/images/legacy-blog/2011/07/mars-surface1.jpg.webp)

This
image is some kind of ridge.  There’s clearly a drop off in altitude into smoother, less cratered
terrain.

This image reminds me a lot of the moon.  It’s pretty amazing that the martian atmosphere really
doesn’t protect it much from the pocking of meteorite impacts… or at the very least it doesn’t cover
it up over time like here on Earth.

[![mars-surface2](/assets/images/legacy-blog/2011/07/mars-surface2-300x225.jpg.webp)](/assets/images/legacy-blog/2011/07/mars-surface2.jpg.webp)

This
looks like some kind of insane canyon system.  It starts out pretty solid on the right side of the
image, but turns into a complex spiderweb of cracks and crevices as it moves to the left.

Having the actual raw data will enable me to create cool height maps in
[Blender](http://blender.org).  Looking forward to creating little flight videos through there.  I
bet it’ll be just like [Beggar’s Canyon](http://starwars.wikia.com/wiki/Beggar%27s_Canyon) back
home!

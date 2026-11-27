---
layout: post
title: Robo Optics
date: '2011-08-09'
author: Richard Lee
permalink: /2011/08/09/robo-optics/
legacy_archive: true
archive_source: https://web.archive.org/web/20151122074727/http://rl337.org/2011/08/09/robo-optics/
archive_original_timestamp: '2011-08-09T16:47:50+00:00'
categories:
- littlerobots
tags:
- 3d
- blender
- drawing
- robots
- sena
---

Originally published on 2011-08-09.

[View the Wayback capture][legacy-source].

[legacy-source]: https://web.archive.org/web/20151122074727/http://rl337.org/2011/08/09/robo-optics/




I’m finally getting into the grave details of modeling robot optics.  There is something that I’ve
noticed about sci-fi movie optics that make no real sense logically, but they definitely add drama
and emotiveness… the idea of eye color.

In just about all movies we’ve seen featuring robots, bad robots have red eyes.   Often we see as a
robot makes a transition from being a good robot, the lights on that robot itself change from say
blue to red.  I decided to add this color change concept to the robot optics I’ll be using for
Little Robots.

[![sena-optics](/assets/images/legacy-blog/2011/08/sena-optics.png.webp)](/assets/images/legacy-blog/2011/08/sena-optics.png.webp)

The
way I’ll do this is, behind the [aperture](http://en.wikipedia.org/wiki/Aperture), I’ll have a set
of three colored lamps.  As I want to express different emotional states, I’ll dim or intensify the
corresponding colors.  I’ll probably look up the [Mood Ring](http://en.wikipedia.org/wiki/Mood_ring)
color scale and just use that as my palette.   The lights themselves will reflect off a white
surface at the back of the optical cylinder and should show up through the aperture of the robot.
Nice and tidy.



Speaking of apertures… I discovered that well… I had no idea how a mechanical aperture worked.
Instead of chickening out and using something lame like a square aperture, I messed around and
discovered that really, apertures are just little sheets of rectangular metal (well, more like
[trapazoids](http://en.wikipedia.org/wiki/Trapazoid)) that rotate about 15 degrees.  Check it out:

[![blender-aperture](/assets/images/legacy-blog/2011/08/blender-aperture.png.webp)](/assets/images/legacy-blog/2011/08/blender-aperture.png.webp)

Here
you see my aperture which is made up of eight rectangles.  On the left, it’s in its closed state.
On the right, I posed it open.  Each aperture blade rotates a small amount in place and whammo… you
have an open aperture.

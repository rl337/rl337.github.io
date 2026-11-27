---
layout: post
title: N-Body Simulation
date: '2012-01-03'
author: Richard Lee
permalink: /2012/01/03/n-body-simulation/
legacy_archive: true
archive_source: https://web.archive.org/web/20120107211637/http://rl337.org/2012/01/03/n-body-simulation/
archive_original_timestamp: '2012-01-03T16:38:17+00:00'
---

Originally published on 2012-01-03.

[View the Wayback capture][legacy-source].

[legacy-source]: https://web.archive.org/web/20120107211637/http://rl337.org/2012/01/03/n-body-simulation/




A long time ago, I created a simple animation using [POV-Ray](http://povray.org/) that simulated a
[Neptune](http://en.wikipedia.org/wiki/Neptune)-like planet that I named Augustus-Voltaire 4.  I
used POV-Ray’s built-in [programmatic texturing](http://povray.org/documentation/view/3.6.1/331/)
features to create a blue banded atmosphere that had white speckled high atmospheric clouds. You can
see the video here… It’s got some pretty bad aliasing features due to compression, but you can get a
basic idea of what I was going for…

[Original embedded media](http://www.youtube.com/embed/i-BXQkFxmoA?rel=0)

Ultimately, I wasn’t happy with the result, so now years later, I’ve decided to take a stab at the
problem again…  This time, armed with a much faster computer!  But how do you simulate turbulent,
banded clouds?

I came up with a couple of different ideas for how to do it… but the only one that seemed to produce
anything vaguely interesting was [N-Body
simulation](http://en.wikipedia.org/wiki/N-body_simulation).  Essentially, you assume that the
atmosphere is a fluid and realize that fluids can be approximated with particles.  In the
simulation, you throw a few thousand simulated particles which interact with each other in set ways
(in my case, they all repel each other in an enclosed space).

I wrote the simulator in [Java](http://en.wikipedia.org/wiki/Java_%28programming_language%29)… and
is kind of slow.  Here is my first real attempt… it took about 18 hours to render.  The source is
too large to include here in the post.  If you’re interested in seeing it, drop me an email.

[Original embedded media](http://www.youtube.com/embed/47E3N1jOgvQ?rel=0)

In this simulation the Red and Blue components of the color describe its mass.  The redder the
particle, the heavier it is.  The Green component of the color is controlled by how fast the
particle is going.   I introduced a force pushing through the center.  The intensity tapers off as
you get closer to the top and bottom.  That the simulation quickly reached a form of equilibrium….
which is kinda cool, but doesn’t make for very interesting weather patterns.

I noted as I watched this run, was.. the particles tended to segregate themselves based on mass.
The heavier stuff accumulated near the center of rotation and the lighter stuff was pushed out to
the edges.

In my second N-Body simulation, I used far fewer particles but made each particle way more massive.
I also changed the shape of the force pushing through the center of the simulation, making it much
more narrow.

[Original embedded media](http://www.youtube.com/embed/HknDCFupeaA?rel=0)

Once again, you can see that we quickly reach a stable pattern.  This one seems to have much more
circulation though.  It seems like bigger particles are the way to go.   I have 2 more avenues to
explore as far as particles go…

- Make the simulatiion have a 3rd generation.  This aught to cause different masses to group in
  layers. That might be visually interesting.
- Add more complex ambient forces than the simple down-the-middle force.

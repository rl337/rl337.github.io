---
layout: post
title: Wrapping N-Body Simulation
date: '2012-02-02'
author: Richard Lee
permalink: /2012/02/02/wrapping-n-body-simulation/
legacy_archive: true
archive_source: https://web.archive.org/web/20120424223833/http://rl337.org/2012/02/02/wrapping-n-body-simulation/
archive_original_timestamp: '2012-02-02T17:33:16+00:00'
---

Originally published on 2012-02-02.

[View the Wayback capture][legacy-source].

[legacy-source]: https://web.archive.org/web/20120424223833/http://rl337.org/2012/02/02/wrapping-n-body-simulation/




[Original embedded media](http://www.youtube.com/embed/zHEIBDKso5w?rel=0)

Continuing with my [previous efforts](/2012/01/03/n-body-simulation/), I updated
my N-Body simulation code to not require the edges of the simulation to be boundaries.  Instead, the
edges now wrap.

[![point-translation](/assets/images/legacy-blog/2012/02/point-translation-300x224.png.webp)](/assets/images/legacy-blog/2012/02/point-translation.png.webp)

That
might seem like a pretty simple change, but the code involved gets a bit complex…

For example, say you’re calculating the force between particle A and some other particle B and
particle B’s force is wrapped around the screen, you need to basically translate B to the other side
of A and do your calculation…

If you’re in a corner… say the upper right, you’d have to do this with all particles above and all
particles to the right of you, so you’d need to do two sets of transformations.

The process is slow enough with 100,000 points that I need to think about moving from
[Java](http://en.wikipedia.org/wiki/Java_%28programming_language%29), which is what the simulation
is currently written in, to something speedier, like
[C](http://en.wikipedia.org/wiki/C_%28programming_language%29).

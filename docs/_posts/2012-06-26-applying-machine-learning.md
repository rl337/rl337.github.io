---
layout: post
title: Applying Machine Learning
date: '2012-06-26'
author: Richard Lee
permalink: /2012/06/26/applying-machine-learning/
legacy_archive: true
archive_source: https://web.archive.org/web/20120629070917/http://rl337.org/2012/06/26/applying-machine-learning/
archive_original_timestamp: '2012-06-26T16:02:43+00:00'
---

[![small-icon.hover](/assets/images/legacy-blog/2012/05/small-icon.hover_-150x135.png.webp)](/assets/images/legacy-blog/2012/05/small-icon.hover_.png.webp)

I’ve
successfully completed [Andrew Ng’s Machine Learning
class](https://class.coursera.org/ml/class/index). I feel pretty spiffy that I can now say that I’ve
implemented a [Neural Network](http://en.wikipedia.org/wiki/Neural_network)… though right now it’s
just in [Octave](http://www.gnu.org/software/octave/).

In his concluding video, Andrew asked that we go forth into the world and do cool things with
[machine learning](http://en.wikipedia.org/wiki/Machine_learning)… and I plan on doing exactly that.
I can think of several interesting things that I can build in the context of my work at [Topsy
Labs](http://topsy.com)… but it’s unlikely that any work context stuff will filter out in a way that
the public can see directly.. so I plan on creating a few personal projects around machine learning.

The first thing that I want to do is go through the course material and actually implement most of
it in Java.  For that purpose, I’ve checked in the start of said project into
[github](https://github.com/rl337) as part of my [incubator
repo](https://github.com/rl337/incubator). I’ve affectionately named the sub-project
“[SkyNET](http://en.wikipedia.org/wiki/Skynet_%28Terminator%29)” after the largely misunderstood AI
from the [Terminator Franchise](http://en.wikipedia.org/wiki/Terminator_%28franchise%29).  The code
itself won’t have specific spoilers from the exercises… that’d be bad form… but they will have brute
force implementations of the algorithms taught in the course.

I think that actually implementing things from scratch, I’ll get a better handle of how and why some
of this stuff works.  For this initial version of Skynet, I am not going to allow myself the luxury
of third party libraries.  The point isn’t to create a well optimized machine learning system… It’s
a learning exercise.  Part two of Skynet will be to re-implement the whole thing again in C++.  This
time I’ll incorporate a bunch of well optimized libraries like [Boost](http://www.boost.org/).

Those of you who want to troll through my Java code… here’s the [direct link to
Skynet](https://github.com/rl337/incubator/tree/master/main/skynet).

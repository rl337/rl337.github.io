---
layout: post
title: Introduction to Music Production, Assignment 4
date: '2013-08-19'
author: Richard Lee
permalink: /2013/08/19/introduction-to-music-production-assignment-4/
legacy_archive: true
archive_source: https://web.archive.org/web/20141014125321/http://rl337.org/2013/08/19/introduction-to-music-production-assignment-4/
archive_original_timestamp: '2013-08-19T00:57:14+00:00'
---

Originally published on 2013-08-19.

[View the Wayback capture][legacy-source].

[legacy-source]: https://web.archive.org/web/20141014125321/http://rl337.org/2013/08/19/introduction-to-music-production-assignment-4/




This is Richard Lee from San Francisco welcoming you to my 4th assignment for
[Coursera](http://coursera.org) and [Berklee College of Music’s](http://www.berklee.edu/) class,
[Introduction to Music Production](https://class.coursera.org/musicproduction-002/class).

I’ll be talking about Dynamic Processors and their parameters.  Specifically threshold, ratio,
attack and release.

As the name suggests, Dynamic Processors affect the [Dynamic
Range](http://en.wikipedia.org/wiki/Dynamic_range) of sound passing through it.  What does that
mean, exactly?

Dynamic Range has two distinct contexts.  On one hand, it refers to the contrast between the softest
sound that can be perceived by humans to the threshold of pain.  This seems like it’d be
straightforward to measure, but not only does the range vary from person to person, it also varies
environmental factors such as air pressure.

Thankfully, we’re mostly concerned with the other notion of Dynamic Range.  This Dynamic Range isn’t
loudness, but the range of signal amplitudes that can accurately passed from input to output through
a piece of audio equipment.

Some of the original uses for Dynamic Processors were to simply limit the amplitude of the signals
beyond a certain threshold.  We call this kind of processor a Limit.  It was put in place to protect
delicate equipment from sudden jolts or surges caused by connecting or dropping components.

You can generalize a Limit to not just cut a signal off at a threshold but instead restrict its
growth to something less aggressive, you get a Compressor.  To say that another way, a Limit is a
Compressor with a very large ratio.  In the context of Compressors, the Ratio represents the
amplitude of the input in relation to the output.

To make a compressor even more useful, we’ll introduce two new parameters, attack, which has time
units (typically milliseconds) gives us a delay between the signal crossing the threshold and the
ratio actually being applied to the input to get the output.  The opposite of attack is release,
which defines the delay between a signal falling below the threshold and the processor halting its
influence.

The main purpose of a compressor in modern music is to reduce the dynamic range of a piece so that
it’s possible to increase the gain, which makes the piece sound louder without distortion.

A sort of inverse to a Compressor is a Gate.  Where the Compressor activates when a signal’s
amplitude is above a certain threshold, a Gate aggressively attenuates any signal BELOW the
threshold.  This helps remove noise from a piece of music as the noise would fall below the
amplitude threshold of the instruments or vocals being played over it.

I’m cutting this assignment a little short.  I didn’t have time to create images to help visualize
what I was trying to get across in my text.  Hopefully I’ll be able to find some time to put some
polish on the next assignment!  Thanks for reading!

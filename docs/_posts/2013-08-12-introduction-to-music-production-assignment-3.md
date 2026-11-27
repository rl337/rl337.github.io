---
layout: post
title: Introduction to Music Production, Assignment 3
date: '2013-08-12'
author: Richard Lee
permalink: /2013/08/12/introduction-to-music-production-assignment-3/
legacy_archive: true
archive_source: https://web.archive.org/web/20141014130024/http://rl337.org/2013/08/12/introduction-to-music-production-assignment-3/
archive_original_timestamp: '2013-08-12T00:24:49+00:00'
categories:
- class
---

Hi. I’m Richard Lee from San Francisco.  This is my 3rd peer review assignment for [Berklee College
of Music](http://www.berklee.edu/)‘s [Introduction to Music
Production](https://class.coursera.org/musicproduction-002) Coursera Class.

For this assignment, I’d like to talk about submixes.  I REALLY enjoy the idea of using submixes.
 It really gets deep into the plumbing of busses and audio flow.  As it turns out though, my DAW of
choice, GarageBand does not have support for submixes, so I’ll have to keep the assignment largely
conceptual.

[![strings](/assets/images/legacy-blog/2013/08/strings-300x252.jpg.webp)](/assets/images/legacy-blog/2013/08/strings.jpg.webp)

So
what is a submix? Imagine you’re setting up to record an entire orchestra.  It’d be very convenient
to have an individual mixer board for every set of instruments playing a distinct part.   In the
example to the right, you see three distinct mixer boards, each one handling an individual type of
instruments.  Each mixer handling a “part” then feeds into an overall “string instruments” mixer.

This setup allows you to adjust the gains on each individual performer (say, player 2 of the violins
consistently plays decibels below the others).  On the “Strings” mixer, you can adjust the level of
all violins as a whole.   This allows you to adjust violins in relation to other instruments, say
the cellos.   Each of the individual instrument mixers could be considered a submix of the Strings
mixer.

Let’s continue to think about submixes in terms of physical devices.  Imagine now, we’re setting up
the audio to record a modern rock band.  We have significantly fewer instruments.  Let’s assume we
have a drum kit, an electric guitar, a bass guitar, and a vocal.  The drum kit has 3 inputs.  A bass
drum mic and two hanging mics.  Each of the other instruments/vocals have one input.

As far as submixes go, it would be nice to have all three inputs from the drums individually
adjusted as a submix.  It’d also be nice to be able to individually adjust each of the guitars, but
also change levels of both guitars relative to vocals or drums, so we should have a submix with both
guitars.  It might also be useful to have a submix of both the drums and guitars so that
instrumentals can be changed relative to vocals.  Finally, we’d like to have everything flowing
through a master, where we can apply some global effects to.   If we were to set this up like we did
for the orchestra, we’d have to find ourselves four very small mixer boards, each representing a
submix.  The submixes will cascade until they converge to a single output.  This means a LOT of
cable, a lot of “self noise” and a lot of opportunity for human error to ruin the recording.

What we’ll do in this case is use a single 10-input mixer board (see diagram below).  Here, we’ll
feed the outputs of the physical channels into the inputs of other channels; sometimes combining the
input of multiple channels.   The combining of multiple channel outputs into a single channel input
is called a “bus”.  To achieve our 4 submixes, we’ll use 4 busses.

[![rockband](/assets/images/legacy-blog/2013/08/rockband.jpg.webp)](/assets/images/legacy-blog/2013/08/rockband.jpg.webp)

Here you see the details of which channel outputs feed into what input.  The busses are denoted by
color.  Our drum submix is made up of the two hanging mics and the bass drum mic.  The guitar submix
is made up of the bass guitar and electric guitar.  The instrumental submix is made up of the drum
submix and the guitar submix.  Finally, the master output is a mix of the instrumental submix and
the vocals.  Thankfully, instead of running lots of cables between inputs and outputs on a physical
mixer board, we can use a full featured DAW.

This is a very basic layout with no aux-sends or effects.  Naturally, that stuff would add more
complexity to an already cluttered diagram; so I skipped it.

This week, I would have really liked to have tried this out on a DAW.  Unfortunately, I didn’t quite
have the time to try out some of the free DAWs that feature busses… Garage band kind of has a notion
of a bus, but it’s really just for effects… not for combining inputs or channeling outputs.

I hope that my examples were able to illustrate the need for and usefulness of submixes. Thanks for
reviewing my work.

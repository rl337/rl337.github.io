---
layout: post
title: Breaking out Instruments
date: '2011-10-04'
author: Richard Lee
permalink: /2011/10/04/submediant-breaking-out-instruments/
legacy_archive: true
archive_source: https://web.archive.org/web/20111007115745/http://rl337.org/2011/10/04/submediant-breaking-out-instruments/
archive_original_timestamp: '2011-10-04T17:21:36+00:00'
categories:
- submediant
tags:
- lullaby
- music
- sound
recovery_notes: |
  The original Flash audio was not recovered.

  [Original audio URL in Wayback][legacy-audio-1].

  [legacy-audio-1]: https://web.archive.org/web/20140000000000/http://rl337.org/wp-content/uploads/2011/10/little_robots-let_them_eat_test-all_through_the_night.mp3
---

I did a bit more work on
[Submediant](/2011/09/13/submediant-the-voice-of-robots/). The
goal for this set of changes was to allow the score files to define what kind of instrument to use.
Before, we could add multiple instruments but they all used the same basic [sine
wave](http://en.wikipedia.org/wiki/Sine_wave) generator…

Not only did I want to give the ability of specifying an instrument to the score file, though, I
wanted to make creating new types of instruments easily… so I introduced a class hierarchy.
Essentially, all instrument objects have a common ancestor, the Instrument.  I defined
MusicalInstrument as any instrument that knows/understands musical notation.  Finally, I defined two
children of MusicalInstrument, MusicalSineInstrument which plays a sine wave and
MusicalSquareInstrument which plays a [square wave](http://en.wikipedia.org/wiki/Square_wave).  I
then found a [simple score](http://www.free-scores.com/download-sheet-music.php?pdf=3312) to
transcribe into Submediant…  Here is what it sounds like:

According to the description, it’s a [Welsh](http://en.wikipedia.org/wiki/Welsh_language)
[Lullaby](http://en.wikipedia.org/wiki/Lullaby) arranged for a
[recorder](http://en.wikipedia.org/wiki/Recorder) duet.

In case you’re curious… here’s the Submediant score file:

[View the original score in the archived
post](https://web.archive.org/web/20111007115745/http://rl337.org/2011/10/04/submediant-breaking-out-instruments/)

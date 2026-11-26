---
layout: post
title: 'Submediant: Imagine – A work in progress'
date: '2011-09-27'
author: Richard Lee
permalink: /2011/09/27/submediant-imagine-a-work-in-progress/
legacy_archive: true
archive_source: https://web.archive.org/web/20111001121634/http://rl337.org/2011/09/27/submediant-imagine-a-work-in-progress/
archive_original_timestamp: '2011-09-27T16:35:17+00:00'
categories:
- submediant
tags:
- imagine
- sound
---

Originally published on 2011-09-27.

[View the Wayback capture][legacy-source].

[legacy-source]: https://web.archive.org/web/20111001121634/http://rl337.org/2011/09/27/submediant-imagine-a-work-in-progress/


This past weekend, I worked more on [Submediant](/2011/09/13/submediant-the-voice-of-robots/).  This
time through included both an internal [refactor](http://en.wikipedia.org/wiki/Code_refactoring) as
well as a few new features:

- Instruments have a chord notation
- Instruments can have individually adjusted volume
- Notes can now be tied together

To help demonstrate the new features, I’ve called upon one of my inspirations, [John
Lennon](http://en.wikipedia.org/wiki/John_Lennon).  This is about a quarter of the song,
[Imagine](http://en.wikipedia.org/wiki/Imagine_%28song%29) rendered with Submediant…

Here is source code for the song…

[View the original score in the archived
post](https://web.archive.org/web/20111001121634/http://rl337.org/2011/09/27/submediant-imagine-a-work-in-progress/)

You can see that chords are simply notes that specify multiple frequencies… for example, C4,E4:1/4
is a quarter note that rings as both [middle C](http://en.wikipedia.org/wiki/Middle_C) and the E a
step above it. You can also see the notation for tied notes:  C4:1/8:tie C4:1/8 C4:1/8:untie are
three 8th notes tied together. Whether a note is tied or not tells the instrument rendering the
sound how to handle the [attack/decay](http://en.wikipedia.org/wiki/Synthesizer#ADSR_envelope)
aspects of the sound generated…

You can see that each of the instruments in the source sets a custom volume.  One thing that I want
to work on in the future is allowing the volume of an instrument to change.  Even though you can set
the volume on any of the lefthand designators, only the last one is applied to the whole song.

There are a few aspects of the code that bother me… it needs more refactoring… but I’ve gotten it to
the point where I need it.  I can now use Submediant as a framework to give [Little
Robots](https://web.archive.org/web/20111001121634/http://rl337.org/category/littlerobots/?sortby=ID&order=ASC)
the ability to speak.


The original Flash audio was not recovered.

[Original audio URL in Wayback][legacy-audio-1].

[legacy-audio-1]: https://web.archive.org/web/20140000000000/http://rl337.org/wp-content/uploads/2011/09/little_robots-let_them_eat_test-imagine.mp3

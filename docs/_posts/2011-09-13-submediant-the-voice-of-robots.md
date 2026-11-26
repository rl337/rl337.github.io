---
layout: post
title: Submediant, the voice of robots
date: '2011-09-13'
author: Richard Lee
permalink: /2011/09/13/submediant-the-voice-of-robots/
legacy_archive: true
archive_source: https://web.archive.org/web/20110930043108/http://rl337.org/2011/09/13/submediant-the-voice-of-robots/
archive_original_timestamp: '2011-09-13T15:54:57+00:00'
categories:
- littlerobots
- submediant
tags:
- robots
- sound
---

Originally published on 2011-09-13.

[View the Wayback capture][legacy-source].

[legacy-source]: https://web.archive.org/web/20110930043108/http://rl337.org/2011/09/13/submediant-the-voice-of-robots/


This past weekend, I spent some time honing the script from [last blog
post](/2011/09/08/exit-structured-audio-enter-home-grown/)
into a framework that could be used to give voice to my [Little
Robots](https://web.archive.org/web/20110930043108/http://rl337.org/category/littlerobots/?sortby=ID&order=ASC).
Okay, so what’s changed since I published that awesome [.wav](http://en.wikipedia.org/wiki/WAV)
generating [perl](http://perl.org) script? Well, first let’s listen to something rendered by the new
script…

You can hear that the sound is far more refined.  I took the time to add some basic [attack and
decay](http://en.wikipedia.org/wiki/Attack-decay-sustain-release_envelope#ADSR_envelope) to the sine
waveform.  Even though it’s one of the most audible changes… it’s probably one of the least
significant.   One major change from the previous script is the movement of all data to external
data files…

Here is the data file that generated the MP3 that you just listened to:

[View the original score in the archived
post](https://web.archive.org/web/20110930043108/http://rl337.org/2011/09/13/submediant-the-voice-of-robots/)

You can see, both the notes and metadata about the song are found all in one place, completely apart
from the code.  At the very top of the file are attributes which are denoted with an ‘@’.  Notes are
comma separated tuples where the first field is the note itself and the 2nd field is its duration.
Notes are divided into sections attributed to instruments (set off by an &).  Multiple sections for
a single instrument simply append notes.

In this particular example, we have two instruments, one called lefthand and the other called
righthand.  They simulate the left and right hands when playing the very simplified version of
[Minuet in G](http://en.wikipedia.org/wiki/Minuet_in_G_major_%28BWV_Anh._114%29) from the [Easiest
Book of Piano Favorites](http://www.amazon.com/dp/product/0825617618).

Both the notes and the durations are defined in a file.  The notes get mapped to
[frequencies](http://en.wikipedia.org/wiki/Frequencies_of_notes) and the durations get mapped to
fractions of [beats](http://en.wikipedia.org/wiki/Tempo).  In my notation, 1/2 means [half
note](http://en.wikipedia.org/wiki/Half_note), 1/4 means [quarter
note](http://en.wikipedia.org/wiki/Quarter_note), etc… and if it ends in a period, that’s a [dotted
note](http://en.wikipedia.org/wiki/Dotted_note).

Like all great projects, this one needed a name… and so I scoured
[Wikipedia](http://en.wikipedia.org/)‘s audio/sound entries for the first cool sounding term that I
had no real understanding of… and that became the name of the project…
[Submediant](http://en.wikipedia.org/wiki/Submediant). Even after trying to read the wiki page… I
still have no idea what a Submediant is… but I’m sticking to it.


The original Flash audio was not recovered.

[Original audio URL in Wayback][legacy-audio-1].

[legacy-audio-1]: https://web.archive.org/web/20140000000000/http://rl337.org/wp-content/uploads/2011/09/little_robots-let_them_eat_test-minuet_in_g.mp3

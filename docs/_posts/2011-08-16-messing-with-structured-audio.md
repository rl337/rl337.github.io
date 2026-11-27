---
layout: post
title: Messing with Structured Audio
date: '2011-08-16'
author: Richard Lee
permalink: /2011/08/16/messing-with-structured-audio/
legacy_archive: true
archive_source: https://web.archive.org/web/20111020212050/http://rl337.org/2011/08/16/messing-with-structured-audio/
archive_original_timestamp: '2011-08-16T17:33:32+00:00'
categories:
- littlerobots
tags:
- structuredaudio
---

Originally published on 2011-08-16.

[View the Wayback capture][legacy-source].

[legacy-source]: https://web.archive.org/web/20111020212050/http://rl337.org/2011/08/16/messing-with-structured-audio/


It’s time to seriously consider what Seña will sound like. To accomplish that, I’ve started messing
with [structured audio](http://www.cs.berkeley.edu/~lazzaro/sa/book/index.html).  What does that
mean?

It seems that part of the MP4 standard includes a section involving programmatically generated
sound.  Basically, making synthetic sounds with programming.  It’s visually pretty drab, but if
you’re into coding like I am… it’s pretty cool.

The audio programming language takes 2 major components, a
[SAOL](http://www.cs.berkeley.edu/~lazzaro/sa/book/control/saolc/index.html) file, and a
[SASL](http://www.cs.berkeley.edu/~lazzaro/sa/book/control/sasl/index.html) file.  The SAOL file is
where you define your “instruments” and the SASL is where you sequence your instruments playing
notes…

I made a test SASL and SAOL based on the example scripts they provided.

    instr sine_tone(f, a) {
        asig x, y, init;

        if (init == 0) {
            init = 1;
            x = 0.5;
        }

        x = x - f * y;
        y = y + f * x;

        output(y * a);
    }

Here I added two parameters, f and a. This allowed me to control the frequency and amplitude of the
approximated sine wave created by the x= and y= expressions.

To actually play the instrument, I made a SASL file:

    0.25 sine_tone 0.50 0.196307 0.10
    0.50 sine_tone 0.75 0.296307 0.10
    0.75 sine_tone 1.00 0.396307 0.10
    1.25 sine_tone 1.50 0.196307 0.20
    1.50 sine_tone 1.75 0.296307 0.20
    1.75 sine_tone 2.00 0.396307 0.20
    2.25 sine_tone 2.50 0.196307 0.35
    2.50 sine_tone 2.75 0.296307 0.35
    2.75 sine_tone 3.00 0.396307 0.35
    3.25 end

Here you see I invoked my “sine_tone” instrument with various parameters. The leading number and
first parameter represent start and end times in seconds. The last two parameters map to the f and a
variables of my instrument.

I wasn’t able to get the audio player plugin to work properly with the resulting .wav file nor was I
able to get it to play with an itunes converted m4a…

UPDATE: I managed to get a proper mp3 toolchain going. I might describe that in more detail on
Thursday. For now, here is a proper flash audio player


The original Flash audio was not recovered.

[Original audio URL in Wayback][legacy-audio-1].

[legacy-audio-1]: https://web.archive.org/web/20140000000000/http://rl337.org/wp-content/uploads/2011/08/simplesine-threetone.mp3

---
layout: post
title: Building infrastructure in ChucK
date: '2014-02-23'
author: Richard Lee
permalink: /2014/02/23/building-infrastructure-in-chuck/
legacy_archive: true
archive_source: https://web.archive.org/web/20140324224702/http://rl337.org/2014/02/23/building-infrastructure-in-chuck/
archive_original_timestamp: '2014-02-23T21:55:48+00:00'
categories:
- chuck
---

[ChucK](http://chuck.cs.princeton.edu/) is a programming environment specifically geared toward
generating sound.  I was first exposed to it through the Coursera Class [Introduction to Programming
for Musicians and Digital Artists](https://www.coursera.org/course/chuck101).

Chuck the language is a little weird, but expressive enough. It’s really good at making experimental
sounds and generating samples but doesn’t have an extensive classlib for playing around with music
theory.

I’ve started a github repository to build out this kind of
infrastructure: <https://github.com/rl337/chuck>

The base class in my library that makes noise is called a Playable.  It’s interface looks like this:

    public class Playable {
        function void play(int midi_note, dur duration, float gain);
        function void play(float freq, dur duration, float gain);
    }

The play methods are synchronous. You might think this would be a serious limitation but a major
feature of ChucK is it’s ability to spin off threads (called sporks)… so keeping things synchronous
keeps the logic easy to follow. At the moment, I only have very basic waveforms implementing
Playable… but later on I can make these things quite complex.

Adding to the library from the music theory side, we have the Scale object:

    public class Scale {
        function void init(int tonic, int intervals[]);
        function int note(int degree);
    }

Here you can initialize the scale with a list of intervals. Intervals are basically the number of
half-steps between the scale degrees. Typically this is 8, but the way it’s coded it can be an
arbitrarily sized array. This will let it capture non-8-degree scales like blues scales later on.
The note() method takes an arbitrary scale degree and returns the midi note of that degree.

As a utility for creating lots of useful scales, I’ve created the Scales object:

    public class Scales {
        public static Scale Major(int tonic);
        public static Scale Minor(int tonic);
    }

The Scales object are essentially factories for Major and Minor Scales… so if you don’t want to
memorize and initialize a Scale object every time, you can just say Scales.Major(60) and BAM you
have a C Major scale!

Building on the Scale object, I created the Chord object. This is going to be a work in progress
because I’m still learning all of the theory behind building chords. Really I just have the
functionality around triads coded up… but it looks like this:

    public class Chord {
        public void init(int halfsteps[]);
        public int note(int index);
    }

The halfsteps are actual midi notes. Now this might not seem that useful as the structure is
super-simple but you’re really not supposed to construct chords on your own… to do that, I’ve build
the Chords factory object. This is where most of music theory around building chords on scales will
take place:

    public class Chords {
        public static Chord Major(Scale scale, int root);
        public static Chord Augmented(Scale scale, int root);
        public static Chord Minor(Scale scale, int root);
        public static Chord Diminished(Scale scale, int root);
    }

Here the Root is in zero-based scale degrees… not in midi notes… so if you have a C scale, the 0th
degree is C.
In order to get a D Major chord on a C Major Scale, you can just do this:
Chords.Major(Scales.Major(60), 2)
There will be a lot of convenience methods here.. I’m sure 7th chords will be added next.

In order to play Chords, I’ve created a class called a Chordable. It takes an array of Playables
which it then uses to voice chords.

        public void init(Playable voices[]);
        function void inversion(int inversion);
        function void play(Chord chord, dur duration, float gain);
        function void arpeggio(Chord chord, int sequence[], dur duration, float gain);

Here, you see that the init() method takes an array of Playable. The play() method plays the chord
voiced with whatever the current inversion is set to. Really, the inversion should probably go on
the Chord, but i found it convenient to put it here. The arpeggio() method takes a chord note array
and divides the duration playing each of the chord notes specified.

Everything is still pretty basic… and i’m sure that it’ll evolve over time.. but as a software
engineer, it makes exploring music theory a little more fun.

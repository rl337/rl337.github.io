---
layout: post
title: Exit Structured Audio, Enter Home Grown
date: '2011-09-08'
author: Richard Lee
permalink: /2011/09/08/exit-structured-audio-enter-home-grown/
legacy_archive: true
archive_source: https://web.archive.org/web/20110930042945/http://rl337.org/2011/09/08/exit-structured-audio-enter-home-grown/
archive_original_timestamp: '2011-09-08T16:33:26+00:00'
categories:
- littlerobots
- submediant
tags:
- announce
- robots
- sound
- structuredaudio
recovery_notes: |
  The original Flash audio was not recovered.

  [Original audio URL in Wayback][legacy-audio-1].

  [legacy-audio-1]: https://web.archive.org/web/20140000000000/http://rl337.org/wp-content/uploads/2011/09/wavegen-temp.mp3
---

In a previous [blog
post](/2011/08/16/messing-with-structured-audio/), I had explored
using [MPEG4 Structured Audio](http://www.cs.berkeley.edu/~lazzaro/sa/book/index.html) to produce
the sounds that my robots will make in future animation.  A few weeks later, I find that the
learning curve for the tools is a bit too steep for my liking… so I decided to start from scratch…
and write my own.

Yeah, I understand that people of far greater sound knowledge and experience put a LOT of effort
into Structured Audio, but that doesn’t help me now.  Maybe this tool that I’m building (which
doesn’t quite have a name yet) will iterate toward the stuff I’m giving up… but I’m sure I’ll learn
quite a bit about audio programming along the way.

As it turns out, most of the tool chain that I had [previously
built](/2011/08/18/structured-audio-c-major-scale/) still works!
I’m just replacing [sfront](http://www.cs.berkeley.edu/~lazzaro/sa/sfman/index.html) with something
that I’ve written… and if you’re curious what a program looks like which generates .wav files? here
it is!

    #!/usr/bin/perl

    use strict;

    my $filename = shift @ARGV;
    die "You must specify an output file." unless $filename;

    my %aliases = (
       C4 => 261.626,
       D4 => 293.665,
       E4 => 329.628,
       F4 => 349.228,
       G4 => 391.995,
       A4 => 440.000,
       B4 => 493.883,
       C5 => 523.251
    );

    my @song = qw(B4 A4 G4 A4 B4 B4 B4 A4 A4 A4 B4
                  D4 D4 B4 A4 G4 A4 B4 B4 B4 B4 A4 A4 B4 A4 G4);
    my $duration = (scalar @song) * 0.5 + 0.5;
    my $volume = 8000;

    my @notes;
    push @notes, $aliases{$_} for @song;

    my $channels = 1;
    my $samplerate = 44100;
    my $bitspersample = 16;
    my $byterate = $channels * $samplerate * $bitspersample / 8;
    my $blockalign = $channels * $bitspersample / 8;
    my $samples = $samplerate * $duration;
    my $dataChunkSize = $samples * $bitspersample / 8;
    my $chunkSize = 36 + $dataChunkSize;

    my @values;
    for (my $i = 0; $i < $samples; $i++) {
       my $note = int($i / $samplerate * 2);
       my $freq = $notes[$note];
       my $x = $i * $freq / $samplerate * 3.14159 * 2;
       push @values, int($volume * sin($x));
    }

    open(FILE, "> $filename") || die "could not open $filename";
    print FILE pack('NVN', 0x52494646, $chunkSize, 0x57415645);
    print FILE pack('NVvvVVvv', 0x666d7420, 16, 1, $channels, $samplerate,
         $byterate, $blockalign, $bitspersample);
    print FILE pack('NV', 0x64617461, $dataChunkSize);
    for my $sample (@values) {
        print FILE pack('v', $sample);
    }

    close(FILE);

Yup. That’s the whole thing.  No libraries. No weird complexity.

I decided to write the thing in [perl](http://perl.org) for the practice.  I use an awful lot of
perl at work, so as this project grows, it’ll force me to learn the proper perl patterns.

If you’re curious what that program produces? Here’s the converted MP3:

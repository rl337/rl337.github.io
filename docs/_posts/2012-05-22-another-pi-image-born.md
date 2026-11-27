---
layout: post
title: Another Pi Image is Born
date: '2012-05-22'
author: Richard Lee
permalink: /2012/05/22/another-pi-image-born/
legacy_archive: true
archive_source: https://web.archive.org/web/20120530095808/http://rl337.org/2012/05/22/another-pi-image-born/
archive_original_timestamp: '2012-05-22T15:32:49+00:00'
---

[![pi](/assets/images/legacy-blog/2012/05/pi-300x268.jpg.webp)](/assets/images/legacy-blog/2012/05/pi.jpg.webp)

I
recently saw the movie [Pi](http://www.imdb.com/title/tt0138704/) for the first time.  A number of
friends and family recommended the movie to me when it first came out.  Me specifically.  As in,
this movie would somehow resonate with me on some fundamental way.   It just seemed, though, that
the harder I was pushed to see the film, the less likely I felt like actually watching it.

Fast forward about 10 years to a week ago.  I was trolling [Netflix](http://netflix.com) streaming
for something to watch and decided… “Oh, what the hell.”  I hit play.

I can understand why so many people thought that I’d like this movie.  I think though, that it hits
a little too close to home in some aspects but is somewhat dumb in others.  I don’t really want to
get into a technical review of the movie because I’m sure that it wasn’t intended to be scrutinized
in that way.  I did enjoy it as a story though.

Every computer scientist I know has thought about how to predict the stock market.  I’m not sure
that each and every one creates some explicit mantra as does the guy in the movie, but, you know… we
don’t all live in a black and white film.

When I’m done with the [Machine Learning](http://www.coursera.org/course/ml) class over on
[Coursera](http://www.coursera.org/), I do plan on trying to make a short-term sale predictor AI.
I’m hoping that I won’t inadvertently learn a true name of God and end up drilling a hole in my
head.  I guess we’ll see.

Instead of just stealing someone else’s colorful pi image, I thought I’d be fun to make one.  The
image used in this blog post was based on the [Wikipedia SVG of the Greek
Letter](http://en.wikipedia.org/wiki/File:Pi_uc_lc.svg).  I imported it into the
[GIMP](http://gimp.org) and exported it as text (Yeah, you can do that!).  After cleaning it up a
little, I wrote a program that would populate the actual pi digits into the exported image.

    #!/usr/bin/perl
    use strict;

    open(my $pifd, "pi-image.txt") or die "couldn't open pi image";
    open(my $numfd, "pi-digits.txt") or die "couldn't open pi digits";
    my $ch;
    while(1) {
        read($pifd, $ch, 1) or last;
        if ($ch eq "\n") {
            print "\n";
            next;
        }
        if ($ch ne ' ') {
            read($numfd, $ch, 1) or last;
        }
        print "$ch";
    }
    close($pifd);
    close($numfd);

Once I had the numerically populated glyph, I pulled it back into the GIMP via screenshot and
applied a rainbow gradient! Bam! Yet another Pi image is born!

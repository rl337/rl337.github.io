---
layout: post
title: 16×2 LCD Display Contrast
date: '2012-01-26'
author: Richard Lee
permalink: /2012/01/26/16x2-lcd-display-contrast/
legacy_archive: true
archive_source: https://web.archive.org/web/20120307024842/http://rl337.org/2012/01/26/16x2-lcd-display-contrast/
archive_original_timestamp: '2012-01-26T17:37:08+00:00'
categories:
- arduino-2
---

Originally published on 2012-01-26.

[View the Wayback capture][legacy-source].

[legacy-source]: https://web.archive.org/web/20120307024842/http://rl337.org/2012/01/26/16x2-lcd-display-contrast/




[![lcd-rig](/assets/images/legacy-blog/2012/01/lcd-rig-266x300.jpg.webp)](/assets/images/legacy-blog/2012/01/lcd-rig.jpg.webp)

A
few weeks ago, I put in an order to [Jameco](http://www.jameco.com/) for some parts that’ll help me
complete some of the projects in [Michael
McRoberts](http://www.amazon.com/Michael-McRoberts/e/B004997ZYW)‘s book [Beginning
Arduino](http://www.amazon.com/Beginning-Arduino-Michael-McRoberts/dp/1430232404/ref=ntt_at_ep_dpt_1).

One of the more interesting components was this [KST1602B 16×2 LCD
Display](http://www.jameco.com/webapp/wcs/stores/servlet/Product_10001_10001_1954674_-1).  I dunno
about you all, but ever since I saw one on a digital calculator, I’ve wanted to bend one of these
bad boys to my will… and now I have! … well, sorta.

The first time I wired this up, I got a totally blank screen. I had assumed that I did \*something\*
wrong and went through and re-verified that things were connected right.  Finally, I eyed the
resistor that I had been using on the “Contrast” pin on the LCD.  (V0 in the case of this one).  I
had chosen a [resistor](http://en.wikipedia.org/wiki/Resistor) close to that described in the book,
but meh… so I pulled out the [potentiometer](http://en.wikipedia.org/wiki/Potentiometer) from my
[last
project](/2012/01/11/smooth-analog-input-class-for-arduino/)
and hooked that up to pin V0.  It turns out that the resistance needs to be a lot more than what I
had expected!

[![lcd-contrast](/assets/images/legacy-blog/2012/01/lcd-contrast-300x120.jpg.webp)](/assets/images/legacy-blog/2012/01/lcd-contrast.jpg.webp)

To
the left you can see an image with three contrast settings on the potentiometer.  The top one is max
(about 10k ohms) the middle one was maybe 8k ohms and the last one represents anything less than
say, 7k ohms.

When you look at the data sheet PDF, the section called “Adjusting Display Contrast” seems to
suggest that you can put a resistance of between 20 and 50k ohms… that’s a HUGE range considering
that what you can go from visible to NO contrast in less than 2k ohms.  I feel like the contrast
range should be a little more linear… but that’s just me.

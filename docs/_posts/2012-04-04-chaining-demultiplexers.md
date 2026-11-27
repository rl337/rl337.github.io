---
layout: post
title: Chaining Demultiplexers
date: '2012-04-04'
author: Richard Lee
permalink: /2012/04/04/chaining-demultiplexers/
legacy_archive: true
archive_source: https://web.archive.org/web/20120410224149/http://rl337.org/2012/04/04/chaining-demultiplexers/
archive_original_timestamp: '2012-04-04T14:44:15+00:00'
categories:
- arduino-2
---

Originally published on 2012-04-04.

[View the Wayback capture][legacy-source].

[legacy-source]: https://web.archive.org/web/20120410224149/http://rl337.org/2012/04/04/chaining-demultiplexers/




[![IMG_0657](/assets/images/legacy-blog/2012/04/IMG_0657-300x224.jpg.webp)](/assets/images/legacy-blog/2012/04/IMG_0657.jpg.webp)

Before,
I controlled 6 LEDs with 3 pins.  This fit very neatly onto a single 3-8 Demultiplexer.  For me to
achieve my goals of world domination, I need to be able to chain them.

What exactly do I mean by chaining?  Well, by themselves, a 3-8 demultiplexer can control 8 things
with 3 control pins.  It follows, that to control 16 things, we need 2 demultiplexers and 6 control
pins.  Well, by chaining, you can control 16 things with just 4 pins!  Well, how does this work?

Well, you take the regular 3 control pins and connect them to BOTH multiplexer input pins. The 4th
“input” pin actually just switches between which demultiplexer we’re using.  So it connects to the
“G1″ of the second and one of the G2s on the first.

I couldn’t really do this before because I lacked the space on my previous little breadboard.  In
case you hadn’t noticed… I’ve upgraded!

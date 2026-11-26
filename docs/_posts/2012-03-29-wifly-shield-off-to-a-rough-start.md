---
layout: post
title: WyFly Shield off to a rough start
date: '2012-03-29'
author: Richard Lee
permalink: /2012/03/29/wifly-shield-off-to-a-rough-start/
legacy_archive: true
archive_source: https://web.archive.org/web/20120410224131/http://rl337.org/2012/03/29/wifly-shield-off-to-a-rough-start/
archive_original_timestamp: '2012-03-29T16:41:38+00:00'
---

Originally published on 2012-03-29.

[View the Wayback capture][legacy-source].

[legacy-source]: https://web.archive.org/web/20120410224131/http://rl337.org/2012/03/29/wifly-shield-off-to-a-rough-start/




[![IMG_0652](/assets/images/legacy-blog/2012/03/IMG_0652-300x224.jpg.webp)](/assets/images/legacy-blog/2012/03/IMG_0652.jpg.webp)

Here
you see my new [WyFly](http://www.sparkfun.com/products/9367) shield!  This little guy will one day
bring [Wifi](http://en.wikipedia.org/wiki/Wifi) capabilities to my
[Arduino](http://arduino.cc/en/Main/ArduinoBoardUno)… but not yet… not yet.

Thankfully there isn’t a lot of assembly required for the shield.  All you have to do is solder in
the [headers](http://www.sparkfun.com/products/9279)… which is easy enough… even for me! (see the
[evidence](https://plus.google.com/u/1/111497547501522705099/posts/RJS78jywK5u))

Out of the box, the [libaries](http://forum.sparkfun.com/viewtopic.php?f=32&t=25216) didn’t seem to
want to work.  First there’s the “no such WProgram.h” issue which is easy enough to solve… you
change the \#include to “Arduino.h”.. but then there were some strange Arduino API changes with the
Print object.  Nothing was terribly wrong… the write() methods now returned a size_t when before
they were void.

Compilation out of the way… I uploaded an example… and nothing happened. I was supposed to see a
google search result for “Arduino” scroll past on the Serial Monitor… but nothing.  Looks like more
digging for me.

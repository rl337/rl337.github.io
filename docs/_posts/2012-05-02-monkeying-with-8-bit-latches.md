---
layout: post
title: Monkeying with 8-bit Latches
date: '2012-05-02'
author: Richard Lee
permalink: /2012/05/02/monkeying-with-8-bit-latches/
legacy_archive: true
archive_source: https://web.archive.org/web/20120521180524/http://rl337.org/2012/05/02/monkeying-with-8-bit-latches/
archive_original_timestamp: '2012-05-02T05:04:15+00:00'
categories:
- arduino-2
---

I while back, I bought a couple of [8-bit
Latches][archive-link-1]
which I had intended to conquer the world with… but just never got around to it. As I’ve just found
out… these specifically may not be the right model for that purpose. sigh.  Let me expound…

[![IMG_0683](/assets/images/legacy-blog/2012/05/IMG_0683-300x224.jpg.webp)](/assets/images/legacy-blog/2012/05/IMG_0683.jpg.webp)

As
I’ve explored in previous [Arduino
setups](/2012/04/04/chaining-demultiplexers/), I want to control lots of
things with few output pins.  With this specific setup, I was hoping to populate two different 8-pin
latches using a large number of shared pins like with the LCD project… but alas, these latches don’t
really like sharing their pins…

If I share pins between the latches (clock/latch pins) but have a selectable data pin, the
unselected latch still \*thinks\* I’m talking to it… What I need is a latch with an Enable Pin.

Pictured above, I was just testing to verify that both latches actually worked. Both are connected
to the same outputs, so their values are mirrored. I won’t post any code this time because I used
the [ShiftOut](http://arduino.cc/en/Tutorial/ShiftOut) example verbatim.


[archive-link-1]: https://www.jameco.com/webapp/wcs/stores/servlet/ProductDisplay?storeId=10001&productId=911189&langId=-1&catalogId=10001&krypto=kMYYrBxGZ%2FJcfaX9kvnXQccS%2BP4zc75V%2FP8SOwNmJCk%3D&ddkey=https:CookieLogon

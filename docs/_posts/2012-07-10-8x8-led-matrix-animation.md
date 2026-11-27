---
layout: post
title: 8×8 LED Matrix animation
date: '2012-07-10'
author: Richard Lee
permalink: /2012/07/10/8x8-led-matrix-animation/
legacy_archive: true
archive_source: https://web.archive.org/web/20120719043822/http://rl337.org/2012/07/10/8x8-led-matrix-animation/
archive_original_timestamp: '2012-07-10T23:44:18+00:00'
categories:
- arduino-2
---

[![IMG_0781](/assets/images/legacy-blog/2012/07/IMG_0781-300x225.jpg.webp)](/assets/images/legacy-blog/2012/07/IMG_0781.jpg.webp)

It’s
been a little while since I messed with my Arduino… so here we go.

This time around, I hooked up with an [8×8 LED
matrix](http://www.jameco.com/webapp/wcs/stores/servlet/Product_10001_10001_2132349_-1).
Essentially, it’s an array of 64 LEDs addressable via 16 pins.

But wait, you ask… how can you address 64 pins with only 16 pins?? That’s an excellent question!
The answer is… not very well.  It turns out that you can only independently address one LED at a
time with this system… well, really only one row at a time… otherwise you get unexpected LEDs
lighting up.

The answer to this problem is essentially
[rastering](http://en.wikipedia.org/wiki/Raster_graphics).  Essentially this means that you display
one row at a time.  You just make sure that the rate at which you display rows happens fast enough
that the observer can’t see that you’re only ever have a single row illuminated.

I chose a really boring animation here.  It’s just an inverting rectangular region inverting
[![lcdmatrix](/assets/images/legacy-blog/2012/07/lcdmatrix.gif)](/assets/images/legacy-blog/2012/07/lcdmatrix.gif)

itself.
This project was taken almost verbatim from project 19 in [Michael McRoberts’s Beginning
Arduino](http://www.amazon.com/Beginning-Arduino-Michael-McRoberts/dp/1430232404).

To the right, you see an animation of my LED Matrix. Kinda distracting, huh… sorry.

A bit later, I’ll use this LED matrix as a means of outputting an accelerometer.  I’d like to think
that I can come up with some cool looking UI in 64 LEDs.

For the curious, here’s the code listing for this project:

    #include <TimerOne.h>

    const int gLatchPin = 11;
    const int gClockPin = 13;
    const int gDataPin = 12;

    const int pLatchPin = 8;
    const int pClockPin = 10;
    const int pDataPin = 9;

    int n = 0;

    int icons[2][8] = {
        {
          0B11111111,
          0B11111111,
          0B11000011,
          0B11000011,
          0B11000011,
          0B11000011,
          0B11111111,
          0B11111111,
        },
        {
          0B00000000,
          0B00000000,
          0B00111100,
          0B00111100,
          0B00111100,
          0B00111100,
          0B00000000,
          0B00000000,
        }
    };

    void setup() {
        pinMode(pLatchPin, OUTPUT);
        pinMode(pClockPin, OUTPUT);
        pinMode(pDataPin, OUTPUT);

        pinMode(gLatchPin, OUTPUT);
        pinMode(gClockPin, OUTPUT);
        pinMode(gDataPin, OUTPUT);

        registerWrite(gLatchPin, gClockPin, gDataPin, 0B00000000);
        Timer1.initialize(10000);
        Timer1.attachInterrupt(matrixUpdate);
    }

    void matrixUpdate() {
        for(int i = 0; i < 8; i++) {
             registerWrite(pLatchPin, pClockPin, pDataPin, 1 << i);
             registerWrite(gLatchPin, gClockPin, gDataPin, icons[n][i]);
        }
    }

    void loop() {
        n = 1 - n;
        delay(1000);
    }

    void registerWrite(int latchPin, int clockPin, int dataPin, byte data) {
         digitalWrite(latchPin, LOW);
         shiftOut(dataPin, clockPin, MSBFIRST, data);
         digitalWrite(latchPin, HIGH);
    }

You can see from the code listing, (and probably from the image as well) that I ended up using two
8-bit latches.  I could have used less pins and cascaded the latches into a single 16-pin logical
latch… but I didn’t out of lazyness.

The other thing of note in this code listing is the TimeOne library.  I had to grab it from the
[google code project](http://code.google.com/p/arduino-timerone/downloads/list). I was pretty
surprised that you could schedule an interrupt driven timer at microsecond granularity.  Pretty
amazing.

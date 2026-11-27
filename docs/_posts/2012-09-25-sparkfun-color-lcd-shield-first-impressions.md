---
layout: post
title: SparkFun Color LCD Shield – First Impressions
date: '2012-09-25'
author: Richard Lee
permalink: /2012/09/25/sparkfun-color-lcd-shield-first-impressions/
legacy_archive: true
archive_source: https://web.archive.org/web/20131021005409/http://rl337.org/2012/09/25/sparkfun-color-lcd-shield-first-impressions/
archive_original_timestamp: '2012-09-25T21:32:57+00:00'
categories:
- arduino-2
tags:
- arduino
- electronics
- lcd
- sparkfun
---

[![IMG_0935](/assets/images/legacy-blog/2012/09/IMG_0935-e1348631879326-300x225.jpg.webp)](/assets/images/legacy-blog/2012/09/IMG_0935-e1348631879326.jpg.webp)

I
picked up a [SparkFun Color LCD Shield](https://www.sparkfun.com/products/9363) while I was shopping
for some sensors and battery packs.  I thought that maybe I could use it to help visualize sensor
data prior to passing it off to my [Raspberry Pi](http://www.raspberrypi.org/).

The shield itself didn’t come with headers… which is okay, because I had a [few
extra](https://www.adafruit.com/products/85) from a purchase I made from
[adafruit](http://adafruit.com/). A short solder job later, It’s plugged into my
[Uno](http://arduino.cc/en/Main/ArduinoBoardUno).

I grabbed the [Arduino
library](https://github.com/downloads/jimblom/ColorLCDShield/ColorLCDShield-July-16-2012.zip) from
[github](https://github.com), plugged it in and tried to run the examples.  Initially, the board
didn’t seem to function, but after reading the documentation a little more, I realized that
[sparkfun](https://www.sparkfun.com/) ships one of two different models. I happened to get one that
didn’t run with the default code. The change to the examples is extremely trivial.  You change the
following line:

    lcd.init(EPSON);

to

    lcd.init(PHILLIPS);

One thing that I noticed about the shield… the updating is very slow, so you have to be extremely
mindful of how you want to change your pixels. Simply clearing the display has a visible redraw. I
wrote a short program to play around with the buttons on the shield. Essentially, it just draws or
undraws rectangles based on whether or not buttons are pressed. Here’s the code itself.  If you try
it out, you can see what I mean about the redraw rate.  Either this is an artifact of the
[sparkfun](https://www.sparkfun.com/) library or it’s a limitation of the device itself. I guess I
can look at the library and see if there’s anything obvious.

    #include <ColorLCDShield.h>
    LCDShield lcd;

    byte cont = 40;  // Good center value for contrast
    int lastS1 = 0;
    int lastS2 = 0;
    int lastS3 = 0;

    void setup() {
      pinMode(3, INPUT);
      digitalWrite(3, HIGH);
      pinMode(4, INPUT);
      digitalWrite(4, HIGH);
      pinMode(5, INPUT);
      digitalWrite(5, HIGH);

      lcd.init(PHILLIPS);
      lcd.contrast(cont);
    }

    void loop() {
      int s1 = digitalRead(3);
      int s2 = digitalRead(4);
      int s3 = digitalRead(5);

      if (s1 == lastS1 && s2 == lastS2 && s3 == lastS3) {
          return;
      }

      if (s1 != lastS1) {
        if (s1) {
          lcd.setRect(80, 35, 131, 51, 1, WHITE);
        } else {
          lcd.setRect(80, 35, 131, 51, 1, CYAN);
        }
        lastS1 = s1;
      }

      if (s2 != lastS2) {
        if (s2) {
          lcd.setRect(80, 67, 131, 83, 1, WHITE);
        } else {
          lcd.setRect(80, 67, 131, 83, 1, MAGENTA);
        }
        lastS2 = s2;
      }

      if (s3 != lastS3) {
        if (s3) {
          lcd.setRect(80, 99, 131, 115, 1, WHITE);
        } else {
          lcd.setRect(80, 99, 131, 115, 1, BLUE);
        }
        lastS3 = s3;
      }
    }

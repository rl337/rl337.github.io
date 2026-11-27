---
layout: post
title: An Arduino general purpose detector!
date: '2011-12-18'
author: Richard Lee
permalink: /2011/12/18/an-arduino-general-purpose-detector/
legacy_archive: true
archive_source: https://web.archive.org/web/20120103185442/http://rl337.org/2011/12/18/an-arduino-general-purpose-detector/
archive_original_timestamp: '2011-12-18T05:15:32+00:00'
tags:
- arduino
---

Originally published on 2011-12-18.

[View the Wayback capture][legacy-source].

[legacy-source]: https://web.archive.org/web/20120103185442/http://rl337.org/2011/12/18/an-arduino-general-purpose-detector/




I’ve been spending some time getting acquainted with my new [Arduino
Uno](http://arduino.cc/en/Main/ArduinoBoardUno).

I did the first [Blinking LED](http://arduino.cc/en/Tutorial/Blink) tutorial which went exactly as
expected.  This particular board has a built-in LED connected to pin 13, so I didn’t even need to do
any wiring!

Having forced the on-board LED to blink, I decided to get a little more ambitious.  Along with my
Arduino, I bought a [bag of
LEDs](http://www.microtivity.com/p/IL083/5mm-assorted-led-w-resistors-3-colors-pack-of-30) which
came with the appropriate resistors for building simple circuits with the board I have.  I attached
a 2nd LED to a small [Bread Board](http://en.wikipedia.org/wiki/Bread_board) and wired it up to pin
12.  After modifying the program a little bit, I got the two LEDs to alternate blinking.

Not wanting to stop at using only 2 LEDs, I strung up 5 more to the Bread Board and connected each
to a corresponding pin from 7 to 11.  With everything wired up, I coded up a simple function that
would take a number from 0-6 and light up an appropriate number of LEDs.  0 leds if 0 were passed
and 6 if six was passed.  You can see that segment of the code here:

    void light(int i) {

      if(i < 0) { i = 0; }
      if (i > 6) {  i = 6; }

      for(int j = 0; j < 6; j++) {
         int reg = 12 - j;
         if (j < i) {
            digitalWrite(reg, HIGH);
         } else {
           digitalWrite(reg, LOW);
         }
      }
    }

The first time running it, I simply cycled through numbers from 0 to 7 which resulted in the LEDs
lighting up one at a time then resetting.

Finally, I decided to mess around with the Arduino’s [Analog Input
capabilities](http://arduino.cc/en/Tutorial/AnalogReadSerial).  The input seems quite sensitive
because as I touched the wire that I connected to the input, it immediately began registering a
voltage.   In my program’s main loop, I scaled the analog input to the 0-7 range of my LED array.
Now when I touch the wire, the more fingers I touch the wire with… the more LEDs light up!  Here’s
the pic!

[![IMG_0391](/assets/images/legacy-blog/2011/12/IMG_0391-1024x764.jpg.webp)](/assets/images/legacy-blog/2011/12/IMG_0391.jpg.webp)

Here,
I was holding the wire with three fingers; my thumb, pointer  and middle finger… four of the LEDs
lit up.  Presumably, if I connect up any random sensor (light, sound, etc), the intensity will light
up a corresponding set of LEDs.  That aught to be more useful than detecting fingers touching a
wire.

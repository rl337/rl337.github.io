---
layout: post
title: Controlling 6 LEDs with only 3 pins
date: '2012-03-06'
author: Richard Lee
permalink: /2012/03/06/controlling-6-leds-with-only-3-pins/
legacy_archive: true
archive_source: https://web.archive.org/web/20120308111928/http://rl337.org/2012/03/06/controlling-6-leds-with-only-3-pins/
archive_original_timestamp: '2012-03-06T08:00:21+00:00'
categories:
- arduino-2
tags:
- demultiplexer-led-inverter
---

Originally published on 2012-03-06.

[View the Wayback capture][legacy-source].

[legacy-source]: https://web.archive.org/web/20120308111928/http://rl337.org/2012/03/06/controlling-6-leds-with-only-3-pins/




The [Arduino Uno](http://arduino.cc/en/Main/ArduinoBoardUno) has something like 13 [digital I/O
pins](http://arduino.cc/en/Tutorial/DigitalPins) and 5 [analog I/O
pins](http://arduino.cc/en/Tutorial/AnalogInputPins) which can be re-tasked to act like digital pins
bringing the grand total of 18 possible Digital I/O pins to work with… so what happens when you need
to work with more than 18 different devices?  For example… what if you wanted to independently
strobe 19
[LEDs](http://www.microtivity.com/p/IL083/5mm-assorted-led-w-resistors-3-colors-pack-of-30)?


[![IMG_0623](/assets/images/legacy-blog/2012/03/IMG_0623-300x224.jpg.webp)](/assets/images/legacy-blog/2012/03/IMG_0623.jpg.webp)

Here, I've connected 3 LEDs directly to the Arduino UNO's digital I/O pins 2,3 and 4. In this
configuration, I could control at most 18 LEDs independently.


I’ve come up with a project which faces just such a problem… I want to be able to independently
light up and update 32+ little [20×2
LCDs](http://www.jameco.com/webapp/wcs/stores/servlet/ProductDisplay?storeId=10001&productId=2115469&catalogId=10001)
with a single Arduino.  To give a little context, each LCD has 16 pins, 8 of which are data pins.
This means that 8 of the 18 digital out pins from the Arduino must be used for sending data to the
LCD.  That hardly seems like more than one could possibly be driven by a single Arduino!  Clearly,
if my plan is to be realized, I need to come up with a scheme that doesn’t involve directly driving
all the LCDs from the Digital I/O pins.

Remembering back to my Structural Computer Organization class, I realized the answer:
[Demultiplexing](http://en.wikipedia.org/wiki/Demultiplexer).


[![IMG_0615](/assets/images/legacy-blog/2012/03/IMG_0615-300x224.jpg.webp)](/assets/images/legacy-blog/2012/03/IMG_0615.jpg.webp)

Here, I'm controlling 6 LEDs with only 3 pins through a 3-8 multiplexer. Chaining multiplexers
together, I could control 2^N LEDs with N pins.


A Demultiplexer or Decoder is a component made up of logic gates that takes a combination of inputs
and chooses a corresponding output.  Generally, for you can choose from 2^N outputs with N inputs.
Learning about them in class is one thing.. but actually sticking them on a breadboard is another.
I chose this Demultiplexer: the
[HD74LS138P][archive-link-1].
It’s a 3-input 8-output multiplexer. It turns out, though that it works counter to how I expected it
to.. instead of the selected output being high, the selected output was low and the other outputs
were high.  When I hooked it up to my LEDs… all of the LEDs were on except for the one currently
being selected!


[![IMG_0609](/assets/images/legacy-blog/2012/03/IMG_0609-300x224.jpg.webp)](/assets/images/legacy-blog/2012/03/IMG_0609.jpg.webp)

Using a hex inverter, I was able to invert the outputs of the Decoder and make the selected output
be on while having the other outputs stay off.


Ok… well, If I want the unselected outputs to be low while the selected is high, I need to invert
the output of the multiplexer.  It turns out that there are little chips that have a bunch of
[inverters](http://en.wikipedia.org/wiki/Inverter_%28logic_gate%29) built into them.  The popular
form factor seems to be the “Hex Inverter” which is simply 6 inverters crammed into a 14-pin
package.  I ended up using a
[MC54F04](https://www.jameco.com/webapp/wcs/stores/servlet/Product_10001_10001_287005_-1) to do it.
It seems like every semiconductor makes identical hex inverters, so
[Jameco](http://www.jameco.com/)‘s catalog just says “popular manufacturer”.  Anyhow, you can see
from the photo to the left, using the inverters, we now have selected output being on and unselected
outputs being off.

If you’re curious about the code that I used for this setup? Here it is.. It’s pretty simple:

    int count = 0;
    int values[8][3] = {
       { LOW, LOW, LOW },
       { LOW, LOW, HIGH },
       { LOW, HIGH, LOW },
       { LOW, HIGH, HIGH },
       { HIGH, LOW, LOW },
       { HIGH, LOW, HIGH },
       { HIGH, HIGH, LOW },
       { HIGH, HIGH, HIGH },
    };

    void setup() {
      pinMode(2, OUTPUT);
      pinMode(3, OUTPUT);
      pinMode(4, OUTPUT);
    }

    void loop() {
      count = (count + 1) % 8;
      digitalWrite(2, values[count][0]);
      digitalWrite(3, values[count][1]);
      digitalWrite(4, values[count][2]);
      delay(1000);
    }

In the setup method, we say that pins 2, 3, and 4 are assigned output roles.  In the loop, we
increment our count variable and if the count exceeds 7, it gets set back to 0.  We then set our
pins HIGH or LOW depending on the count’s offset in our table of values.   We also put a 1 second
delay between loop executions so that the loop doesn’t happen too quickly to see.

One kind of annoying problem that I ran into while stringing up my Decoder was, it has 3 pins called
G1, G2a and G2b which are effectively enable pins.  G1 must be HIGH and BOTH G2a and G2b must be
ACTIVELY LOW in order for the demultiplexer to work.  I didn’t realize it and only connected G2a to
ground… so naturally nothing worked because G2b was not actively being set to LOW (not directly
connected to ground).  It wasn’t until I grounded both pins, that the decoder started decoding.


[archive-link-1]: https://www.jameco.com/webapp/wcs/stores/servlet/ProductDisplay?storeId=10001&productId=46608&langId=-1&catalogId=10001

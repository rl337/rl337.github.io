---
layout: post
title: Controlling multiple LCDs from one Arduino
date: '2012-03-20'
author: Richard Lee
permalink: /2012/03/20/controlling-multiple-lcds-from-one-arduino/
legacy_archive: true
archive_source: https://web.archive.org/web/20120322020303/http://rl337.org/2012/03/20/controlling-multiple-lcds-from-one-arduino/
archive_original_timestamp: '2012-03-20T05:13:13+00:00'
categories:
- arduino-2
tags:
- demultiplexer
- hexinverter
- lcd
---

Originally published on 2012-03-20.

[View the Wayback capture][legacy-source].

[legacy-source]: https://web.archive.org/web/20120322020303/http://rl337.org/2012/03/20/controlling-multiple-lcds-from-one-arduino/




[![IMG_0641](/assets/images/legacy-blog/2012/03/IMG_0641-300x224.jpg.webp)](/assets/images/legacy-blog/2012/03/IMG_0641.jpg.webp)

Taking
the [previous Arduino
project](/2012/03/06/controlling-6-leds-with-only-3-pins/) a
step further, I managed to get two
[LCDs](https://www.jameco.com/webapp/wcs/stores/servlet/Product_10001_10001_2115469_-1)
independently updating from a single Arduino.  My original plan was to have 4 of them updating
independently, but two of the cables that I made for connecting the LCDs to my
[breadboard](http://en.wikipedia.org/wiki/Breadboard) somehow stopped working.  I suspect that
[14-pin header](https://www.jameco.com/webapp/wcs/stores/servlet/Product_10001_10001_153948_-1)
stopped making contact with one or more of its pins.

[![IMG_0644](/assets/images/legacy-blog/2012/03/IMG_0644-224x300.jpg.webp)](/assets/images/legacy-blog/2012/03/IMG_0644.jpg.webp)

You
can see in the image to the right, how I constructed this cable.  It’s essentially a [ribbon
cable](https://www.jameco.com/webapp/wcs/stores/servlet/Product_10001_10001_644156_-1) that I cut
down 14-pins wide.  On one end I connected the [14-pin
header](https://www.jameco.com/webapp/wcs/stores/servlet/Product_10001_10001_153948_-1) and at the
other, I connected a series of [Molex
connectors][archive-link-1].
I chose the to break the wire into three groups of four pins plus a single group of two.  The group
of two corresponds to the Power and Ground of the LCD.  The first group of 4 has the LCD’s RW, RS,
Enable, and Contrast pins.  The final two groups of four end up being the data pins. (In four pin
mode, only the second group of data pins are used).

[![IMG_0640](/assets/images/legacy-blog/2012/03/IMG_0640-300x224.jpg.webp)](/assets/images/legacy-blog/2012/03/IMG_0640.jpg.webp)

If you look at the assembly from above, you can see that on the larger breadboard, I have a similar
setup to my [previous project’s
setup](/2012/03/06/controlling-6-leds-with-only-3-pins/).
Essentially, I have a [3-8 Demultiplexer](http://en.wikipedia.org/wiki/Demultiplexer) and a [Hex
inverter](http://en.wikipedia.org/wiki/Inverter_%28logic_gate%29).  The input to the Demultiplexer
comes from the digital out pins from the Arduino and the outputs run through inverters.  I connect
the inverted values to the “G1″ of the LCD which, when set to LOW disables writing to the LCD.
Since I know that the inverted output of the demuxer will only ever have a single line set HIGH, I
can use it to select which LCD to enable.  The other LCD pins are all connected in parallel to the
controlling pins on the Arduino.

    #include <LiquidCrystal.h>

    LiquidCrystal lcd(11, 9, 5, 4, 3, 2);
    int state;

    void setup() {
      pinMode(12, OUTPUT);
      pinMode(10, OUTPUT);

      // Pin 6 controls which LCD. If I had more than
      // two LCDs, I would need more pins to select them
      pinMode(6, OUTPUT);

      state = 0; // Pin 6's value 0 -> LOW, 1 -> HIGH

      // Initialize the first LCD
      digitalWrite(6, LOW);
      lcd.begin(20, 2);
      lcd.print("I am Tweedle Dee!");

      // Select and initialize the 2nd LCD
      digitalWrite(6, HIGH);
      lcd.begin(20, 2);
      lcd.print("I am Tweedle Dum!");
    }

    void loop() {
      digitalWrite(6, state == 0 ? LOW : HIGH);
      lcd.setCursor(0, 1);
      lcd.print(millis()/1000);
      delay(1000);

      state = 1 - state; // toggle which LCD to display on
    }

The program itself was based heavily on the LCD Hello World example.  I changed a couple of pins
around to be more convenient for my wiring… but the loop() function was copied almost verbatim.  The
intent of the program was to have one LCD display “I am Tweedle Dee!” and the other to display “I am
Tweedle Dum!” then Tweedle Dee will start counting all even numbers while Tweedle Dum counts all odd
numbers.  As you can see here… it worked out fairly well!

[![IMG_0643](/assets/images/legacy-blog/2012/03/IMG_0643-1024x764.jpg.webp)](/assets/images/legacy-blog/2012/03/IMG_0643.jpg.webp)


[archive-link-1]: https://www.jameco.com/webapp/wcs/stores/servlet/StoreCatalogDrillDownView?langId=-1&storeId=10001&catalogId=10001&categoryName=cat_3040&subCategoryName=Interconnects%20%2F%20Rectangular%20Connectors%20%2F%20Discrete%20Wire%20Housing&category=304090&refine=1&position=1&history=8vfb1qat%7CsubCategoryName~Interconnects%5Ecategory~30%5EcategoryName~category_root%5EprodPage~15%5Epage~SEARCH%252BNAV%402ljbuj6b%7Ccategory~3040%5EcategoryName~cat_30%5Eposition~1%5Erefine~1%5EsubCategoryName~Interconnects%2B%252F%2BRectangular%2BConnectors%5EprodPage~15%5Epage~SEARCH%252BNAV%40zabjogsc%7CrefineValue~MOLEX%2BINC.%5ErefineType~1%5Eposition~1%5Esub_attr_name~Manufacturer%5Erefine~1%5EprodPage~15%5Epage~SEARCH%252BNAV

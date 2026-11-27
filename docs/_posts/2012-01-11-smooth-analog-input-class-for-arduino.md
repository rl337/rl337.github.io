---
layout: post
title: Smooth Analog Input Class for Arduino
date: '2012-01-11'
author: Richard Lee
permalink: /2012/01/11/smooth-analog-input-class-for-arduino/
legacy_archive: true
archive_source: https://web.archive.org/web/20120113230753/http://rl337.org/2012/01/11/smooth-analog-input-class-for-arduino/
archive_original_timestamp: '2012-01-11T17:51:24+00:00'
categories:
- arduino-2
---

Originally published on 2012-01-11.

[View the Wayback capture][legacy-source].

[legacy-source]: https://web.archive.org/web/20120113230753/http://rl337.org/2012/01/11/smooth-analog-input-class-for-arduino/




[![IMG_0465](/assets/images/legacy-blog/2012/01/IMG_0465-1024x764.jpg.webp)](/assets/images/legacy-blog/2012/01/IMG_0465.jpg.webp)

In
the above photo, you see my [Arduino Uno](http://arduino.cc/en/Main/ArduinoBoardUno) with a
[mini-breadboard](http://www.makershed.com/Mini_Breadboards_p/mkkn1.htm)
[ProtoShield](http://arduino.cc/en/Main/ArduinoProtoShield).

Here, I wired it up to accept data from a
[potentiometer](http://en.wikipedia.org/wiki/Potentiometer) on analog input A0.  I also have a
[standard servo](http://en.wikipedia.org/wiki/Servo_%28radio_control%29) connected to digital pin
7.  The point of this is, you turn the potentiometer, it produces a corresponding motion in the
servo.

Here’s the initial code that I used for making this happen:

    #include

    Servo servo;
    int last;
    void setup() {
        servo.attach(7);
        Serial.begin(9600);
        last = -1;
    }

    void loop() {
      int current = analogRead(A0);
      int scaled = map(current, 0, 1024, 0, 180);
      if (scaled != last) {
        last = scaled;
        Serial.println(scaled);
        servo.write(scaled);
      }
    }

Pretty simple stuff.  You see I attach he Servo object to pin 7 and within the loop() section, read
from A0, scale the value, then write it to the servo! It works!

One kind of annoying thing that I noticed was… the input from the potentiometer wasn’t terribly
stable.  Even when it was just sitting there, it would output values that were up to plus/minus 5.
Because of this, my servo was constantly twitching.  Not only is that probably not good for the
servo, you could constantly hear it too… so it was annoying.

It turns out that in one of the Arduino [Tutorials](http://arduino.cc/en/Tutorial/HomePage), they
talk about [analog input smoothing](http://arduino.cc/en/Tutorial/Smoothing).  Essentially, you take
10 readings and average them.  That’ll give you a more stable value.  The problem with using the
code from the tutorial is, it’s ungainly.  It would be nice if we could create an object, attach it
to A0 and have it automatically smooth incoming values for us… well, that’s what I wrote!

You can grab the actual code from here:
<http://github.com/rl337/incubator/tree/master/main/arduino/libraries/SmoothAnalogInput>

The prototype for the object looks like this:

    #define SMOOTH_ANALOG_INPUT_SIZE 32

    class SmoothAnalogInput {
        public:
            SmoothAnalogInput();
            void attach(int pin);
            void scale(int min, int max);
            int read();
            int raw();

    };

The object smooths data over 32 samples. You attach() the object to whatever pin you want it to
smooth input for, in our case, A0. the raw() method takes a reading and returns the raw value from
the analog input. the read() method returns the smoothed result which can be automatically scaled
between a min/max value if you call the scale() method. Here’s the program reworked to use the
SmoothAnalogInput object

    #include
    #include

    Servo servo;
    SmoothAnalogInput ai;
    int last;
    void setup() {
      Serial.begin(9600);
      servo.attach(7);
      ai.attach(A0);
      last = -1;
    }

    void loop() {
      int sensorReading = ai.read();

      int scaled = map(sensorReading, 0, 1024, 0, 180);
      if (scaled != last) {
        last = scaled;
        Serial.println(scaled);
        servo.write(scaled);
      }
    }

Looking at the Serial Monitor, there are still a few cases where the servo fidgets, but by and
large, the values become stable quickly after you stop moving the potentiometer.

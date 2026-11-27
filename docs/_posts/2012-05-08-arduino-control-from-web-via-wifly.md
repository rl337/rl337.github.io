---
layout: post
title: Arduino Control from Web via WiFly
date: '2012-05-08'
author: Richard Lee
permalink: /2012/05/08/arduino-control-from-web-via-wifly/
legacy_archive: true
archive_source: https://web.archive.org/web/20120521180219/http://rl337.org/2012/05/08/arduino-control-from-web-via-wifly/
archive_original_timestamp: '2012-05-08T16:45:38+00:00'
categories:
- arduino-2
---

[![IMG_0691](/assets/images/legacy-blog/2012/05/IMG_0691-300x224.jpg.webp)](/assets/images/legacy-blog/2012/05/IMG_0691.jpg.webp)

I
bought a [WiFly a while
back](/2012/03/29/wifly-shield-off-to-a-rough-start/) but didn’t
really do much with it.  For those of you not in the know, a
[WiFly](http://www.sparkfun.com/products/9367) is a compact wireless device that you can buy on a
little break-out board… or in this case, on an [Arduino
Shield](http://arduino.cc/en/Main/ArduinoShields).

The interface to the WiFly is pretty straight forward.  You initialize the library then create a
Client object.  This Client object has typical filehandle-like methods such as read(), available(),
println() etc.

In this example, I took my [previous setup with 8-bit
latches](/2012/05/02/monkeying-with-8-bit-latches/) and used the LEDs
to display output that I submitted to a webservice using the WiFly.  The Webservice in question is a
very simple php app that returns a single 8-bit hex number.  Here’s the code:

    <?php print '@'.dechex(time() % 255); ?>

The prepended ‘@’ sign is a flag value.  Because read() returns just a single char, I wanted to skip
through all of the http header information to the data.  I stop when I encounter the first ‘@’.

I modified the latch setup I had by using two triplets of pins instead of sharing the single
triple.  This allowed me to independently control two latches. Here’s the final code for the
project:

    #include "WiFly.h"

    int latchPin1 = 2;
    int clockPin1 = 3;
    int dataPin1 = 4;

    int latchPin2 = 5;
    int clockPin2 = 6;
    int dataPin2 = 7;

    Client client("www.tokyo3.com", 80);

    void setup() {
      Serial.begin(9600);
      pinMode(latchPin1, OUTPUT);
      pinMode(clockPin1, OUTPUT);
      pinMode(dataPin1, OUTPUT);

      pinMode(latchPin2, OUTPUT);
      pinMode(clockPin2, OUTPUT);
      pinMode(dataPin2, OUTPUT);

      WiFly.begin();

      if (!WiFly.join("ssid", "password")) {
        Serial.println("Association failed.");
        while (1) {
          // Hang on failure.
        }
      }
    }

    int convert(char ch) {
        if (ch >= '0' && ch <= '9') {
             return ch - '0';
        }
        if (ch >= 'a' && ch <= 'f') {
             return ch - 'a' + 10;
        }
        return 0;
    }

    int getWebValue() {
      if (!client.connected()) {
          Serial.println("Connecting...");
          if (!client.connect()) {
            return 0;
          }
      }

      client.println("GET /arduino.php HTTP/1.1");
      client.println("Host: www.tokyo3.com");
      client.println();

      char ch;
      while (client.available()) {
        ch = client.read();
        Serial.print(ch);
        if (ch == '@') {
          break;
        }
      }

      if (!client.available()) {
         return 0;
      }

      int a = convert(client.read());
      int b = convert(client.read());

      return (a << 4) + b;
    }

    int count = 0;
    void loop() {
        int a = getWebValue();

        if (count++ % 2 == 0) {
            digitalWrite(latchPin1, LOW);
            shiftOut(dataPin1, clockPin1, MSBFIRST, a);
            digitalWrite(latchPin1, HIGH);
        } else {
            digitalWrite(latchPin2, LOW);
            shiftOut(dataPin2, clockPin2, MSBFIRST, a);
            digitalWrite(latchPin2, HIGH);
        }
        delay(1000);
    }

Pretty simple for the most part.  As with the WiFly examples, I use the Serial Monitor to echo
print.  Very useful when trying to figure out what you’re getting via network.

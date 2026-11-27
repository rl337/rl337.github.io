---
layout: post
title: Anatomy of a Robot
date: '2013-03-20'
author: Richard Lee
permalink: /2013/03/20/anatomy-of-a-robot/
legacy_archive: true
archive_source: https://web.archive.org/web/20130504071221/http://rl337.org/2013/03/20/anatomy-of-a-robot/
archive_original_timestamp: '2013-03-20T00:14:12+00:00'
categories:
- arduino-2
- ml
---

Originally published on 2013-03-20.

[View the Wayback capture][legacy-source].

[legacy-source]: https://web.archive.org/web/20130504071221/http://rl337.org/2013/03/20/anatomy-of-a-robot/




A while back, I wrote a [blog post](/2011/12/13/spherical-robots-and-arduino-uno/) about [spherical
robots](http://www.google.com/?q=spherical+robot).   I had taken it upon myself to learn a bit more
about [robotics](http://en.wikipedia.org/wiki/Robotics) with the intention of building a simple
[autonomous robot](http://en.wikipedia.org/wiki/Autonomous_robot).  Well, over two years later, I’m
at a point where I can do some actual robotics work.  I look back on what I’ve learned… and the
rabbit hole of a trek that led me here.

## The Coursera Rabbit Hole

![mindstormbrick](/assets/images/legacy-blog/2013/03/mindstormbrick.jpg.webp)

What goes into a robot?  Well, naively I thought that you hook up servos and sensors tosome kind of
micro controller and away you go.  It’s the [Lego
Mindstorms](http://mindstorms.lego.com/en-us/default.aspx) version of Robotics.  Of course, that
\*IS\* one way to look at robots… but really, that’s just the beginning… the “Hello World” program
of building robots.  I wanted to build something a little more sophisticated than the “recommended
age 12-adult” crowd.

[![itunes-artwork](/assets/images/legacy-blog/2013/03/itunes-artwork.jpg.webp)](https://www.coursera.org/course/conrob)Well,
for the answer we look to the [Control of Mobile Robots](https://www.coursera.org/course/conrob)
class offered on [Coursera](https://www.coursera.org).  In this class, [Dr. Magnus
Egerstedt](http://users.ece.gatech.edu/~magnus/) introduces [Control
Systems](http://en.wikipedia.org/wiki/Control_systems).  The class itself does not get into the
hardware of building robots, but digs into the abstraction layers necessary for successfully
modeling and controlling things that interact with the real world. [Archived resource](https://www.coursera.org/university/gatech)

What exactly do I mean when I say “Control things?” Well, think about yourself for a moment.  If
you’re standing and someone shoves you, you are able to react in a way to keep yourself stable and
standing… or simply put you’re in control of your body.  The act of keeping yourself upright is a
complex set of muscle movements that need to be carried out correctly but you don’t need to think
about how to control each muscle… you just do it.  The instinctive impulse to lean or step is
handled by your innate control system.

[![itunes-artwork](/assets/images/legacy-blog/2013/03/itunes-artwork1.jpg.webp)](https://www.coursera.org/course/aiplan)It’s
not enough, however, for a robot to be “controllable”.  My goal is to build a robot that’s
[autonomous](http://www.merriam-webster.com/dictionary/autonomous).   That requires some form of
higher level artificial intelligence.  It turns out that Coursera offers another class geared toward
exactly this: [Artificial Intelligence Planning](https://www.coursera.org/course/aiplan)!  In this
class, Dr. Gerhard Wickler and Professor Austin Tate take you through a survey of programmatic
problem solving algorithms.  I was amused to learn that like all other [computer
science](http://en.wikipedia.org/wiki/Computer_science) problem, artificial intelligence problem
solving comes down to a search algorithm.

At the end of this course, you’ll be able to write a program that given some set of circumstances
and corresponding set of possible actions, it will figure out what to do to accomplish its goals;
assuming that some possible set of actions can achieve the goal.

[![small-icon.hover](/assets/images/legacy-blog/2012/05/small-icon.hover_-150x135.png.webp)](/assets/images/legacy-blog/2012/05/small-icon.hover_.png.webp)

This
lead me to the next problem… perception.  An autonomous robot has sensors and it needs to be able to
figure out some “state” of the universe in order for it to use its problem solving capabilities.
 How on earth do you map images/sounds/echolocation to logical states of the universe?  Through
machine learning.  As it turns out, Coursera offers a LOT of classes on exactly this.  The most
notable of these classes is [Coursera’s co-founder](http://en.wikipedia.org/wiki/Andrew_Ng)‘s class
on Machine learning…  Here, you learn all kinds of algorithms for automatically classifying and
identifying logical states based on noisy or confusing input.

[![itunes-artwork](/assets/images/legacy-blog/2013/03/itunes-artwork2.jpg.webp)](/assets/images/legacy-blog/2013/03/itunes-artwork2.jpg.webp)

A
more advanced class that I really enjoyed focused on state of the art [Neural
Networks](http://en.wikipedia.org/wiki/Neural_networks).  The class is called [Neural Networks for
Machine Learning](https://www.coursera.org/course/neuralnets) and is taught by [Dr. Geoffrey
Hinton](http://en.wikipedia.org/wiki/Geoffrey_Hinton).  This class goes into great depth on various
kinds of Neural Networks.  This class totally blew my mind.  I have no doubt that the correct
application of neural nets with the right kind of self-motivating planner will lead to formidable
AIs.

## Putting it all together

First let’s talk about hardware.  Below is a list of hardware that I’m going to use and I’ll
parallel it with what I feel may be the human anatomy counter-part.

[![IMG_0465](/assets/images/legacy-blog/2013/03/IMG_0465-e1363761692520-150x150.jpg.webp)](http://arduino.cc/en/Main/arduinoBoardUno)I’m
going to use an [Arduino Uno](http://arduino.cc/en/Main/arduinoBoardUno) as the primary interface
with all of my robot’s actuators.  It represents the spinal cord and instinctive nervous system of
the robot.   The Arduino is a very simple microcontroller that isn’t terribly fast.  It also doesn’t
have much in the way of memory.  It does have extremely easy interfaces with motors and sensors.
 This makes it ideal for running a [closed loop
System](http://en.wikipedia.org/wiki/State_space_(controls)). (See Control of Mobile Robots class
for details).

[![raspberrypi](/assets/images/legacy-blog/2012/08/raspberrypi-150x150.jpg.webp)](http://en.wikipedia.org/wiki/Raspberry_Pi)Connected
to the Arduino will be a [Raspberry Pi](http://en.wikipedia.org/wiki/Raspberry_Pi). The Pi will be
the brains of the Robot. All higher order problem solving will occur here.  The brain and the spinal
cord will talk to each other using
[SPI](http://en.wikipedia.org/wiki/Serial_Peripheral_Interface_Bus).  Naturally the Raspberry Pi
will be the master of the SPI bus.  As the robot gets more complex, it might be necessary to attach
more than one microcontroller (maybe not all arduinos)… especially if I start working with more
complex sensors.

[![shapelock](/assets/images/legacy-blog/2013/03/shapelock-150x150.jpg.webp)](http://shapelock.com/)The
supports and overall skeleton of my robot will be created with [Shape Lock](http://shapelock.com/).
 It’s a material that can be melted, shaped and re-used over and over.  It claims to be machinable
(using my dremmel) and durable.  I imagine that if I need stronger load bearing parts, I can
prototype in shape lock and carve some other material based on the prototype.  Wood is a likely
candidate.

Okay. The big pieces are out of the way.  Now the fun stuff.  What sensors / servos will I use?  I
have a variety of electric motors, solenoids and steppers that I picked up from
[Adafruit](http://adafruit.com/). It’s likely that my first robot will be a simple differential
drive deal.. but eventually I’d like to go back to my ideas in the original blog post and create a
spherical robot.   In the end, the actual drive system and sensors don’t matter that much… they’re
just the accessories of the Mr. Potato head.  All interchangeable.

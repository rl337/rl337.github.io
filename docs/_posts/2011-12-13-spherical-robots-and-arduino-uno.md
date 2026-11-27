---
layout: post
title: Spherical Robots and Arduino Uno!
date: '2011-12-13'
author: Richard Lee
permalink: /2011/12/13/spherical-robots-and-arduino-uno/
legacy_archive: true
archive_source: https://web.archive.org/web/20120103185858/http://rl337.org/2011/12/13/spherical-robots-and-arduino-uno/
archive_original_timestamp: '2011-12-13T16:29:24+00:00'
tags:
- arduino
- robots
---

Back in November, I was at the [Academy of Science](http://www.calacademy.org) for
[Nightlife](http://www.calacademy.org/events/nightlife/) and found nestled in the creepy taxidermy
([African Hall](http://www.calacademy.org/academy/exhibits/nat_history/)), I ran into Spherical
Robots rolling around. Check out the video:

[Original embedded media](http://www.youtube.com/embed/pLPOUVHUgcQ)

This particular [set of robots](http://orbswarm.com/) were originally created for [Burning
Man](http://www.burningman.com/), but it’s no surprise to me that they would tour around the more
sciency venues of San Francisco.  I’d never really considered a spherical robot before… but I guess
it’s a “thing”.  Go ahead! [Google it](http://www.google.com/?q=spherical+robot)!

Now to me, the easiest way to get a sphere moving would be to have a rod running through an axis of
the ball and you roll around it using either weight or a
[gyroscope](http://en.wikipedia.org/wiki/Gyroscope) on whatever internal mechanism you’ve got
driving.  In this design you effectively have one HUGE wheel. These robots, however did not seem to
do that.  They were able to roll in arbitrary directions.  They didn’t have to turn to change
direction.

My initial gut feeling was, it used a pair of gyroscopes offset from each other by some angle.  When
the orientation of the two gyroscopes change, the sphere’s effective [center of
gravity](http://en.wikipedia.org/wiki/Center_of_gravity) would shift causing it to move.  After
doing some reading, though, it seems like that is not the case. A more likely scenario is… you have
a large [pendulum](http://en.wikipedia.org/wiki/Pendulum) style structure which is moved around with
a pair of [solenoids](http://en.wikipedia.org/wiki/Solenoid).  This apparatus is dangled from a
stable platform.  When the pendulum is pushed in a direction by the solenoids, the center of gravity
shifts and the ball rolls.  The amount that the pendulum can move the ball is proportional to the
weight at the end of the pendulum.

[![IMG_0385](/assets/images/legacy-blog/2011/12/IMG_0385-224x300.jpg.webp)](/assets/images/legacy-blog/2011/12/IMG_0385.jpg.webp)

All
of this conjecture has lead me to conclude that I need to try it out.  So… I’m off to learn a little
bit of [robotics](http://en.wikipedia.org/wiki/Robotics).  So… how does one get started in
robotics?  One dives right in!

I’ve been wanting to work with the [Arduino](http://arduino.cc/) family of microcontrollers, and
this seems like an ideal project.  I ordered myself an [Arduino
Uno](http://arduino.cc/en/Main/ArduinoBoardUno), a couple of add-on boards and am ready to rock!

My first goal will be to familiarize myself with the [Arduino programming
language](http://arduino.cc/en/Reference/HomePage) and generally make myself comfortable with the
tools involved.

There is some soldering involved.  You can see in the above image, my new toys.  The blue circuit
board is the actual Arduino itself.  Below the magnifier is an add-on board that will allow me to
control two motors.  (some assembly required).   I have a 2nd add-on board coming which will have
add a small LCD display. I’m sure that board will be the one I play with the most (At least at
first).

Naturally, I had to try to put together the motor controls, but it seems like fate would have other
plans… Look at what happened to my soldering pencil:

[![IMG_0387](/assets/images/legacy-blog/2011/12/IMG_0387-1024x444.jpg.webp)](/assets/images/legacy-blog/2011/12/IMG_0387.jpg.webp)

Yeah.
So… a new one is on the way. I guess soldering will have to wait a few days.

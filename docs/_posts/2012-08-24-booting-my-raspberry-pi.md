---
layout: post
title: Booting my Raspberry Pi
date: '2012-08-24'
author: Richard Lee
permalink: /2012/08/24/booting-my-raspberry-pi/
legacy_archive: true
archive_source: https://web.archive.org/web/20131020213921/http://rl337.org/2012/08/24/booting-my-raspberry-pi/
archive_original_timestamp: '2012-08-24T00:00:17+00:00'
---

Originally published on 2012-08-24.

[View the Wayback capture][legacy-source].

[legacy-source]: https://web.archive.org/web/20131020213921/http://rl337.org/2012/08/24/booting-my-raspberry-pi/




[![raspberrypi](/assets/images/legacy-blog/2012/08/raspberrypi-300x300.jpg.webp)](/assets/images/legacy-blog/2012/08/raspberrypi.jpg.webp)

Yeah I spent the \$35 to get myself a [Raspberry Pi](http://www.raspberrypi.org/). Here it is!

Admittedly, It’s taken me a bit longer than I’d have expected to get it to boot.  First, I bought
the wrong USB power cable.  I thought that the connector was a “Mini-USB” but really it was a
“Micro-USB”. You’d think that with the volume of electronics I own, I’d know the difference [between
the two](http://en.wikipedia.org/wiki/Universal_Serial_Bus#Mini_and_Micro_connectors)… but you’d be
wrong.

My next folly was with the operating system.  First I tried the [Arch Linux
build](http://archlinuxarm.org/platforms/armv6/raspberry-pi), but for some reason, it didn’t copy to
my SD card properly. My instinct was that the Amazon Basics SD Card wasn’t compatible for some
reason or another, but that was a false trail.  I instead copied the recommended [Raspbian “Wheezy”
image](http://www.raspberrypi.org/downloads)… and viola! I have it booting!

[![IMG_0865](/assets/images/legacy-blog/2012/08/IMG_0865-300x225.jpg.webp)](/assets/images/legacy-blog/2012/08/IMG_0865.jpg.webp)

Here’s a screen shot part way through the boot.  The Composite Video output doesn’t seem to line up
very well with my [old Dell
monitor](http://support.dell.com/support/edocs/monitors/2005FPW/En/about.htm).

The boot process is pretty swift and the distribution automatically DHCPs a network address and
starts sshd, so it’s possible to ssh in as soon as it finishes coming up.

Once inside, I poked around a little bit. Here’s the CPU info

    pi@raspberrypi ~ $ cat /proc/cpuinfo
    Processor   : ARMv6-compatible processor rev 7 (v6l)
    BogoMIPS    : 697.95
    Features    : swp half thumb fastmult vfp edsp java tls
    CPU implementer : 0x41
    CPU architecture: 7
    CPU variant : 0x0
    CPU part    : 0xb76
    CPU revision    : 7

    Hardware    : BCM2708
    Revision    : 0002
    Serial      : 0000000048e7f498

I distinctly remember commenting that a *“100mhz computer with 128 megs of ram will always make a
good linux box.” Here’s a linux box that has way way more as far as capabilities… for \$35. Maybe
we’ve reached the future.

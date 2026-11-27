---
layout: post
title: Weirdo in a Weird Land
date: '2012-04-17'
author: Richard Lee
permalink: /2012/04/17/weirdo-in-a-weird-land/
legacy_archive: true
archive_source: https://web.archive.org/web/20120423062946/http://rl337.org/2012/04/17/weirdo-in-a-weird-land/
archive_original_timestamp: '2012-04-17T16:46:34+00:00'
---

Weirdo in a Weird Land is the working title for the slowly [progressing
game.](/2012/04/10/sdl-side-scroller-takes-shape/)

It took a while to actually get the application bundle squared away.


[![First OSX
Build](/assets/images/legacy-blog/2012/04/wiawl-128.png.webp)][archive-link-1]

Click Image to Download v0.0.1!


One of the more irritating parts of creating the bundle was referencing the image resources.  Mac
Applications are supposed to keep their data in a Contents/Resources but using the provided SDLMain,
your application’s working directory is the PARENT of the resource bundle… so you’d have to make the
assumption that the end user didn’t rename the application bundle on you and build your path
including what you think your resource bundle is named.

I modified the SDLMain a little bit, putting the working directory at the top level of the
Application Bundle.  This allows me to reference my image files as: Contents/Resources/Images/ which
is still a little ugly, but probably more reliable.  The “correct” thing to do would be to have
SDLMain expose a method which allows me to retrieve the path of individual resources.  That’s
probably a much later change though.

My most recent efforts are to get a Windows build going.  I’d like to do the up front work to make
this game cross platform.  This way, I can release builds for both Mac and PC/Win32 relatively
easily in the future.  My first attempt at creating a Win32 build was using Visual Studio 2010
Express, but I ran into a lot of strange linking issues.  The compilation process was tough too.
[cl.exe](http://en.wikipedia.org/wiki/Visual_C%2B%2B) command line compiler had radically different
invocations than [gcc](http://en.wikipedia.org/wiki/GNU_Compiler_Collection)… so it’s unlikely that
I’d be able to reuse the same Makefile. There has to be an easier way to build a windows app than
this…

The [SDL](http://libsdl.org) Tutorial suggests using [mingw32](http://www.mingw.org/) which is a
minimalist windows [toolchain](http://en.wikipedia.org/wiki/Toolchain) built on top of all GNU
tools.  This means that I \*SHOULD\* be able to reuse my Makefile and if it’s part of the tutorial…
I shouldn’t run into weird issues.  We’ll see how that pans out.  Hopefully by Thursday I’ll have a
slightly expanded build that runs on both [Windows](http://windows.microsoft.com/en-US/windows/home)
and [OSX](http://www.apple.com/macosx/)!


[archive-link-1]: https://web.archive.org/web/20120423062946/http://rl337.org/wp-content/uploads/2012/04/wiawl.zip

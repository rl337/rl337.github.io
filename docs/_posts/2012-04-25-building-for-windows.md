---
layout: post
title: Building for Windows!
date: '2012-04-25'
author: Richard Lee
permalink: /2012/04/25/building-for-windows/
legacy_archive: true
archive_source: https://web.archive.org/web/20120521180441/http://rl337.org/2012/04/25/building-for-windows/
archive_original_timestamp: '2012-04-25T08:39:39+00:00'
---

Originally published on 2012-04-25.

[View the Wayback capture][legacy-source].

[legacy-source]: https://web.archive.org/web/20120521180441/http://rl337.org/2012/04/25/building-for-windows/





[![Download Windows
Version!](/assets/images/legacy-blog/2012/04/windows-logo.jpg.webp)][archive-link-1]

Download the Windows Version!


It took me a while to get there, but I’ve finally gotten a Windows build of the [Weirdo in a Weird
Land](/2012/04/17/weirdo-in-a-weird-land/) bootstrap project!

My first attempt at building one involved grabbing [Visual Studio 10
Express](http://www.microsoft.com/visualstudio/en-us/products/2010-editions/express) but it really
wasn’t meant to be used from the command line… at least not easily…

The successful strategy was to use the [Minimalist GNU for Windows](http://www.mingw.org/)
toolchain.  This lead to some heartache which began with linker issues… but working with the [SDL
FAQ](http://wiki.libsdl.org/moin.cgi/FAQWindows), I got things mostly working.  Of all the problems,
the most surprising to me was the fact that including libraries in gcc is significant.
Specifically… the following did not work:

    $(CC) -o $(BUILDDIR)/$(EXETARGET) $(BUILDDIR)/main.o \
        $(BUILDDIR)/Level.o $(BUILDDIR)/SDLAppMain.o \
        -L$(SDLDIR)/lib -L$(SDLIMAGEDIR)/lib/$(ARCH) \
        -lSDLmain -lSDL -lSDL_image -lmingw32 -mwindows

but THIS did!

    $(CC) -o $(BUILDDIR)/$(EXETARGET) $(BUILDDIR)/main.o \
        $(BUILDDIR)/Level.o $(BUILDDIR)/SDLAppMain.o \
        -L$(SDLDIR)/lib -L$(SDLIMAGEDIR)/lib/$(ARCH) \
        -lmingw32 -lSDLmain -lSDL -lSDL_image -mwindows

The significant part here is the -lmingw32 being first.  Without that, I got the following linker
issue…


    Undefined reference to 'WinMain@16'

Which is discussed in the FAQ… but the answer did not point out that the ordering of the libraries
was significant!

Now i just need to create a proper Makefile that will switch easily between the two architectures….
then it’s time to actually write the game!

UPDATE: The original zip that I uploaded seemed to be missing a few necessary files… specifically
two DLLs: libgcc_s_dw2-1.dll and libstdc++-6.dll both of which are now part of the distribution.


[archive-link-1]: https://web.archive.org/web/20120521180441/http://rl337.org/wp-content/uploads/2012/04/wiawl-dist.zip

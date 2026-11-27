---
layout: post
title: Objective C, C++ and OpenGL
date: '2012-02-21'
author: Richard Lee
permalink: /2012/02/21/objective-c-c-and-opengl/
legacy_archive: true
archive_source: https://web.archive.org/web/20120307024902/http://rl337.org/2012/02/21/objective-c-c-and-opengl/
archive_original_timestamp: '2012-02-21T17:40:16+00:00'
---

[Archived image:
silver-apple-logo][archive-link-1]I
started working on converting my
[N-Body](/2012/02/02/wrapping-n-body-simulation/) simulation code over
to C/C++ and realized that I had no idea how I’d actually display the results.  So… it was time to
learn a little about displaying stuff in [OS X](http://www.apple.com/macosx/).

One thing that struck me as ungainly was having to use [XCode](https://developer.apple.com/xcode/)
when really all I wanted to do was get myself a window and draw to it. This lead me to this awesome
[blog post](http://cocoawithlove.com/2010/09/minimalist-cocoa-programming.html) showing a very
minimalist [Cocoa](https://developer.apple.com/technologies/mac/cocoa.html) app.

With that start, I thought that I’d try to do most of my work in [C++](http://www.cplusplus.com/)
instead of [Objective
C](https://developer.apple.com/library/mac/#referencelibrary/GettingStarted/Learning_Objective-C_A_Primer/_index.html)…
so how does one do THAT in OS X?? There seems to be a bunch of literature about how to make C++
calls from Objective C… but not the other way around, which is really what I want to do… I want my
C++ code to be the driver of the application and use Objective C to pass events and display results…
It was stackoverflow to the rescue with this article:
<http://stackoverflow.com/questions/1061005/calling-objective-c-method-from-c-method>

Essentially, you write yourself a C header with some forward declarations for methods that are later
declared in a .mm file.  Assuming that you’re coding in C++ instead of C, compile with g++ or you’ll
get a lot of strange missing symbols at link-time if you use plain old gcc.

Once I have things going smoothly, I’ll post the skeleton code up on
[github](http://github.com/rl337)!


[archive-link-1]: https://web.archive.org/web/20120307024902/http://rl337.org/wp-content/uploads/2012/02/silver-apple-logo.png

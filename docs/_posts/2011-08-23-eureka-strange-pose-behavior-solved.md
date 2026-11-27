---
layout: post
title: Eureka! Strange pose behavior solved!
date: '2011-08-23'
author: Richard Lee
permalink: /2011/08/23/eureka-strange-pose-behavior-solved/
legacy_archive: true
archive_source: https://web.archive.org/web/20110930042040/http://rl337.org/2011/08/23/eureka-strange-pose-behavior-solved/
archive_original_timestamp: '2011-08-23T16:19:36+00:00'
categories:
- littlerobots
tags:
- 3d
- blender
- robots
- sena
---

Originally published on 2011-08-23.

[View the Wayback capture][legacy-source].

[legacy-source]: https://web.archive.org/web/20110930042040/http://rl337.org/2011/08/23/eureka-strange-pose-behavior-solved/




A while back, I had
[posted](/2011/08/11/rigging-its-tougher-than-it-looks/)
about a strange rigging behavior that I was seeing.  I’m not sure that the description that I was
terribly useful… so I decided to make a couple [animated
gifs](http://en.wikipedia.org/wiki/Animated_gif#Animated_GIF) to help with the visuals…

[![pose-normal](/assets/images/legacy-blog/2011/08/pose-normal.gif)](/assets/images/legacy-blog/2011/08/pose-normal.gif)

Here
you see what a proper rigging is supposed to look like.  The block rotates with the rotation of the
“Bone”. Now, The following image illustrates what I was looking at…

[![pose-broken](/assets/images/legacy-blog/2011/08/pose-broken.gif)](/assets/images/legacy-blog/2011/08/pose-broken.gif)

You
can see here, the cube is actually moving faster than the rotation of the bone.  The exaggerated
motion caused all kinds of stuff to get out of alignment.

The way you associate the Armature or Skeleton to an object is you set the Armature as the “Parent”
of the object.  In this case, the object is the cube.  You do this by simply selecting the cube,
then the Armature and hitting CTRL-P (You can also parent by going through the menus).

When I created the simplified case of the single bone and a single cube, it worked just fine.  On a
hunch, I decided to un-parent then re-parent the object and armature… and voiala! the problem was
reproduced.   It turns out that in Blender 2.5, you’re not actually “parenting” you’re setting a
modifier on the object… so clearing the object’s parent does NOT clear its relationship with the
armature.  When you then re-parent the two, you create a SECOND modifier between the object and the
armature, so any changes to the armature are magnified 2x… which is the behavior you see in the 2nd
image.

[![cube-properties](/assets/images/legacy-blog/2011/08/cube-properties.png.webp)](/assets/images/legacy-blog/2011/08/cube-properties.png.webp)

Okay.
Well, this is all well and dandy, but if you can’t un-parent, how do you get rid of the armature to
object relationship?  It ends up in the object modifiers tab.  Here’s what it looks like if you’ve
got an Armature associated multiple times with an object…So… all you really have to do at this point
is figure out which of the two modifiers you want and X the other one(s).

In the situation with my aperture, I had created 3 modifiers.. so the pose was affecting the object
three times as fast.

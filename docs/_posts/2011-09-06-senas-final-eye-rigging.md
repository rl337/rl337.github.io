---
layout: post
title: Seña’s Final Eye Rigging
date: '2011-09-06'
author: Richard Lee
permalink: /2011/09/06/senas-final-eye-rigging/
legacy_archive: true
archive_source: https://web.archive.org/web/20110930043103/http://rl337.org/2011/09/06/senas-final-eye-rigging/
archive_original_timestamp: '2011-09-06T15:53:17+00:00'
categories:
- littlerobots
tags:
- 3d
- blender
- robots
- sena
---

Originally published on 2011-09-06.

[View the Wayback capture][legacy-source].

[legacy-source]: https://web.archive.org/web/20110930043103/http://rl337.org/2011/09/06/senas-final-eye-rigging/




[![eye-rigging-final](/assets/images/legacy-blog/2011/09/eye-rigging-final-300x271.jpg.webp)](/assets/images/legacy-blog/2011/09/eye-rigging-final.jpg.webp)

I
took some time over the [Labor Day](http://en.wikipedia.org/wiki/Labor_Day) weekend to finalize
Seña’s eye rigging.  As you can see from the image to the right, the rigging itself is made up of
something like 25 bones.  Crazy but awesome.

A particularly pleasing aspect of finishing this rig is, it satisfies all of the requirements that I
set forth in my previous post about [Eye Detail](/2011/07/28/sena-eye-detail/).  This means that I
wasn’t forced to compromise with the features I wanted… I was able to figure it all out.

While rigging the “eye petals” (the four sun shades around the outside of the eye), I ran into
another peculiarity of [blender](http://blender.org)‘s [armature
system](http://wiki.blender.org/index.php/Doc:Manual/Rigging/Armatures).  Let me describe the setup…
The eye petals each have a vertex group (upper petal, lower petal, left petal, right petal) and each
vertex group has an associated bone in the armature (they’re the largest ones in the image above).
Whenever I’d rotate a petal, though, it’d deform in very peculiar ways.  Below is a simple rig that
reproduces the problem…

[![double-grouped](/assets/images/legacy-blog/2011/09/double-grouped.gif)](/assets/images/legacy-blog/2011/09/double-grouped.gif)

For
the first say, 20 degrees of rotation everything looks fine.  You’ll notice though as the bone is
rotated, the box it rotates starts to get smaller and no longer seems to follow the track of
rotation.  Grrr… what’s causing that??!

Before I present the solution, I need to show you how the vertex groups are set up so that I can
explain what it is we’re seeing here…

[![vertex-groups](/assets/images/legacy-blog/2011/09/vertex-groups-300x168.png.webp)](/assets/images/legacy-blog/2011/09/vertex-groups.png.webp)

You can see that I have two vertex groups… “Upper Box” represents the box we’re trying to move and
“All Boxes” is a group containing both the upper and lower box.  “All Boxes” is associated with the
parent bone (behind blue one) and “Upper box” is associated with only the box that we’re moving.

Because the upper box is being influenced by two different bones at the same time, their overlapping
influence on the vertexes of the box causes the strange behavior.  The solution is to remove the
upper box from the “All Boxes” vertex group.  Once I removed the overlap in bone influence
everything works as expected.

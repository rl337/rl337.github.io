---
layout: post
title: Using Background Images in Blender
date: '2012-01-24'
author: Richard Lee
permalink: /2012/01/24/blender-background-images/
legacy_archive: true
archive_source: https://web.archive.org/web/20120307024838/http://rl337.org/2012/01/24/blender-background-images/
archive_original_timestamp: '2012-01-24T16:44:08+00:00'
---

Originally published on 2012-01-24.

[View the Wayback capture][legacy-source].

[legacy-source]: https://web.archive.org/web/20120307024838/http://rl337.org/2012/01/24/blender-background-images/




While I was building the [iPhone4
model](/2012/01/05/iphone4-blender-model-still-incomplete-but-oh-well/),
I began to realize that my proportions were off.  The Home Button seemed out of place. The front
camera and speaker were not quite the right shape.  The buttons and breaks in the seems were a bit
off from where they needed to be… the list went on and on.

It turns out that blender has a feature for exactly this problem, [background
images](http://wiki.blender.org/index.php/Doc:2.6/Manual/3D_interaction/Navigating/3D_View_Options).
This lets you set an image as the background to your modeling space, thus allowing you to match up
your mesh boundaries to features of the image!  Obviously, care has to be chosen when choosing these
kinds of images, but assuming you can find fairly
[orthogonal](http://wiki.blender.org/index.php/Doc:2.4/Tutorials/Animation/BSoD/Character_Animation/3D_View)
shots of the front, back, left, right, top and bottom, you can model very precisely from actual
photographs.

[![view-properties](/assets/images/legacy-blog/2012/01/view-properties-300x117.jpg.webp)](/assets/images/legacy-blog/2012/01/view-properties.jpg.webp)

Ok.
How can you set background images?  Go to your view menu and click properties. That should pop up a
properties pane.  Near the bottom of the properties pane, you’ll see the widget for background
images.  Check the check box and click “Add
[![bg-image](/assets/images/legacy-blog/2012/01/bg-image.jpg.webp)](/assets/images/legacy-blog/2012/01/bg-image.jpg.webp)

Image”.
Select which view you’d like this image to show up in (front, left, right, back, etc) and expand the
“Not Set” arrow. That should give you a little dialog box that’ll give you a file picker.

You can add an image for every orthogonal view, so when you hit a perspective key on the number pad,
the appropriate background image is displayed.

After digging around the web for a while, I finally found a set of images that could help me re-tune
my iPhone mesh… here’s the mesh with the “front” background image

[![iphone-wireframe-bgimage](/assets/images/legacy-blog/2012/01/iphone-wireframe-bgimage.jpg.webp)](/assets/images/legacy-blog/2012/01/iphone-wireframe-bgimage.jpg.webp)

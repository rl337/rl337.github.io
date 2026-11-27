---
layout: post
title: Martian Census Data
date: '2011-09-20'
author: Richard Lee
permalink: /2011/09/20/martian-census-data/
legacy_archive: true
archive_source: https://web.archive.org/web/20110930043132/http://rl337.org/2011/09/20/martian-census-data/
archive_original_timestamp: '2011-09-20T17:30:06+00:00'
categories:
- mars
---

Originally published on 2011-09-20.

[View the Wayback capture][legacy-source].

[legacy-source]: https://web.archive.org/web/20110930043132/http://rl337.org/2011/09/20/martian-census-data/




It’s been a while since I posted anything about [Project:
Mars](https://web.archive.org/web/20110930043132/http://rl337.org/category/mars/?sortby=ID&order=ASC),
so here we go…

A subtle but very important aspect of any fictional culture is its population.  Specifically the
census of age, gender and point of origin.  I see Martian culture to be an interesting conflict of
old world (from [Earth](http://en.wikipedia.org/wiki/Earth)) ways of life with new world (born on
[Mars](http://en.wikipedia.org/wiki/Mars)) burgeoning tradition.  To see just how much this affects
the story, I needed some data… so it was off to the drawing board to model some [population
growth](http://en.wikipedia.org/wiki/Population_growth).

[![population_growth](/assets/images/legacy-blog/2011/09/population_growth-300x175.png.webp)](/assets/images/legacy-blog/2011/09/population_growth.png.webp)

To
the right, you can see a graph of population growth over time.  The population represented here has
two components (which I should have broken out, but didn’t), an immigrant part and a birthrate
part.  The immigrant portion of the population growth starts out modest and grows slowly over time.
I simulated this with a logarithmic increase.  The birthrate portion of the population represents
actual births on Mars.  This population is of particular interest to me because they represent the
specific culture that I want to study.  The population of Mars-born Martians grows exponentially; a
lot like a [compounded interest](http://en.wikipedia.org/wiki/Compound_interest) problem.  You can
see from the graph, we have a healthy concave up growth curve.

I had put the setting of this fiction about 250 years after the founding of the principal city (yet
unnamed).  After simulating 250 years, I ended with some interesting numbers… almost exactly 50% of
the population at this point in time was born on Mars and the other 50 percent originated from
Earth.   I need to play with the simulation to have a more realistic age distribution… at the
moment, I assume that medicine has advanced to the point where old age is no longer a fatal
condition, so a [histogram](http://en.wikipedia.org/wiki/Histogram) of counts by age will look
unrealistically flat.

Another liberty that I took with the simulation was with gender.  I assumed that the initial
population would be male-heavy… which I set at 70% male.  Subsequent immigration, I slanted a little
bit less male (65%).  To make things a bit more interesting, I assumed that natural birthrate on
Mars would skew female, so 55% of children born on mars would be girls.  Let’s take a look at how
this pans out…

[![earth_gender](/assets/images/legacy-blog/2011/09/earth_gender-300x247.png.webp)](/assets/images/legacy-blog/2011/09/earth_gender.png.webp)

At
year 250, we can see that all surviving people from Earth are totally skewed male.  There are
basically 2 men for every 1 woman.  I could see how this would amount to some extreme competition
and drama as men vie over the extreme scarcity of a mate.  It could very well be that we see huge
campaigns encouraging more women to head off to Mars… cuz, [Mars Needs
Women](http://en.wikipedia.org/wiki/Mars_needs_women)!

On the flip side of the
coin[![martian_gender](/assets/images/legacy-blog/2011/09/martian_gender-300x243.png.webp)](/assets/images/legacy-blog/2011/09/martian_gender.png.webp),
when we look at native born Martians, we see that women outnumber men.  Of course, the gender
difference won’t equal out to near 50/50 for probably another 50 years based on the simulation… but
it’s clear to me that earth men will end up pairing up with martian women more often than not.

I’m sure that there will be quite a lot of angst over the preferences of martian vs earth partners
just as we see [race preferences in online
dating](http://blog.okcupid.com/index.php/your-race-affects-whether-people-write-you-back/) today.

Even with this limited simulation I can already see interesting drama unfolding in this Martian
city!

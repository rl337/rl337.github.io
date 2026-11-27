---
layout: post
title: Gradient Descent and Normalized Data
date: '2012-07-03'
author: Richard Lee
permalink: /2012/07/03/gradient-descent-and-normalized-data/
legacy_archive: true
archive_source: https://web.archive.org/web/20120706234502/http://rl337.org/2012/07/03/gradient-descent-and-normalized-data/
archive_original_timestamp: '2012-07-03T07:00:39+00:00'
categories:
- ml
---

[Skynet](https://github.com/rl337/incubator/tree/master/main/skynet) is coming along nicely. I’ve
gotten the chance to build out a fairly comprehensive [Linear
Regression](http://en.wikipedia.org/wiki/Linear_regression) object model.

The actual learning part of Linear Regression centers around finding the minimum value of something
called the [Cost Function](http://en.wikipedia.org/wiki/Cost_function); a function which measures
how inaccurate the algorithm guesses at the answers.  The method that I’m using for finding the
minimum value for the cost function is called Gradient Descent.  One thing that I noticed, though,
was that Gradient Descent was taking FOREVER to converge to an optimal theta… (theta is the set of
parameters which lead to a minimal cost function)  especially if the learning rate was low.  I had
no idea just how slow it could be.

[![linear_regression_unnormalized](/assets/images/legacy-blog/2012/07/linear_regression_unnormalized-300x300.png.webp)](/assets/images/legacy-blog/2012/07/linear_regression_unnormalized.png.webp)

On
the right, you can see a plot of my *Hypothesis*.  The hypothesis is the function that my AI is
using to guess against a synthetic data set. The data set is very linear and really, an ideal
hypothesis would run right down the center of the line.

In this case, Gradient Descent did not converge in time and it hit its maximum iterations before it
could reach a reasonable value of theta.

Normally my options are I could increase my learning rate or add more iterations.   I wanted to see,
however what using data normalization would do.

Normalizing data takes each data point, subtracts the mean of the data set and divides by the
standard deviation (you can optionally divide by the range).   This gives you a dataset that’s
centered around y=0 and has a much smaller range of y values.   So how does this change whether or
not Gradient Descent converges? Let’s see…

[![gradient_descent_convergence](/assets/images/legacy-blog/2012/07/gradient_descent_convergence-300x300.png.webp)](/assets/images/legacy-blog/2012/07/gradient_descent_convergence.png.webp)

Here,
you see the convergence rates of Gradient Descent.  The red values represent un-normalized data and
the blue represents the same dataset, but normalized.

I should have cut off the first few data points because they’re totally outliers, but you can see
that the red line goes all the way off to the right which means that it hit its maximum number of
iterations.  The blue line, however stops short.  It converged before maxing out its iterations.

How does the normalized hypothesis look plotted against the data? Take a look!

[![linear_regression_normalized](/assets/images/legacy-blog/2012/07/linear_regression_normalized-300x300.png.webp)](/assets/images/legacy-blog/2012/07/linear_regression_normalized.png.webp)

You
can see that the hypothesis for the normalized data looks far more correct.

One thing to note before you dive into normalized data… whatever dataset you use your learned thetas
on must also be normalized… otherwise you’ll be feeding your Linear Regression algorithm apples when
it learned on oranges.  That’s very likely not going to produce desired results.

---
layout: post
title: Perceptrons as a digit classifier
date: '2013-01-06'
author: Richard Lee
permalink: /2013/01/06/perceptrons-as-a-digit-classifier/
legacy_archive: true
archive_source: https://web.archive.org/web/20131021050045/http://rl337.org/2013/01/06/perceptrons-as-a-digit-classifier/
archive_original_timestamp: '2013-01-06T23:39:00+00:00'
categories:
- ml
---

Originally published on 2013-01-06.

[View the Wayback capture][legacy-source].

[legacy-source]: https://web.archive.org/web/20131021050045/http://rl337.org/2013/01/06/perceptrons-as-a-digit-classifier/




[![perceptron-diag](/assets/images/legacy-blog/2013/01/perceptron-diag.png.webp)][archive-link-1]It’s
been a while since I posted.  I’ve continued to mess around with [Machine
Learning](http://en.wikipedia.org/wiki/Machine_learning).  As a seemingly natural extension of
[Andrew Ng](http://en.wikipedia.org/wiki/Andrew_Ng)‘s [class](https://www.coursera.org/course/ml), I
took [Geoffrey Hinton](http://en.wikipedia.org/wiki/Geoffrey_Hinton)‘s [Neural Networks for Machine
Learning class](https://www.coursera.org/course/neuralnets).  I have to say, it totally blew my
mind.  If we haven’t already gotten to a near-sentient
[AI](http://en.wikipedia.org/wiki/Artificial_intelligence), I’m convinced that we’re very close.

For my own exploration of Machine Learning, I’ve decided to work through the family of neural
network types in a similar order to the sequence presented in Geoffrey Hinton’s class.  That means,
that I start with the very first type of neural network, the Perceptron.

A [Perceptron](http://en.wikipedia.org/wiki/Perceptron) takes multiple input values and makes a
single logistic decision about it.  I took a collection of
[MNIST](http://yann.lecun.com/exdb/mnist/) digits to see how well a Perceptron would do at
identifying them.  You’d imagine that this would be a natural fit for a Perceptron as digits are
reasonably distinct… but I discovered that there really is not enough information stored within the
weights of a perceptron to make it an effective classifier for MNIST.

Here’s what the perceptron weights looked like for number 3. White means positive coefficients and
black means negative.  Gray means near-zero.  The images read from left to right and represent the
state after increasing batches of 1000 labeled cases.

![perceptron-0.5](/assets/images/legacy-blog/2013/01/perceptron-0.5.png.webp)

Here you can see that the more batches you run against the perceptron, the more complex the weights
get.  These complexities are probably overfitting. I thought, meh. Let me see how well it performed.
 Now, as 3s only represent about 10% of the label data, if I always guess “Not a 3″, I would see a
90% correct guess.  This means that I wanted a value higher than 90%. It turns out that my
classifier scored 90.26% which caused me to suspect that my perceptron had guessed all 0s.   From
actually looking at the guesses, though, I realized that no… the perceptron was actually guessing
based on data, so I needed to dig a bit more into what it was doing.   Here’s the distribution of
its answers:

    Correct Negative: 4034
    Correct Positive: 479
    False Negative: 466
    False Positive: 21

So for real, it was guessing right about 90% of the time.  What screws it over ends up being its
false negatives.  blah.

I decided to try something.  Instead of weighting positive and negative cases equally when
determining weights, I thought that I would add a term called alpha which weights positive and
negative cases differently.  In this case, since the positive case only happens one in 10 times, I
wanted to weight the negative cases by 1/10th, so I set alpha to 0.1.

![perceptron-0.1](/assets/images/legacy-blog/2013/01/perceptron-0.1.png.webp)

Here is an image of the coefficients using the values weighted by alpha.  You can see that,
especially in the earlier batches that the shape of the 3 is a lot fuzzier and we have less
complexity, even in the later iterations.  So how well did THIS set of coefficients work?

    Correct Negative 3962
    Correct Positive 472
    False Negative 538
    False Positive 28

It seems like it did a lot worse.  It had a lot more false negatives. The false positives and
correct positives also dropped but not by much.  It seems like the fuzzier coefficients caused the
perceptron to be less certain about a particular trial.




[archive-link-1]: https://web.archive.org/web/20131021050045/http://rl337.org/2013/01/06/perceptrons-as-a-digit-classifier/perceptron-diag/

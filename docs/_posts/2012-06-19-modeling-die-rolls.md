---
layout: post
title: Modeling Die Rolls
date: '2012-06-19'
author: Richard Lee
permalink: /2012/06/19/modeling-die-rolls/
legacy_archive: true
archive_source: https://web.archive.org/web/20120629070848/http://rl337.org/2012/06/19/modeling-die-rolls/
archive_original_timestamp: '2012-06-19T16:45:12+00:00'
---

Modeling out die rolls seems pretty straight forward.  Let’s say that you wanted to figure out the
distribution of sums. The brute force method for doing this looks like the following chunk of perl
code:

    sub dist {
        my ($count, $sides) = @_;
        my $state = [];
        for (my $i = 0; $i < $count; $i++) {
            $state->[$i] = 1;
        }

        my $max = $count * $sides;
        my $result = [];
        while(1) {
           my $sum = 0;
           for (my $i = 0; $i < $count; $i++) {
              $sum += $state->[$i];
           }

           $result->[$sum]++;
           last if $sum >= $max;
           $state->[0]++;
           for (my $i = 0; $i < $count; $i++) {
               last if $state->[$i] [$i] = 1;
               $state->[$i+1]++;
           }
       }
       return $result;
    }

This seems to work well for distributions of same sided dice. What if I wanted to combine multiple
types of dice? Say, 4x six sided dice and 8 4-sided dice… well, the brute force method starts to get
pretty expensive.

I was reading
[this][archive-link-1]
lecture on normal distributions for sums and came to the solution to my problem.  Instead of
iterating over all sums for all dice, I could probably just add the normal curves for the die rolls.

How do you compute a normal distribution? It’s called a Gausian… check the [Wikipedia
page](http://en.wikipedia.org/wiki/Normal_distribution)!  The code for a gausian given two params,
mu and sigma look like so:

    sub gausian {
        my ($x, $mu, $sigma) = @_;

        my $exp = - 1/2 * (($x - $mu) / $sigma) ** 2;
        return 1/($sigma * sqrt(2 * $pi)) * exp($exp);
    }

Now I just need to figure out how to scale mu and sigma (mean, std deviation) to number of dice and
the sides per die.  The lecture above seems to model 6 sided dice well with a mean of 3.5 x number
of dice and 1.7 \* sqrt(num of dice) but I need to expand that out to other side counts for this to
work.


[archive-link-1]: https://web.archive.org/web/20120629070848/http://rl337.org/2012/06/19/modeling-die-rolls/www.stat.berkeley.edu/~bradluen/stat2/lecture22.pdf

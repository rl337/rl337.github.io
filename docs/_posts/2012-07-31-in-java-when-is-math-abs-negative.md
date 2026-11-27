---
layout: post
title: When is Math.abs(x) < 0?
date: '2012-07-31'
author: Richard Lee
permalink: /2012/07/31/in-java-when-is-math-abs-negative/
legacy_archive: true
archive_source: https://web.archive.org/web/20120822065908/http://rl337.org/2012/07/31/in-java-when-is-math-abs-negative/
archive_original_timestamp: '2012-07-31T09:07:31+00:00'
---

Originally published on 2012-07-31.

[View the Wayback capture][legacy-source].

[legacy-source]: https://web.archive.org/web/20120822065908/http://rl337.org/2012/07/31/in-java-when-is-math-abs-negative/




[![drunk-duke](/assets/images/legacy-blog/2012/07/drunk-duke-280x300.png.webp)](/assets/images/legacy-blog/2012/07/drunk-duke.png.webp)

I
was monitoring a long running [Hadoop](http://hadoop.apache.org/) job yesterday at work when I began
noticing one of the tasks which make up that job began failing for an odd reason: Illegal Partition.

For those of you not familiar with Hadoop jobs, part of it involves splitting up massive amounts of
data into smaller, more manageable pieces; or partitioning the data.  The goal of partitioning is to
get N roughly equal chunks where N is generally pretty big.

The specific illegal partition value that was coming up was negative. “But that’s not possible!” I
thought to myself! The expression I was using to choose partitions used Math.abs(x), or the Absolute
value of x.  Specifically:

    partition = Math.abs(x) % N

Ok, now at a glance, you tell me how that could be negative… It turns out though, that for at least
a critical value of x, Math.abs(x) will return negative: Integer.MIN_VALUE.

As it turns out, Integer.MIN_VALUE is the smallest value that a 32-bit number can hold in
java: -2,147,483,648. and if you try to Math.abs(Integer.MIN_VALUE), the result is STILL
Integer.MIN_VALUE.  Is this a bug? It turns out that it’s not.  If you read the javadoc for
Math.abs(), it points out that:

> “Note that if the argument is equal to the value of `Long.MIN_VALUE`, the most negative
> representable `long` value, the result is that same value, which is negative.”

Now, exactly why is that the case?  Well, for you to get the absolute value of Integer.MIN_VALUE,
you’ve got to be able to represent the result as a 32-bit integer too… which is impossible, as the
largest integer you could possibly represent is 2,147,483,647 which is one smaller than we need it
to be.  Maybe this was coded so that the Integer.MIN_VALUE would be preserved?  I decided to look at
the [source](http://hg.openjdk.java.net/jdk6/jdk6/jdk/).

So … here’s the implementation:

    public static int abs(int a) {
        return (a < 0) ? -a : a;
    }

Okay… that’s a much simpler than what I thought it’d be, however it does point out that it’s not
just Math.abs(x) that has this problem… it’s any negation of Integer.MIN_VALUE.  Anotherwords, the
following must be a true expression:

    Integer.MIN_VALUE == -Integer.MIN_VALUE

Give it a shot if you don’t believe me, fire up eclipse and try it out!  In fact, eclipse will
highlight the expression with a warning that says “Comparison of identical expressions”.

Okay… I’m not sure how i feel about this.  so WWCD? (What would
[C](http://en.wikipedia.org/wiki/C_(programming_language)) do?) … so I gave it a shot… Here’s a
[C](http://en.wikipedia.org/wiki/C_(programming_language)) program that exercises this exact
question:

    int main(int argc, char *argv[]) {
        int x = -2147483648;
        int y = -2147483647;
        printf("X: %d %d\n", x, abs(x));
        printf("Y: %d %d\n", y, abs(y));
    }

What do you think the answer is?  It actually surprised me a little:

    X: -2147483648 -2147483648
    Y: -2147483647 2147483647

It seems like [C](http://en.wikipedia.org/wiki/C_(programming_language)) behaves the same way.
 Apparently this isn’t just a Java problem.  Bottom line? watch and test around -2,147,483,648. It’s
a critical value.

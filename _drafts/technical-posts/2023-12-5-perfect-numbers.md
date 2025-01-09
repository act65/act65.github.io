---
layout: post
title: Perfect numbers
subtitle: Playing with new and old ideas
permalink: /perfect-numbers/
categories:
    - play
---


A perfect number is a positive integer that is equal 
to the sum of its unique positive divisors, excluding the number itself. 
For example;

- 6 has divisors 1, 2 and 3 (excluding itself), and 1 + 2 + 3 = 6, therefore 6 is a perfect number. 
- 28 has divisors 1, 2, 4, 7 and 14 (excluding itself), and 1 + 2 + 4 + 7 + 14 = 28, therefore 28 is a perfect number.

Currently, it is unknown if there are any odd perfect numbers.

<h2>
    Jigsaw puzzle
</h2>
<p>
    Another way to think about these perfect numbers is to imagine a kind of jigsaw puzzle.
    The goal is to fill a n x n square with smaller squares. 
    <ul>
    <li> Each row of squares must constructed from i squares of the same size (j x j). (aka a pair of divisors, i x j = n)</li>
    <li> No two rows can be the same. (unique divisors)</li>
    </ul>
</p>

Here are the some jigsaw puzzles.

<div>
    <canvas id="2"></canvas>
    <canvas id="3"></canvas>
    <canvas id="4"></canvas>
    <canvas id="5"></canvas>
    <canvas id="6"></canvas>
    <canvas id="7"></canvas>
    <canvas id="8"></canvas>
    <canvas id="9"></canvas>
    <canvas id="10"></canvas>
    <canvas id="11"></canvas>
    <canvas id="12"></canvas>
    <canvas id="13"></canvas>
    <canvas id="14"></canvas>
    <canvas id="15"></canvas>
</div>

So the perfect numbers perfectly fill the n x n square.
While prime numbers do not fill the square at all.
They are opposite in this sense.

There also exist numbers that can fill the square, and more.
12 is the first example, with divisors 1, 2, 3, 4, 6 which sum to 16.
These numbers are called __abundant numbers__.





How many rearangements of the jigsaw puzzle are there?
For 6 there are;

<div>
    <canvas id="6.1"></canvas>
    <canvas id="6.2"></canvas>
    <canvas id="6.3"></canvas>
    <canvas id="6.4"></canvas>
    <canvas id="6.5"></canvas>
    <canvas id="6.6"></canvas>
</div>

Properties of the jig saw puzzle;

- None of the larger blocks can be composed of smaller blocks. ??? (aka, ...)
- 

## Reframe

<p>
    The converse question. Which sets of numbers (S) sum to x. 
    And also each element of the set can be multiplied with other elements in the set to get x. 
</p>

Patterns in the images?
Each of these has similar structure?!

<div>
    <canvas id="28"></canvas>
    <canvas id="496"></canvas>
    <canvas id="8128"></canvas>
</div>

Note.
In this jigsaw game, primes are the opposite of perfect numbers.
They do not fill the n x n box at all.

want to induce some data!
the factors!

<p>
    <b>Q:</b>
    Are all the positive integers (after 5) contained in the set of sums of divisiors?
    <br>
    Using the first 50 integers we get a set of 25 elements;
    <ul>
    <li> 6,7,8,9,10,11,13,14,15,16,17,20,21,22,26,28,31,33,36,40,42,50,54,55,76</li>  
    </ul>

    Which is missing a few elements, first of which is 12.
    But if we go you to 200 integers we get a set of 103 elements with 12 now included.
    And the first missing element is 18.

    A new element can be added to this set per integer.
    Since the rate of integers is increasing linearly.

</p>

<p>
    <b>Q:</b>
    Is it possible for the sum of divisors of n to be larger than 2 x n?
    sum_divisors(24) -> 36.
    sum_divisors(48) -> 76.
    <br>

</p>

<p>
    $$
    \begin{align}
    2 \times 496 &= 1 + 2 + 4 + 8 + 16 + 31 + 62 + 124 + 248 + 496. \\
    &= 1 + 2 + 4 + 8 + 16 + 31 (1 + 2 + 4 + 8 + 16) \\
    &= (1 + 31)(1 + 2 + 4 + 8 + 16) \\
    \end{align}
    $$
    
    
    aka. 1, then double till we get to mersenne prime + 1. then keep doubling till ...?


</p>

<p>
    Interestingly there is a connection to the mersenne primes!<br>

    $$
    (2^{n - 1})(2^n - 1)
    $$

    Each even perfect number must have a prime factor.
    The factors must sum to an even number. And since 1 is always a factor, we need a least one more odd factor.
    If the odd factor is not prime (ie 9).
</p>

Unsolved problem in mathematics:
Are there any odd perfect numbers?

Questions;

- does there exist a fast test for perfect numbers?
- what are their applications?

https://en.wikipedia.org/wiki/Weird_number

<script src="{{base.url}}/assets/perfect-numbers/canvas.js"></script>



<!-- 
mersenne primes are quite useful.
is it possible to effecitly find perfect numbers to help generate mersenne primes?

 -->

Let's say we have an odd perfect number n.

1) First, let's consider what we know about its divisors:
- All divisors come in pairs (d, n/d), except possibly √n
- All divisors must be odd (since n is odd)
- The sum of all these divisors must equal n

2) In the jigsaw representation:
- Each row must have an odd number of squares (i)
- Each square in a row must have odd dimensions (j)
- i × j = n for each row
- The sum of all i × j combinations used must equal n
---
title: Confidence versus rigor
subtitle:
layout: post
permalink: /confidence/
categories:
    - tutorial
---


<style>
.small-input {
    width: 50px;
}

.large-input {
    width: 240px;
    font-size: 16px;
}

p {
    font-size: 16px;
}
</style>

Here is a tutorial designed to help you calibrate your (over) confidence.
I believe we easily confuse confidence of >80% with certainty.

<!-- 
this is a manifesto for rigor. via example.
 -->

## Binary search example

This is a simple problem.
Implement a binary search algorithm in your favorite programming language.

You are given a sorted list of integers and a target value.
Return the index of the target value in the list or -1 if it is not present.

***

Here's my (first) solution in Python:

Binary search seems straightforward - divide and conquer, right? Yet Jon Bentley 
observed that 90% of professional programmers couldn't implement it correctly in under
an hour.


```javascript
function binarySearch(arr, target) {
    low = 0;
    high = arr.length - 1;

    while (low <= high) {
        mid = Math.floor((low + high) / 2);
        midval = arr[mid];
        if (midval < target) {
            low = mid + 1;
        } else if (midval > target) {
            high = mid - 1;
        } else {
            return mid;
        }
    }
    return -1;
}
```

Take a look at this algorithm. Is there anything wrong with it?

Let's try it out <input type="text" id="numberList" placeholder="Enter numbers (e.g., 1,2,3,4)">

<div>
    <input type="number" id="search_val" placeholder="Enter text here"  onkeypress="runBinarySearch(event)">
</div>
<p>Index: <span id="index"></span></p>

<script>
function runBinarySearch(event) {
    if (event.key === 'Enter') {
        const inputList = document.getElementById('numberList').value;
        const search_val = parseInt(document.getElementById('search_val').value);
        const arr = stringToList(inputList);
        const index = binarySearch(arr, search_val);
        console.log(search_val);
        console.log(index);
        console.log(arr);
        document.getElementById('index').innerText = index;
    }
}

function stringToList(str) {
    return str.split(',').map(x => parseInt(x));
}

function binarySearch(arr, target) {
    low = 0;
    high = arr.length - 1;

    while (low <= high) {
        mid = Math.floor((low + high) / 2);
        midval = arr[mid];
        if (midval < target) {
            low = mid + 1;
        } else if (midval > target) {
            high = mid - 1;
        } else {
            return mid;
        }
    }
    return -1;
}

</script>


The bug? When the array is large enough, `(low + high) / 2` can cause integer overflow.
On arrays with billions of elements, this could lead to infinite loops or incorrect results.

The fix is subtle:
```mid = low + (high - low) / 2```

## The Borwein integrals.

We have verified the following;

$$
\begin{aligned}
&\int _{0}^{\infty }{\frac {\sin(x)}{x}}\,dx={\frac {\pi }{2}}\\
&\int _{0}^{\infty }{\frac {\sin(x)}{x}}{\frac {\sin(x/3)}{x/3}}\,dx={\frac {\pi }{2}}\\
&\int _{0}^{\infty }{\frac {\sin(x)}{x}}{\frac {\sin(x/3)}{x/3}}{\frac {\sin(x/5)}{x/5}}\,dx={\frac {\pi }{2}}\\
&\int _{0}^{\infty }{\frac {\sin(x)}{x}}{\frac {\sin(x/3)}{x/3}}{\frac {\sin(x/5)}{x/5}}{\frac {\sin(x/7)}{x/7}}\,dx={\frac {\pi }{2}}
\end{aligned}
$$

Should we generalise this pattern?

$$
\forall n, \int _{0}^{\infty }{\prod _{i=1}^{n}{\frac {\sin(x/i)}{x/i}}}\,dx={\frac {\pi }{2}}
$$


This pattern continues up to

$$
\int _{0}^{\infty }{\frac {\sin(x)}{x}}{\frac {\sin(x/3)}{x/3}}\cdots {\frac {\sin(x/13)}{x/13}}\,dx={\frac {\pi }{2}}
$$

At the next step the pattern fails,

$$
\begin{aligned}
\int _{0}^{\infty }{\frac {\sin(x)}{x}}{\frac {\sin(x/3)}{x/3}}\cdots {\frac {\sin(x/15)}{x/15}}\,dx&\approx {\frac {\pi }{2}}-2.31\times 10^{-11}\end{aligned}
$$


## Floating point math

```python
0.1 + 0.2 == 0.3  # Returns False!
```
- Excellent example of how intuition can mislead
- Shows why financial software needs special decimal types


## Time Complexity Intuition
```python
# Looks O(n) but is actually O(n²) in Python
def build_string(n):
    result = ""
    for i in range(n):
        result += str(i)  # String concatenation creates new string each time
```

## The Fast Inverse Square Root from Quake III
- approximates 1/√x using bit manipulation.
- Works surprisingly well despite being mathematically "wrong".


***

1. **The Fast Fourier Transform Aliasing**
   - Seemingly correct FFT implementations that fail spectacularly due to subtle aliasing effects
   - Shows how sampling theory intuitions can fail
   - Particularly relevant in signal processing and machine learning

2. **Gradient Descent Pathologies**
   - The surprising ways optimization can fail even on seemingly simple functions
   - Saddle points in high dimensions
   - Why momentum sometimes makes things worse
   - Could include visualizations of optimization trajectories

3. **Martingale Stopping Times**
   - Counter-intuitive results about optional stopping
   - Connects to common mistakes in A/B testing and experimental design
   - Relevant to both theorists and practitioners

4. **Distributed Systems Race Conditions**
   - Examples where even careful reasoning about concurrent systems fails
   - The subtleties of eventual consistency
   - Could include examples from real distributed databases

5. **Type System Corner Cases**
   - Surprising theorems about type inference
   - Cases where seemingly reasonable type systems become undecidable
   - The subtle interaction between variance and generics


2. **The Birthday Paradox**
   - Only needs 23 people for a 50% chance of shared birthdays
   - Most people's intuition is way off
   - Easy to code and demonstrate

3. **Monty Hall Problem**
   - Classic example of intuition vs math
   - Can be coded as a simulation
   - Shows how even mathematicians initially got it wrong

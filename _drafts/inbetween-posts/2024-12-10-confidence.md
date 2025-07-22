---
title: The Cost of Confidence
subtitle: Why being 'sure' isn't sure enough
layout: post
permalink: /confidence/
categories:
    - tutorial
---

<!-- 
this is a manifesto for rigor. via example.
 -->

We all make mistakes. But what's more dangerous than making mistakes is being confidently wrong. This post explores several examples where our natural intuitions lead us astray, and demonstrates why rigorous testing and mathematical proof are essential, even when we are confident we are right.

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

## Binary search example

Let's start with a simple problem. Implement a binary search algorithm in your favorite programming language.

You are given a sorted list of integers and a target value.
Return the index of the target value in the list or -1 if it is not present.

Binary search seems straightforward right? Yet Jon Bentley observed that 90% of professional programmers couldn't implement it correctly in under
an hour.

```javascript
function binarySearch(arr, target) {
    low = 0;
    high = arr.length - 1;

    while (low <= high) {
        // Calculate mid index
        mid = Math.floor((low + high) / 2);
        midval = arr[mid];
        // If the target is greater, ignore left half
        if (midval < target) {
            low = mid + 1;
        // If the target is smaller, ignore right half
        } else if (midval > target) {
            high = mid - 1;
        // Else target is present at mid
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
        const search_val_int32 = search_val | 0; // Convert to int32
        const arr = stringToList(inputList);
        const arr_int32 = arr.map(x => x | 0); // Convert to int32
        const index = binarySearch(arr_int32, search_val_int32);
        // console.log(typeof search_val);
        console.log(search_val_int32);
        console.log(index);
        // console.log(arr);
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
        mid = Math.floor((low + high)|0 / 2)|0;
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

***

Great. Now let's try with some large numbers. 

<!-- breaks -->

The fix is subtle:
```mid = low + (high - low) / 2```

***

Now let's try with repeated numbers.

<!-- breaks -->

<!-- The bug? When the array is large enough, `(low + high) / 2` can cause integer overflow.
On arrays with billions of elements, this could lead to infinite loops or incorrect results. -->

***

We are adding test cases, but when will we be satisfied that our implementation is truly 'correct'?


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


1. **The Fast Fourier Transform Aliasing**
   - Seemingly correct FFT implementations that fail spectacularly due to subtle aliasing effects
   - Shows how sampling theory intuitions can fail
   - Particularly relevant in signal processing and machine learning

3. **Martingale Stopping Times**
   - Counter-intuitive results about optional stopping
   - Connects to common mistakes in A/B testing and experimental design
   - Relevant to both theorists and practitioners

4. **Distributed Systems Race Conditions**
   - Examples where even careful reasoning about concurrent systems fails
   - The subtleties of eventual consistency
   - Could include examples from real distributed databases

2. **The Birthday Paradox**
   - Only needs 23 people for a 50% chance of shared birthdays
   - Most people's intuition is way off
   - Easy to code and demonstrate

3. **Monty Hall Problem**
   - Classic example of intuition vs math
   - Can be coded as a simulation
   - Shows how even mathematicians initially got it wrong

4. **The Collatz Conjecture**
- Take any positive integer
- If even, divide by 2
- If odd, multiply by 3 and add 1
- Repeat
- Seems to always reach 1 eventually
- Despite its simplicity, remains unproven after 80+ years
- Shows how even simple-looking patterns need rigorous proof

3. **Mertens Conjecture**
   The Mertens function M(n) appeared to be bounded by ±√n for all positive integers. This was believed true for all n up to 10¹⁰, but was later proven false (though a counterexample is astronomically large).

1. **The Prime Number Formula**
   ```
   f(n) = n² + n + 41
   ```
   This generates prime numbers for all n from 0 to 40, leading one to think it might always generate primes. However, f(41) = 41² + 41 + 41 = 1763 = 41 × 43.
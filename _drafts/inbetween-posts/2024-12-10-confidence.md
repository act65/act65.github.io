---
title: Confidence versus rigor
subtitle:
layout: post
permalink: /confidence/
categories:
    - tutorial
---

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

```python
def binary_search(arr, target, count=0):
    if len(arr) == 0:
        return -1
    elif len(arr) == 1:
        return 0 if arr[0] == target else -1
    else:
        mid = len(arr) // 2
        if arr[mid] == target:
            return count + mid
        elif arr[mid] < target:
            return binary_search(arr[mid+1:], target, count + mid + 1)
        else:
            return binary_search(arr[:mid], target, count)
```



## The Borwein integrals.





## 
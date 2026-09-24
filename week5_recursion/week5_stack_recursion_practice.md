# Week 5 - Stacks and Recursion

## Exercise 1 - Simple Stack problem

Use two stacks. Reverse stack 1 using stack 2.

```
Push all elements in Stack 1
Pop elements from Stack 1 and push then onto Stack 2
Replace Stack 1 with Stack 2
```

Try this in Python

Start data: push list elements [1,2,3,4,5]
End data: list displayed in opposite order: 5,4,3,2,1

## Problem - Towers of Hanoi

Lecturer led

### Iterative version:

```
(Geeks for Geeks)

1. Calculate the total number of moves required i.e. "pow(2, n) - 1" here n is number of disks.
2. If number of disks (i.e. n) is even then interchange destination pole and auxiliary pole.
3. for i = 1 to total number of moves 

if i%3 == 1: legal movement of top disk between source pole and destination pole
if i%3 == 2: legal movement of top disk between source pole and auxiliary pole    
if i%3 == 0: legal movement of top disk between auxiliary pole and destination pole 
```

### Recursive version:

```
 The idea is to use the helper node to reach the destination using recursion. Below is the pattern for this problem:

Shift 'n-1' disks from 'A' to 'B', using C.
Shift last disk from 'A' to 'C'.
Shift 'n-1' disks from 'B' to 'C', using A.
```
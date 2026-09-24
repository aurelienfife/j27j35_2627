# Week 5 Recursion Exercises

These exercises begin with familiar loops and convert them into small recursive functions. 

## Before converting a loop

Ask these questions:

1. What is the simplest input?
2. What answer should the function give for that input?
3. How can one function call move towards the simplest input?
4. How should the current value combine with the recursive result?

The simplest input becomes the **base case**. The smaller function call becomes the **recursive case**.

## Exercise 1: Iterative and recursive countdown

This iterative function uses a loop:

```python
def countdown_iterative(number):
    while number > 0:
        print(number)
        number = number - 1

    print("Go")
```

Complete the recursive version in a code editor by filling the blanks:

```python
def countdown_recursive(number):
    # Base case
    if ____________________:
        print("Go")
        return

    # Work completed by this call
    print(____________________)

    # Recursive case
    countdown_recursive(____________________)
```

### Test code

```python
countdown_iterative(3)
print("---")
countdown_recursive(3)
```

Both functions should produce:

```text
3
2
1
Go
```

### Code hints

- The loop stops after `number` reaches `0`.
- Use `number == 0` as the base case.
- Print the current number before making the recursive call.
- Pass `number - 1` to the next call.
- Test with `0`, `1` and `3`.



## Exercise 2: Convert an iterative sum

This function uses a loop to add every integer from `1` to `number`:

```python
def sum_to_iterative(number):
    total = 0

    for value in range(1, number + 1):
        total = total + value

    return total
```

Examples:

```text
sum_to_iterative(0) returns 0
sum_to_iterative(3) returns 6
sum_to_iterative(5) returns 15
```

Complete the recursive version:

```python
def sum_to_recursive(number):
    # Base case
    if ____________________:
        return ____________________

    # Recursive case
    return ____________________ + sum_to_recursive(____________________)
```

### Test code

```python
tests = [0, 1, 3, 5]

for number in tests:
    iterative = sum_to_iterative(number)
    recursive = sum_to_recursive(number)
    print(number, iterative, recursive)
```

Expected output:

```text
0 0 0
1 1 1
3 6 6
5 15 15
```

### Code hints

- The simplest input is `0`.
- The sum of the integers up to `0` is `0`.
- `sum_to_recursive(4)` can return `4 + sum_to_recursive(3)`.
- Each call must reduce `number` by one.
- Trace `sum_to_recursive(3)` on paper before running it.



## Exercise 3: Convert iterative powers

This function calculates a positive whole-number power using a loop:

```python
def power_iterative(base, exponent):
    result = 1

    for _ in range(exponent):
        result = result * base

    return result
```

For example, `power_iterative(2, 3)` calculates `2 * 2 * 2`.

Complete the recursive version:

```python
def power_recursive(base, exponent):
    # Base case
    if ____________________:
        return ____________________

    # Recursive case
    return ____________________ * power_recursive(
        ____________________,
        ____________________,
    )
```

### Test code

```python
tests = [
    (2, 0),
    (2, 1),
    (2, 4),
    (3, 3),
]

for base, exponent in tests:
    iterative = power_iterative(base, exponent)
    recursive = power_recursive(base, exponent)
    print(base, exponent, iterative, recursive)
```

Expected output:

```text
2 0 1 1
2 1 2 2
2 4 16 16
3 3 27 27
```

### Code hints

- Any number raised to the power `0` returns `1`.
- Reduce `exponent`, not `base`.
- Keep the same value of `base` in every call.
- `power_recursive(2, 3)` can return `2 * power_recursive(2, 2)`.
- Compare the iterative and recursive results for every test.


### Further challenge

Add a check that rejects a negative exponent with a clear error message.


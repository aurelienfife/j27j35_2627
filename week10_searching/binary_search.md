# Binary Search Exercises

Binary search requires values sorted in ascending order. Use zero-based indices and treat both search bounds as inclusive. Write the search yourself in every exercise. Avoid Python search shortcuts such as `list.index()`, `bisect` and `in` to locate the target.

## Learning goals

- Implement iterative binary search and handle an absent target.
- Identify the base case and recursive calls in binary search.
- Sort an unsorted list before applying binary search.

## Exercise 1 — Implement iterative binary search

### Required behaviour

- Return an index containing the target, or `-1` when the target is absent.
- For repeated values, any matching index is valid.
- Leave the input list unchanged.

### Starter code

```python
def binary_search(values, target):
    low = 0
    high = len(values) - 1

    while low <= high:
        mid = (low + high) // 2
        # Return mid if it matches the target.
        # Otherwise, change exactly one bound.
        pass  # Replace this before running the tests.

    return -1
```

### Test code

```python
values = [3, 7, 11, 18, 24, 31, 42]

print(binary_search(values, 31))
print(binary_search(values, 3))
print(binary_search(values, 42))
print(binary_search(values, 20))
print(binary_search([], 9))

assert binary_search([9], 9) == 0
assert binary_search([9], 8) == -1
assert binary_search([1, 4, 4, 4, 9], 4) in (1, 2, 3)
```

Expected output:

```text
5
0
6
-1
-1
```

## Exercise 2 — Sort an unsorted list, then search it

Write a program that takes an unsorted list of integers and a target. First sort a copy of the list in ascending order using a sorting algorithm of your choice. Then pass that sorted copy to one of the binary search functions you wrote.

### Required behaviour

- Implement or reuse a sorting algorithm from the sorting exercises, such as insertion sort, bubble sort, quicksort or merge sort.
- Leave the input list unchanged.
- Return an index in the **sorted list**, or `-1` if the target is absent.
- Use your own binary search function to find the target.

### Starter code

```python
def sort_then_search(values, target):
    ordered = values.copy()
    # Sort ordered using your chosen algorithm.
    # Search ordered and return the resulting index.
    pass
```

### Hints

- Bubble sort and insertion sort modify the list passed to them. Call them on `ordered`.
- The quicksort and merge sort functions from the recursive sorting sheet return a new list. Assign that return value to `ordered` before searching.

### Test code

```python
values = [24, 3, 42, 11, 7]

assert sort_then_search(values, 24) == 3
assert sort_then_search(values, 3) == 0
assert sort_then_search(values, 42) == 4
assert sort_then_search(values, 20) == -1
assert sort_then_search([], 9) == -1
assert values == [24, 3, 42, 11, 7]
```

Expected result: all assertions pass.


## Exercise 3 (Hard Mode) — Attempt recursive binary search

Write a recursive version with the same behaviour as Exercise 1. Each call should search a smaller interval of the original list.

### Starter code

```python
def recursive_binary_search(values, target):
    def search(low, high):
        # Handle an empty interval.
        # Check the middle value.
        # Recurse into the remaining half if needed.
        pass

    return search(0, len(values) - 1)
```

### Hints

- Start with the base case. If `low > high`, return `-1` before accessing the list.
- Calculate `mid = (low + high) // 2`. If `values[mid]` matches the target, return `mid`.
- If the middle value is too small, recurse with the interval from `mid + 1` to `high`. If it is too large, recurse with the interval from `low` to `mid - 1`.
- Return the result of the recursive call. Keep passing bounds into the helper so the indices refer to the original list.

### Test code

```python
values = [3, 7, 11, 18, 24, 31, 42]
assert recursive_binary_search(values, 7) == 1
assert recursive_binary_search(values, 42) == 6
assert recursive_binary_search(values, 20) == -1
assert recursive_binary_search([], 9) == -1
assert recursive_binary_search([9], 9) == 0
```

Expected result: all assertions pass.

### Questions

1. Why is the returned index for `24` different from its index in the input list?
2. If you need to search for several targets in the same list, when can you reuse the sorted copy?

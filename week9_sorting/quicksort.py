# Quicksort algorithm
# Quicksort is a divide-and-conquer sorting method.
# It repeatedly chooses a pivot value and splits the list into two smaller lists:
# - items smaller than or equal to the pivot go to the left
# - items larger than the pivot go to the right
# Then it sorts each side recursively and combines the results.

# General algorithm -> quicksort
def quicksort(arr):

    # This line helps us see what the function is currently processing.
    # It is useful for learning/debugging, but not needed in the final version.
    # print("Working on:", arr)

    # Base case:
    # If the list has 0 or 1 item, it is already sorted.
    # We stop calling quicksort on it.
    if len(arr) <= 1:  # It's sorted
        return arr

    # Choose the last element as the pivot.
    # This value will be placed in its final position when the function finishes.
    pivot = arr[-1]

    # Create two new lists:
    # left -> values smaller than or equal to the pivot
    # right -> values greater than the pivot
    left = []
    right = []

    # Look at every element except the pivot.
    # Move each value to the correct side of the pivot.
    for i in range(len(arr) - 1):
        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    # Recursively sort the left part and the right part.
    # Then put the pivot in the middle.
    return quicksort(left) + [pivot] + quicksort(right)

# Example list to test the algorithm.
result = quicksort([6, 3, 9, 10, 2, 8, 1, 4, 5, 7, 6])
print(result)
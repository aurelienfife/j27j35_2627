# This is an example of testing template for performance
# Using a bubble sort in this case

# It takes a timestamp before running the algorithm
# and another one afterwards

# After each run it prints out the time taken

import datetime
# For bubble sort - create a random list
import random

# Insert your function here (e.g. bubble sort)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        sorted = True
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                sorted = False
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if sorted:
            break
    return arr

def perf_run(runs, size):

    

    # Run algorithm "runs" times
    for i in range(runs):
        # Create an array of "size" random ints
        test_data = []
        for i in range(size):
            test_data.append(random.randint(1,100))

        t = datetime.datetime.now()
        arr = bubble_sort(test_data)
        t2 = datetime.datetime.now()
        #print(arr)
        print(f"Run {i}, size {size}, time: {t2-t}")

# Comparing bubble sort, 5 runs, size: 10, 100, 1000, 10k elements

perf_run(5,10)
perf_run(5,100)
perf_run(5,1000)
perf_run(5,10000)
perf_run(5,20000)
perf_run(5,100000)

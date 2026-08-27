import array
import random

# I am going to create an array of numbers
# with the constraint of them being integers


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

num_array = array.array('i')
for i in range(10):
    num_array.append(random.randint(1,100))

print(num_array)
print(bubble_sort(num_array))



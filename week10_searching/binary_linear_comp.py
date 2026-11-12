numbers = [12, 24, 31, 45, 53, 67, 78, 89, 96, 104, 115, 123, 137, 149, 158, 169, 177, 186, 198, 207, 219, 228, 236, 247, 259, 268, 276, 285, 297, 306, 318, 327, 339, 348, 356, 367, 379, 388, 396, 407, 419, 428, 436, 447, 459, 468, 476, 485, 497, 506, 518, 527, 539, 548, 556, 567, 579, 588, 596, 607, 619, 628, 636, 647, 659, 668, 676, 685, 697, 706, 718, 727, 739, 748, 756, 767, 779, 788, 796, 807, 819, 828, 836, 847, 859, 868, 876, 885, 897, 906, 918, 927, 939, 948, 956, 967, 979, 988, 996]

# To try   31  123   276     727    897
# Not in list 55   136   699

def linear_search(arr, key):
    count = 0
    # Compare each element to search term
    for i in range(len(arr)):
        count += 1
        # If match return index
        if arr[i] == key:
            print("linear runs:", count)
            return i
    # Nothing found: return -1
    print("linear runs:", count)
    return -1

def binary_search(arr, key):
    count = 0
    # Set low and high boundaries to 0 and len(-1)
    low = 0
    high = len(arr) - 1
    # Repeat the process for as long as there is a gap in between
    # low and high
    while low <= high:
        count+=1
        # Midpoint: middle of available space
        # Effectively difference between high and low 
        # Divided by two, but adding low (to ensure we 
        # search in the right place)
        mid = int(low + (high-low)/2)

        # If equal, return mid
        if arr[mid] == key:
            print("binary runs:", count)
            return mid
        # Else if midpoint is lower than key
        # Set midpoint as new low boundary + 1
        elif arr[mid] < key:
            low = mid + 1
        # Else set the high boundary to mid -1
        else:       # > case
            high = mid - 1

    # Nothing found?
    print("binary runs:", count)
    return -1


# To try   31  123   276     727    897
# Not in list 55   136   699

def main():
    test_vals = [31, 55, 123, 136, 276, 897, 968]
    for k in test_vals:
        res = binary_search(numbers, k)
        res = linear_search(numbers, k)
        print("Index of:", k, ":", res)

if __name__ == "__main__":
    main()
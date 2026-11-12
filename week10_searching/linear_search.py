# Just FYI a linear search
# Linear complexity

def linear_search(arr, search_term):
    # Compare each element to search term
    for i in range(len(arr)):
        # If match return index
        if arr[i] == search_term:
            return i
    # Nothing found: return -1
    return -1

def main():
    data = ["Biniam", "Cameron", "Michal", "Panashe"]

    for search in ["Cameron", "Brandon"]:
        res = linear_search(data, search)
        print("Index of", search, ":", res)


if __name__ == "__main__":
    main()
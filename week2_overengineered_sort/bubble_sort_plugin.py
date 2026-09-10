class bubble_sort_plugin:
    def sort(self, arr):
        # Bubble sort
        n = len(arr)
        for i in range(n):
            for j in range(n-i-1):
                sorted = True
                if arr[j] > arr[j+1]:
                    sorted = False
                    arr[j], arr[j+1] = arr[j+1], arr[j]
            if sorted:
                break

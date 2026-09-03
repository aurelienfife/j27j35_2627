import bubble_sort_plugin as bs
import sortable_array as sortable

def main():
    arr = [3,7,1,10,22,56,5,16]
    plugin = bs.bubble_sort_plugin()
    sarr = sortable.Sortable_array(arr, plugin)

    print(sarr.arr)
    sarr.sort
    print(sarr.arr)


if __name__ == "__main__":
    main()
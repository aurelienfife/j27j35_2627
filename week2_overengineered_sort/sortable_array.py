class Sortable_array:
    def __init__(self, arr, sort_plugin):
        self.arr = arr
        self.sort_plugin = sort_plugin

    def sort(self):
        self.arr = self.sort_plugin.sort(self.arr)



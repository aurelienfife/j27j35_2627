# Binary Search Tree - Class demo 19/11/2026
# This was the day of release of GTA VI and only one person was missing

# Tree node: data and two children
class Node:
    def __init__(self, data):
        self.data = data   # Set the node's data with argument value
        self.left = None   # Empty pointer to another node
        self.right = None  # Empty pointer to another node

# Tree class - constructor sets root to empty pointer
class BSTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        # Create new Node with the data
        new_node = Node(data)

        # If root is still empty, set the root to the new Node
        if self.root is None:
            self.root = new_node
            return

        # You may want trees allowing duplicates, or not
        # if value is in tree already, just end
        if self.root.data == data:
            return
        # Else, insert left/right based on comparison
        else:
            current = self.root
            parent = None
            # Loop indefinitely
            while True:
                parent = current
                # If the value we want to insert is less than current
                # Set current to its left child
                if new_node.data < parent.data:
                    current = current.left
                    # if the new "current" is empty
                    # set it to new node and end loop
                    if current is None:
                        current = new_node      # Set current node
                        parent.left = current   # Link with parent
                        return                  # End loop
                # Else set current to right child
                else:
                    current = current.right
                    # Same process as on right
                    if current is None:
                        current = new_node
                        parent.right = current
                        return


    # This method will convert the tree to a string representation
    # To use in a print() statement
    # Tree represented as string (recursive)
    def __str__(self):
        def append_r(node, level):
            s = ""
            if node is not None:
                s += append_r(node.right, level+1)
                s += "| " * level
                s += str(node.data) + "\n"
                s += append_r(node.left, level+1)
            return s
        return append_r(self.root, 0)




# Test code for the tree
def main():
    # To create a new tree, you need to set up a new Tree object
    # And insert its first value

    t = BSTree()

    for n in [4,3,5,2,6,1]:
        t.insert(n)

    print(t)



if __name__ == "__main__":
    main()

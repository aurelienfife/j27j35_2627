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

    def get_node_with_parent(self, data): 
        parent = None 
        current = self.root 
        if current is None: 
            return (parent, None) 
        while True: 
            if current.data == data: 
                return (parent, current) 
            elif current.data > data: 
                parent = current 
                current = current.left 
            else: 
                parent = current 
                current = current.right
        return (parent, current) 

    
    def remove(self, data):  
        parent, node = self.get_node_with_parent(data)  
 
        if parent is None and node is None:  
            return False  
 
        # Get children count  
        children_count = 0  
 
        if node.left_child and node.right_child:  
            children_count = 2  
        elif (node.left_child is None) and (node.right_child is None):  
            children_count = 0  
        else:  
            children_count = 1  
        
        if children_count == 0:  
            if parent:  
                if parent.right_child is node:  
                    parent.right_child = None  
                else:  
                    parent.left_child = None  
            else:  
                self.root_node = None 
        elif children_count == 1:  
            next_node = None  
            if node.left_child:  
                next_node = node.left_child  
            else:  
                next_node = node.right_child  
 
            if parent:  
                if parent.left_child is node:  
                    parent.left_child = next_node  
                else:  
                    parent.right_child = next_node  
            else:  
                self.root_node = next_node  
        else:  
            parent_of_leftmost_node = node  
            leftmost_node = node.right_child  
            while leftmost_node.left_child:  
                parent_of_leftmost_node = leftmost_node  
                leftmost_node = leftmost_node.left_child  
            node.data = leftmost_node.data       
    
            if parent_of_leftmost_node.left_child == leftmost_node:  
                parent_of_leftmost_node.left_child = leftmost_node.right_child  
            else:  
                parent_of_leftmost_node.right_child = leftmost_node.right_child


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

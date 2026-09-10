# Basic linked list example - Python 3
# Node class
# Create five elements -> append function
# Traverse and display -> traverse

# Node class
# 2 attributes: value, and next
# Initialiser takes a value, but None by default
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None # Keyword none explicitly sets a variable as "not set"

def main():
    # Create three nodes manually
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)

    # link them manually
    n1.next = n2
    n2.next = n3

    # Basic traversal
    # We don't know how many nodes there are
    # So a while loop is more appropriate

    current = n1

    while current != None:
        print(current.value)
        current = current.next


if __name__ == "__main__":
    main()

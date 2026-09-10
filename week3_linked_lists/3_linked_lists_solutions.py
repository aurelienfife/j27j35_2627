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

# Single Linked List contains a head node
# append function
class SingleLinkedList:
    def __init__(self):
        self.head = None

    # If the head Node doesn't exist, create it
    # Otherwise, traverse until the end and add new Node to the back
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            # Traverse linearly to last element
            current = self.head
            while current.next:
                current = current.next
            # current is now last elememnt, new_node becomes next
            current.next = new_node

    def display(self):
        if not self.head:
            return
        else:
            current = self.head
            while current:
                print(current.value)
                current = current.next

    def search(self, value):
        if not self.head:
            return None
        else:
            current = self.head
            while current:
                if current.value == value:
                    return current.value
                current = current.next
            return None

    def delete(self, value):
        if not self.head:
            return
        elif self.head.value == value:
            self.head = self.head.next
        else:
            current = self.head
            while current.next:
                if current.next.value == value:
                    current.next = current.next.next
                    return
                current = current.next



def main():

    # Create a new list
    new_list = SingleLinkedList()
    for i in range(1,4):
        new_list.append(i)


    

if __name__ == "__main__":
    main()

# Queue class based with a linked list implementation

# FIFO  -   First-in-first-out

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Queue has front and rear
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    # Add an element to the rear of the queue
    def enqueue(self, data):
        new_node = Node(data)

        # If single element, front and rear are the same
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
            return

        # Define "next" of current rear to new element
        # Then define new rear to new element         
        self.rear.next = new_node
        self.rear = new_node

    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek at an empty queue")

        return self.front.data

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Cannot dequeue an empty queue")

        # Return value of front element
        value = self.front.data
        # Make new from the next element
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return value
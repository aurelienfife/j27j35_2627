# Queue class based with a linked list implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.front = new_node
            self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek at an empty queue")

        return self.front.data

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Cannot dequeue an empty queue")

        value = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return value
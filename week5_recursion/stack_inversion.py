# Node class

class Node:
    def __init__(self, data):
        # Create a node to store one stack value and link it to the next node.
        self.data = data
        self.next = None


class Stack:
    """A LIFO stack implemented with linked nodes."""

    def __init__(self):
        # Create an empty stack with no top node.
        self.top = None

    def is_empty(self):
        # Check whether the stack currently contains no nodes.
        # The stack is empty when it has no top node.
        return self.top is None

    def push(self, data):
        # Add a new value to the top of the stack.
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        # Remove and return the value at the top of the stack.
        if self.is_empty():
            raise IndexError("pop from empty stack")
        popped_node = self.top
        self.top = self.top.next
        return popped_node.data

    def peek(self):
        return self.top.data


def main():
    nums = [1,2,3,4,5]
    s = Stack()

    for n in nums:
        print('Pushing', n, 'in s')
        s.push(n)

    print(s.peek())


    s2 = Stack()
    while not s.is_empty():
        n = s.pop()
        print('Popping', n, 'from s')
        print('Pushing into s2')
        s2.push(n)

    print(s2.peek())
    



if __name__ == "__main__":
    main()

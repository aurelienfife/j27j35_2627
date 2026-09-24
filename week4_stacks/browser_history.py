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

history = Stack()
current_page = "Home"

def visit(page):
    global current_page
    global history

    history.push(current_page)
    current_page = page




def go_back():
    global current_page
    global history

    if not history.is_empty():
        current_page = history.pop()
    return current_page



def main():
    print(current_page)

    visit("Products")
    visit("Basket")
    visit("Checkout")

    print(current_page)
    print(go_back())
    print(go_back())
    print(go_back())
    print(go_back())

if __name__ == "__main__":
    main()

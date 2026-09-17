# Node class
class Node:
    def __init__(self, data):
        # Create a node to store one stack value and link it to the next node.
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        # When creating stack, the top element is empty
        self.top = None

    def push(self, data):
        # Pushing new value:
        # 1. create new node
        # 2. set node's next as current top
        # 3. set new "top" as new node
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def is_empty(self):
        return self.top is None

    # Allows us to check the data at the top of the stack
    def peek(self):
        return self.top.data

    def pop(self):
        if not self.is_empty():
            # 1. save top in temp variable
            # 2. set new top to next
            # 3. return the value
            value = self.top.data
            self.top = self.top.next
            return value
        


    

def main():
    s = Stack()
    for i in range(5):
        s.push(i)
        print("The top element is now:", s.peek())

    while not s.is_empty():
        print(s.pop())

    print()

if __name__ == "__main__":
    main()
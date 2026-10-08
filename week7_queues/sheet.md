# Week 6 Queue Exercises

These exercises apply queues to simple first-come, first-served problems. Use the `Node` class from the linked-list work and the supplied `Queue` class below.
OpenAI/Codex was used to suggest ideas and format this document in Markdown.

## Learning goals

By the end of these exercises, you should be able to:

- explain first in, first out behaviour
- use `enqueue`, `dequeue`, `peek` and `is_empty`
- trace the front and rear of a queue
- apply a queue to orders and print jobs
- distinguish queue behaviour from stack behaviour

## Supplied queue class

You do not need to memorise this implementation. The important part is how the queue behaves.

```python
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
```

## Exercise 1: Trace a queue

A café receives orders in this order:

```python
orders = Queue()

orders.enqueue("Tea")
orders.enqueue("Coffee")
orders.enqueue("Soup")

print(orders.peek())
print(orders.dequeue())

orders.enqueue("Sandwich")

print(orders.dequeue())
print(orders.peek())
```

Without running the code, record the queue after each operation.

Use this format:

```text
Front -> Tea, Coffee, Soup <- Rear
```

Then predict the four values printed by the program.

### Hints

- `enqueue()` adds an item at the rear.
- `dequeue()` removes an item from the front.
- `peek()` returns the front item without removing it.
- The first item added is the first item removed.

### Questions

1. Which item remains at the front after `Tea` is removed?
2. Does `peek()` change the queue?
3. Why does `Sandwich` join behind `Soup`?
4. How would a stack process the same four orders differently?

## Exercise 2: Café order queue

Create a small order-processing program. Customers should receive their orders in the same order that the café accepted them.

### Required behaviour

- `place_order()` adds a new order to the rear of the queue.
- `next_order()` removes and returns the oldest order.
- Calling `next_order()` on an empty queue returns `"No orders waiting"`.
- `show_next_order()` returns the oldest order without removing it.

### Starter code

```python
orders = Queue()


def place_order(customer, item):
    order = {
        "customer": customer,
        "item": item,
    }

    # Add the order to the queue.
    pass


def next_order():
    # Check whether an order is available.
    # Remove and return the oldest order.
    pass


def show_next_order():
    # Check whether an order is available.
    # Return the oldest order without removing it.
    pass
```

### Test code

```python
place_order("Amina", "Tea")
place_order("Ben", "Soup")
place_order("Cara", "Coffee")

print(show_next_order())
print(next_order())
print(next_order())
print(show_next_order())
print(next_order())
print(next_order())
```

Expected output:

```text
{'customer': 'Amina', 'item': 'Tea'}
{'customer': 'Amina', 'item': 'Tea'}
{'customer': 'Ben', 'item': 'Soup'}
{'customer': 'Cara', 'item': 'Coffee'}
{'customer': 'Cara', 'item': 'Coffee'}
No orders waiting
```

### Code hints

- Pass the whole `order` dictionary to `enqueue()`.
- Call `is_empty()` before calling `dequeue()` or `peek()`.
- `next_order()` should use `dequeue()`.
- `show_next_order()` should use `peek()`.
- Return the string exactly as shown when the queue is empty.

Pseudocode:

```text
PLACE_ORDER customer, item
    CREATE an order containing customer and item
    ENQUEUE the order

NEXT_ORDER
    IF the queue is empty
        RETURN No orders waiting
    RETURN DEQUEUE from the queue

SHOW_NEXT_ORDER
    IF the queue is empty
        RETURN No orders waiting
    RETURN PEEK at the queue
```

### Questions

1. Why does Amina's order leave before Ben's order?
2. What is stored in each queue node?
3. Why should the program check `is_empty()` first?
4. When might strict first-come, first-served processing be inappropriate?

## Exercise 3: Printer job queue

An office printer receives documents from several users. Each print job contains a document name and a number of pages.

Complete the functions below.

### Starter code

```python
print_queue = Queue()


def add_print_job(document, pages):
    job = {
        "document": document,
        "pages": pages,
    }

    # Add the job to the rear of the queue.
    pass


def print_next_job():
    if print_queue.is_empty():
        return "Printer idle"

    # Remove the oldest job.
    job = ____________________

    return f"Printing {job['document']} ({job['pages']} pages)"
```

### Test code

```python
add_print_job("report.pdf", 4)
add_print_job("diagram.png", 1)
add_print_job("notes.txt", 2)

print(print_next_job())
print(print_next_job())

add_print_job("invoice.pdf", 1)

print(print_next_job())
print(print_next_job())
print(print_next_job())
```

Expected output:

```text
Printing report.pdf (4 pages)
Printing diagram.png (1 pages)
Printing notes.txt (2 pages)
Printing invoice.pdf (1 pages)
Printer idle
```

### Code hints

- `add_print_job()` should enqueue the whole dictionary.
- `print_next_job()` should dequeue one dictionary.
- Use the dictionary keys inside the formatted string.
- Adding `invoice.pdf` does not move it ahead of `notes.txt`.
- The final call finds an empty queue.

### Further challenge

Improve the output so that a one-page document uses `page` instead of `pages`:

```text
Printing diagram.png (1 page)
Printing report.pdf (4 pages)
```

## Exercise 4: Round-robin print processing

A long print job can block every job behind it. In this exercise, the printer processes at most two pages from the front job. If pages remain, the job returns to the rear of the queue.

Use dictionaries that contain a document name and the number of pages remaining:

```python
print_queue = Queue()

print_queue.enqueue({"document": "report.pdf", "remaining": 5})
print_queue.enqueue({"document": "diagram.png", "remaining": 1})
print_queue.enqueue({"document": "notes.txt", "remaining": 3})
```

Complete the function:

```python
def process_turn():
    if print_queue.is_empty():
        return "Printer idle"

    job = ____________________

    pages_printed = min(2, job["remaining"])
    job["remaining"] = job["remaining"] - pages_printed

    message = (
        f"Printed {pages_printed} page(s) from {job['document']}"
    )

    if job["remaining"] > 0:
        # Put the unfinished job at the rear of the queue.
        ____________________
    else:
        message = message + " - complete"

    return message
```

### Test code

```python
while not print_queue.is_empty():
    print(process_turn())
```

Expected output:

```text
Printed 2 page(s) from report.pdf
Printed 1 page(s) from diagram.png - complete
Printed 2 page(s) from notes.txt
Printed 2 page(s) from report.pdf
Printed 1 page(s) from notes.txt - complete
Printed 1 page(s) from report.pdf - complete
```

### Code hints

- Begin each turn by dequeuing the front job.
- Change the `remaining` value in the dictionary.
- Re-enqueue the same dictionary when pages remain.
- Do not re-enqueue a completed job.
- Trace the front and rear of the queue after every turn.

### Questions

1. Why does an unfinished job return to the rear?
2. Which operation gives another job its turn?
3. How is this different from printing each document completely before starting the next?
4. Does the queue still follow first in, first out behaviour within each round?

## Using Python's deque

Deque stands for "double ended-queue" is not the same as "dequeue()" (de-queue), the method in the other class provided.
Python also provides `collections.deque`, which can act as a queue:

```python
from collections import deque

queue = deque()
queue.append("first")
queue.append("second")

print(queue.popleft())
```

The course exercises use the supplied `Queue` class so that the front, rear and linked nodes remain visible.

## Reference examples

- [W3Schools: Queues with Python](https://www.w3schools.com/python/python_dsa_queues.asp)
- [GeeksforGeeks: Queue in Python](https://www.geeksforgeeks.org/python/queue-in-python/)
- [Python documentation: Using Lists as Queues](https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-queues)
- [Python documentation: collections.deque](https://docs.python.org/3/library/collections.html#collections.deque)

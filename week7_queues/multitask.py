from queue import Queue
import time 


# Multitasking queue
task_queue = Queue()

# Initial processes
processes = [10, 5, 8]

for i in range(len(processes)):
    process = {
        "index": i,
        "instructions_left": processes[i]
    }

    # Add process to queue
    task_queue.enqueue(process)

print("Tasks queued in")

# while queue is not empty
while not task_queue.is_empty():
    # Take process at front of queue
    current_process = task_queue.dequeue()

    # Visual feedback
    current_process["instructions_left"] -= 1
    print(f'''Process number: {current_process["index"]}
    , instructions left:{current_process["instructions_left"]}''')

    # If instructions are left, send to back of queue
    if current_process["instructions_left"] > 0:
        task_queue.enqueue(current_process)

    # Suspend 50ms for visualisation purposes
    time.sleep(0.25)

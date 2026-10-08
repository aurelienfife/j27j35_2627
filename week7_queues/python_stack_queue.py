# Python can let you use a Python list as a queue
browser_history = []  # Just a basic Python list

pages = ["Home", "Products", "Checkout"]
for p in pages:
    browser_history.append(p)     # That's equivalent to a push

print("Browser history stack")
print(browser_history)

# Simulate a back button click until end of history
while len(browser_history) > 0:
    p = browser_history.pop()   # Pop method exists on Python lists
    print(p)


# In Python you have the deque object 
# deque -> double-ended queue
# Not the same as dequeue -> action of dequeuing value


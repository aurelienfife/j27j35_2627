def countdown_iterative(n):
    for i in range(n, 0, -1):
        print(i)
    print("Go!")


def countdown(n):   # Recursive version
    # Base case
    if n == 0:
        print("Go!")
        return
    else:          # Recursive case
        print(n)
        countdown(n-1)

def add(n):
    if n==1:
        return n
    else:
        return n+add(n-1)




# countdown_iterative(5)
countdown(5)

print(add(5))
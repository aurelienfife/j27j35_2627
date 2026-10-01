from stack import Stack
# for testing
import copy

poles = {
    "source" : Stack(),
    "middle" : Stack(),
    "destination" : Stack()
}


# For testing
def display_stack(s):
    s2 = copy.deepcopy(s)
    while not s2.is_empty():
        print(s2.pop(), sep='')

# Pass the names of the poles
# Determine legal move
# Make move
def make_move(left, right):
    # Peek left / right to see what move is legal
    left_top = poles[left].peek()
    right_top = poles[right].peek()

    # In case one stack is empty change to int
    # To avoid crash
    if left_top is None:
        left_top = 0
    if right_top is None:
        right_top = 0

    if (left_top < right_top) or ((left_top > right_top) and right_top == 0):
        temp = poles[left].pop()
        poles[right].push(temp)
        # For debugging
        print(left, "->", right)
    else:
        temp = poles[right].pop()
        poles[left].push(temp)
        # For debugging
        print(left, "<-", right)




def solve_hanoi(poles, n):

    # push the disks on the stack
    for move_counter in range(n, 0, -1):
        poles["source"].push(move_counter)

    # For testing:
    print("Source stack at beginning:")
    display_stack(poles["source"])


    # Number of moves
    num_moves = 2**n-1

    # Loop from 1 to num_moves included
    for move_counter in range(1, num_moves + 1):
        if move_counter%3==1:
            make_move("source", "destination")
        elif move_counter%3==2:
            make_move("source", "middle")
        elif move_counter%3==3:
            make_move("middle", "destination")

        print("----------------------")
        display_stack(poles["source"])
        display_stack(poles["middle"])
        display_stack(poles["destination"])

    

solve_hanoi(poles, 5)

# Do tower of Hanoi resolution using pop / push
# Remember to check if l -> r or r -> l is legal move


''' Pseudocode from Geeks for geeks
2. If number of disks (i.e. n) is even then interchange destination pole and auxiliary pole.
3. for i = 1 to total number of moves 

if i%3 == 1: legal movement of top disk between source pole and destination pole
if i%3 == 2: legal movement of top disk between source pole and auxiliary pole    
if i%3 == 0: legal movement of top disk between auxiliary pole and destination pole 
'''

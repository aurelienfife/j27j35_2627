from stack import Stack

poles = {
    "source" : Stack(),
    "middle" : Stack(),
    "destination" : Stack()
}

for n in [3,2,1]:
    poles["source"].push(n)

# Create a resolve function
# Takes the dictionary
# Counts how many disks on source pole
# Calculate the number of moves
# Do tower of Hanoi resolution using pop / push
# Remember to check if l -> r or r -> l is legal move


''' Pseudocode from Geeks for geeks
1. Calculate the total number of moves required i.e. "pow(2, n) - 1" here n is number of disks.
2. If number of disks (i.e. n) is even then interchange destination pole and auxiliary pole.
3. for i = 1 to total number of moves 

if i%3 == 1: legal movement of top disk between source pole and destination pole
if i%3 == 2: legal movement of top disk between source pole and auxiliary pole    
if i%3 == 0: legal movement of top disk between auxiliary pole and destination pole 
'''

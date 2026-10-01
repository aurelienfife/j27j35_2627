# From the stack module import the Stack class
# without the need to prefix it with the module name
from stack import Stack

# Create empty stacks in a list, index 0, 1, 2
poles = [Stack(), Stack(), Stack()]

for i in [3,2,1]:
    poles[0].push(i)

# Function takes number of disks, start and end
def hanoi(count, start, end):
    # Index in list of stacks: 0, 1, 2
    
    # For calculations we do 1, 2, 3
    # Other pole is 6 - start+end
    other = 6 - start - end

    # Base case - end of the function
    if count == 1:
        # Make move
        print(start,"->",end)
        # temp = poles[start-1].pop()
        # poles[end-1].push(temp)
        return

    # Recursive call
    hanoi(count-1, start, other)
    # Move bottom to end
    # temp = poles[start-1].pop()
    # poles[end-1].push(temp)
    print(start,"->",end)
    hanoi(count-1, other, end)

hanoi(4,1,3)
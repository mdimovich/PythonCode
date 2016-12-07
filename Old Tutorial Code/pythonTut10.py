#Drawing a pine tree on the screen
#How tall is the tree: 5


height = input ("How tall is the tree: ")
height = int(height)
#Get the starting spaces for the top of tree
spaces = height - 1

hashes = 1

stump_spaces = height - 1
#Make sure right number of rows are printed
while height != 0:
    for i in range(spaces):
        print(' ', end="")
    for i in range(hashes):
        print('#', end="")
    print()

    spaces -= 1
    hashes += 2
    height -= 1
#Print the spaces
#end="" means new line wont start
#print("hello",end="")
#Print the hashes
for i in range(stump_spaces):
    print(' ',end="")
print("#")
#Newline after each row is printed

#Spaces decremented by 1 each time

#Hashes is incremented by 2 each time

#Decrement tree height each time to jump out of loop

#Print the spaces before stump and the final hash


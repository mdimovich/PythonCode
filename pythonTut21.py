# Learning lists in python
import random
import math

# Python lists can grow in size and can contain different types of data, unlike other languages

randList = ["michael", 1.345, 7, 'c', "blah"]

oneToTen = list(range(10))

# Concatenate two lists
randList = randList + oneToTen

print(randList)

# Can get length the same way as with strings
print("List length: ", len(randList))

# Make a new list with a range of values from another list
first3 = randList[0:3]

# Get index for the list and the corresponding data
for i in first3:
    print("{} : {}".format(first3.index(i), i))

# Return true if a string is inside the list
print("michael" in first3)

# Generate a list full of random numbers and print them out
numList = []
for i in range(5):
    numList.append(random.randrange(1,9))
for i in numList:
    print(i)
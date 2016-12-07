import math
import random

numList = [1, 2, 3, 4 ,5]

# Generate a list of lists with exponential function
listOfValues = [[math.pow(m, 2), math.pow(m, 3), math.pow(m, 4)] for m in numList]

for i in listOfValues:
    print(i)
print()

# Create a 10 by 10 list
multiDList = [[0] * 10 for i in range(10)]

# Populate a multi dimensional array
for i in range(10):
    for j in range(10):
        multiDList[i][j] = "{} : {}".format(i, j)

# Print out the multi dimensional array
for i in range(10):
    for j in range(10):
        print(multiDList[i][j], end=" || ")
    print()

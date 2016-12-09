# Bubble sort in Python

import random

numList = []
# Generate list of random values
for i in range(10):
    numList.append(random.randrange(1, 15))

i = len(numList)-1
for b in numList:
    print(b, end=", ")
print()

# Bubble Sort Algorithm
while i > 1:
    j = 0
    while j < i:
        if numList[j] > numList[j+1]:
            temp = numList[j]
            numList[j] = numList[j+1]
            numList[j+1] = temp
        else:
            print()
        j += 1
    i -= 1

for k in numList:
    print(k, end=", ")
print()



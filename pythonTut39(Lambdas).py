sum = lambda x, y: x + y

print("Sum : ", sum(4, 5))

can_vote = lambda age: True if age >= 18 else False

print("Can Vote: ", can_vote(19))

powerList = [lambda x: x ** 2, lambda x: x ** 3, lambda x: x ** 4]
for func in powerList:
    print(func(4))

import random

flipList = []
for i in range(1, 101):
    flipList += random.choice(['H', 'T'])

print("Heads: ", flipList.count('H'))
print("Tails: ", flipList.count('T'))

oneToTen = range(1, 11)
def dbl_num(num):
    return num * 2

print(list(map(dbl_num, oneToTen)))

print(list(map(lambda x: x * 3, oneToTen)))

print(list(filter((lambda x: x % 2 == 0), range(1, 11))))

# Find the multiples of 9 from a random 100 value list with values between 1 and 1000

num_list = []
num_list = list(random.randint(1, 1001) for i in range(100))
print(list(filter(lambda x: x % 9 == 0, num_list)))

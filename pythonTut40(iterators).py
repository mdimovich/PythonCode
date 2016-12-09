# Iterators and Iterable
class Alphabet:
    def __init__(self):
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.index = -1
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.letters) - 1:
            raise StopIteration
        self.index += 1
        return self.letters[self.index]

alpha = Alphabet()
for letter in alpha:
    print(letter)

# Create a class that returns the values from the Fibonacci sequence each time next is called
# Fib: 1
# Fib: 2
# Fib: 3
# Fib: 5


class Fib:
    def __init__(self):
        self.first = 0
        self.second = 1

    def __iter__(self):
        return self

    def __next__(self):
        fibNum = self.first + self.second
        self.first = self.second
        self.second = fibNum
        return fibNum

fib_sequence = Fib()
for i in range(10):
    print("Fib: ", next(fib_sequence))

# List Comprehensions
print([x for x in range(1, 11) if x % 2 != 0])
# Generate 50 values -> Take to the power of 2 -> Return multiples of 8
print([i ** 2 for i in range(50) if i % 8 == 0])
print([x * y for x in range(1, 3) for y in range(11, 16)])
print([x for x in [i * 2 for i in range(10)] if x % 8 == 0])

# Problem: Generate list of 50 random values between 1 and 1000 -> Return multiples of 9
import random
print([x for x in[random.randint(1, 1001) for i in range(1, 50)] if x % 9 == 0])

multi_list = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

print([col[1] for col in multi_list])
print([multi_list[i][i] for i in range(len(multi_list))])

# Generator Functions
def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def gen_primes(max_number):
    for num1 in range(2, max_number):
        if isPrime(num1):
            yield num1

prime = gen_primes(50)
print("Prime: ", next(prime))
print("Prime: ", next(prime))
print("Prime: ", next(prime))
print("Prime: ", next(prime))
print("Prime: ", next(prime))
print("Prime: ", next(prime))
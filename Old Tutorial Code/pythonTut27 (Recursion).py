# Recursive Functions in Python

# Recursive Factorial Function
def factorial(num):
    if num <= 1:
        return 1
    else:
        result = num * factorial(num-1)
        return result

print(factorial(4))


# 1, 1, 2, 3, 5, 8, 13
# Fibonacci Sequence: Fn = Fn-1 + Fn-2
# Where F0 = 0 and F1 = 1

def fibonacci(num):
    if num == 0:
        return 0;
    elif num == 1:
        return 1;
    else:
        result = fibonacci(num-1)+fibonacci(num-2)
        return result

amount = int(input("Enter the numer of fibonacci numbers you want: "))
for i in range(1, amount+1):
    print(fibonacci(i))

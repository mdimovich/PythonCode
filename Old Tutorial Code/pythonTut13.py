import math
from decimal import Decimal as D
print("Ceiling of 4.4: ", math.ceil(4.4))
print("Floor of 4.4: ", math.floor(4.4))
print("Absolute value of -4.4: ", math.fabs(-4.4))
print("Factorial of 4: ", math.factorial(4))
print("Remainder of 5/4: ", math.fmod(5,4))

sum = D(0)
sum+=D("0.1")
sum+=D("0.1")
sum+=D("0.1")
sum -= D("0.3")
print("Sum: ", sum)
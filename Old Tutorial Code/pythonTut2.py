#Ask the user to input 2 values and store them in variables num and num2

num1, num2 = input("Input two Numbers: ").split()

#Convert the strings into regular integers

num1 = int(num1)
num2 = int(num2)

#Add the values entered and store in variable sum
sum = num1+num2
#Subtract values and store in difference
difference = num1-num2
#Multiply the values and store in product
product = num1*num2
#Divide the values and store in quotient
quotient = num1 / num2
#Use modulus on the values to find the remainder
remainder = num1%num2
#Print the results on the screen for the user
print("{} + {} = {} ".format(num1,num2, sum))
print("{} - {} = {} ".format(num1,num2, difference))
print("{} * {} = {} ".format(num1,num2, product))
print("{} / {} = {} ".format(num1,num2, quotient))
print("{} % {} = {} ".format(num1,num2, remainder))
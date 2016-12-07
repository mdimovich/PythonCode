#Provide different output based on age
# 1-18 -> Important; 21, 50, >65 ->Important
#All others -> Not important

#Receive and store variable age
age = eval(input("Enter age: "))
#If age is both greater than or equal to 1 and less than or equal to 18, print important
if (age >= 1) and (age<= 18):
    print("Important Birthday")
#If age is 21 or 50, important
elif (age == 21) or (age == 50):
    print("Important Birthday")
#Check if age is less than 65 and then convert true to false
elif not (age < 65):
    print("Important Birthday")
else:
    print("Sorry not important")
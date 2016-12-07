#If age is 5 print Go to kindergarten
#Ages 6 through 17 goes to grades 1-12
#If age is greater than 17 say go to college
# Try to complete this program with 10 or less lines

#Ask for age and handle if age < 5
age = eval(input("Enter age: "))
#Special output for kindergarten
if(age == 5):
    print("Go to kindergarten")
#output for grade school
elif (age > 5) and (age <= 17):
    grade = age - 5
    print("Go to grade {}".format(grade))
#Output for college
elif(age >= 18):
    print("Go to college")
else:
    print("Too young for school")
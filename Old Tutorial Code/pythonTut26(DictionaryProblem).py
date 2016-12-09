# Create a customer list
# Enter Customer -> Enter customer name -> continue until someone says no

customerList = []
confirm = input("Enter customer: ")
while confirm != 'n':
    fName, lName = input("Enter customer name: ").split()
    customerList.append({'fName': fName, 'lName': lName})
    confirm = input("Enter customer: ")

for i in customerList:
    print(i['fName'], i['lName'])


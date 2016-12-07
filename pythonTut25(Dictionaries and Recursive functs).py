mikeDictionary = {"fname": "Michael", "lname": "Dee", "address": "123 Blah Street"}

print("Print name: ", mikeDictionary["fname"])

# Change something inside the list with normal assignment operator
mikeDictionary["address"] = "2333 Bob Lane"

# Add a new key
mikeDictionary['city'] = "Detroit"

# Returns true if there is a key named city in the dictionary
print("Is there a city: ", "city" in mikeDictionary)

# Print out just the values or just the keys
print(mikeDictionary.values())
print(mikeDictionary.keys())

# Print both the keys and values using a for loop
for k, v in mikeDictionary.items():
    print(k, v)

# Delete a dictionary key
del mikeDictionary["fname"]

# Clear all data from dictionary
mikeDictionary.clear()

# Creating a list of dictionaries
employees = []
fName, lName = input("Enter Employee Name: ").split()
employees.append({'fName': fName, 'lName': lName})
print(employees)
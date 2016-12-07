# Create an acronym generator
# Random Access Memory: RAM
theString = input("Enter a string: ")
theString = theString.upper()
aList = theString.split()
for word in aList:
    print(word[0], end="")
print()



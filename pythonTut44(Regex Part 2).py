import re

owlFood = "rat cat mat pat"

randStr = '''This is a long
string that goes on
for many lines
'''

# Replace cat and rat with owl, but not mat and pat
regex = re.compile("[cr]at")
owlFood = regex.sub("owl", owlFood)
print(owlFood)

# Remove new lines and replace them with spaces
regex = re.compile("\n")
randStr = regex.sub(" ", randStr)
print(randStr)

# Number Regex: How many characters are 1-9
numStr = "12345"
print("Matches: ", len(re.findall("\d", numStr)))

# Number Regex: Find Numbers Between 5 and 7 digits
numStr2 = "123 12345 123456 1234567"
print("Matches: ", len(re.findall("\d{5,7}", numStr2)))

# Regex: Matching alphanumeric characters to see if its formatted like a phone number
phone = "412-555-1212"
if re.search("\w{3}-\w{3}-\w{4}", phone):
    print("it is a phone number")

# Regex: Finding a name between 2-20 characters and space between first/last name
if re.search("\w{2,20}\s\w{2,20}", "Ultraman Toshiio"):
    print("Is a valid name")

# Problem: Make a regex that matches an e-mail address from a list
# 1-20 lower/upper case letters,numbers, plus ._%t-
# Followed by @ symbol
# Followed by 2-20 lower/uppercase letters, numbers, plus .-
# Followed by a period
# Followed by 2 to 3 lower/uppercase letters
email = "mikedee@email.net"
if re.search("[\w._%+-{1,20}@[\w.-{1,20}].[a-zA-Z]{2,3}", email):
    print("Its an email")
    print(email)



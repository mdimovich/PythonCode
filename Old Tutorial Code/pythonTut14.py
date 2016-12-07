# Enter a string to hide in uppercase
# Secret Message:
# Original Message:
# 1. Accept uppercase string from user
# 2. Run through the string converting each character to unicode and putting them in a new string
# 3. Print Secret Message
# 4. Convert back to characters by cycling through 2 at a time and print the original message
# To make it work with lowercase letters too, need to convert 97-122 to two digit values
# Subtract by 23
orig = input("Enter a string to hide in uppercase: ")
secret = ""
newOrig = ""
for i in range(0, len(orig)):
    secret += str(ord(orig[i]) - 23)
print("Secret message: ", secret)
for i in range(0, len(secret), 2):
    origInt = chr(int(secret[i]+secret[i+1])+23)
    newOrig += str(origInt)


print("Original Message: ", newOrig)
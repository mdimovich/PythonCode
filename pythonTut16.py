# Python Learn To Program Lecture 4

letter_z = "z"
num_3 = "3.14"
a_space = " "

print("Is z uppercase: ", letter_z.isupper())
print("Is z alphanumeric: ", letter_z.isalnum())


def isfloat(str_val):
    try:
        float(str_val)
        return True
    except ValueError:
        return False

print("Is Pi a Float: ", isfloat(num_3))

# Problem: Implement a Caesar Cipher
# 1. Pass a message to be encrypted
# 2. Shift the values a set length

message = input("Enter the message to encrypt: ")
key = int(input("Enter the number of chars to shift: "))

secret_message = ""

# Cycle through each character in message
for char in message:
    if char.isalpha():
        char_code = ord(char)
        char_code += key
        if char.isupper():
            if char_code > ord('Z'):
                char_code -= 26
            elif char_code < ord('A'):
                char_code += 26
        else:
            if char_code > ord('z'):
                char_code -= 26
            elif char_code < ord('a'):
                char_code += 26
        secret_message += chr(char_code)
    else:
        secret_message += char
print("Encrypted: ", secret_message)
key = -key
orig_message = ""
for char in secret_message:
    if char.isalpha():
        char_code = ord(char)
        char_code += key
        if char.isupper():
            if char_code > ord('Z'):
                char_code -= 26
            if char_code < ord('A'):
                char_code += 26
        else:
            if char_code > ord('z'):
                char_code -= 26
            if char_code < ord('a'):
                char_code += 26
        orig_message += chr(char_code)
    else:
        orig_message += char
print("Decrypted: ", orig_message)









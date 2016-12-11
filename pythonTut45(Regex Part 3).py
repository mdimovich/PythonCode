import re

# Regex: Match for both cat and cats
randStr = "cat cats"
regex = re.compile("[cat]+s?")
matches = re.findall(regex, randStr)
for i in matches:
    print(i)

# Regex: Match for doctor,doctors, and doctor's
randStr2 = "doctor doctors doctor's"
regex = re.compile("[doctor]+['s]*")
matches = re.findall(regex, randStr2)
for i in matches:
    print(i)

# Regex Problem: Grab each of the lines in a string
multiStr = '''Have some words
and some more\r
and more
'''

regex = re.compile("[\w\s]+[\r]?\n")
matches = re.findall(regex, multiStr)
for i in matches:
    print(i)

# Regex: Get strings between the XML tags
newStr = "<name>Life on mars</name><name>Freaks and Geeks</name>"
regex = re.compile("<name>.*?</name>")
matches = re.findall(regex, newStr)
for i in matches:
    print(i)

# Regex: Get the first word of each line
animStr = '''Ape is big
Turtle is slow
Cheetah is fast
'''

regex = re.compile(r"(?m)^.*?\s")
matches = re.findall(regex, animStr)
print(len(matches))
for i in matches:
    print(i)

# Regex: Get phone numbers minus the area codes
phoneStr = "412-555-1212 412-555-1213 412-555-1214"
regex = re.compile(r"412-(.{8})")
matches = re.findall(regex, phoneStr)
print(len(matches))
for i in matches:
    print(i)

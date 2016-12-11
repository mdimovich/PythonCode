import re

# Regex: Back References
rand = "<a href='#'><b>The Link</b></a>"

# Replace the bold tags and keep the link in there
regex = re.compile(r"<b>(.*?)</b>")

# Substitute using a back reference
rand = re.sub(regex, r"\1", rand)

# Output Result: <a href='#'>The Link</a>
print(rand)

matches = re.findall(regex, rand)

print("Matches: ", len(matches))

for i in matches:
    print(i)

# Regex: Match the phone number using multiple sub expressions
# Want output to look like: (412)555-1212

randStr = "412-555-1212"
regex = re.compile(r"([\d]{3})-([\d]{3}-[\d]{4})")
randStr = re.sub(regex, r"(\1)\2", randStr)
print(randStr)


# Generate multiplication table using a multi-dimensional list
multList = [[0] * 10 for i in range(10)]

# Populate the table
for i in range(1, 10):
    for j in range(1, 10):
        multList[i][j] = i * j

# Print the table
for i in range(1, 10):
    for j in range(1, 10):
        print(multList[i][j], end=" || ")
    print()



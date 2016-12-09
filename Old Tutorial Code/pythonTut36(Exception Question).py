try:
    file = open("mydata2.txt", 'r', encoding="utf-8")
    # f.write("This is a test")
except FileNotFoundError as ex:
    print("File Not Found")
    print(ex)
else:
    print(file.read())
finally:
    print("Finished working with file.")

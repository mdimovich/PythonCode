import os

with open("mydata.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("Some random text \nMore random text \nEven more text")

# os.rename("mydata.txt", "mydata2.txt") -> Rename
# os.remove("mydata2.txt")
# os.mkdir("mydir") -> Create Directory
# os.chdir("mydir") -> Change into the new directory
# os.getcwd() -> Get the current working directory
# os.rmdir("mydir") -> Remove directory
with open("mydata.txt", encoding="utf-8") as myFile:
    lineNum = 1

    while True:
        line = myFile.readline()

        if not line:
            break

        print("Line",lineNum," : ", line, end="")

        wordList = line.split()

        print("# of Words: ", len(wordList))
        charCount = 0
        for word in wordList:
            for char in word:
                charCount += 1
        avgNumChars = charCount/len(wordList)
        print("Average word Length: {:.2f}".format(avgNumChars))
        lineNum += 1

class DogNameError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

try:
    aList = [1, 2, 3]
    dogName = input("What is your dogs name: ")
    if any(char.isdigit() for char in dogName):
        raise DogNameError
    #print(aList[3])

except IndexError:
    print("Sorry that index doesn't exist")
except DogNameError:
    print("Your dogs name can't contain a number")
import sum


class Sum:

    @staticmethod
    def getSum(*args):
        sum = 0
        for i in args:
            sum += i
        return sum

class Dog:
    num_of_dogs = 0

    def __init__(self, name="Unknown"):
        self.name = name

        Dog.num_of_dogs += 1

    @staticmethod
    def getNumOfDogs():
        print("There are currently {} dogs ".format(Dog.num_of_dogs))

def main():
    print("Sum: ", Sum.getSum(1, 2, 3, 4, 5))
    spot = Dog("Spot")
    doug = Dog("Doug")
    spot.getNumOfDogs()
    print("Sum : ", sum.getSum(10,10,15,20))
main()
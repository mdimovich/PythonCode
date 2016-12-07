def isPrime(num):
        for i in range (2, num):
            if (num % i == 0):
                return False

        return True

def getPrimes(max_number):
    listOfPrimes = []

    for num1 in range(2, max_number):
        if isPrime(num1):
            listOfPrimes.append(num1)




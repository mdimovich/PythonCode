# Prime number generator
# Check and see which numbers in a specified range are prime
# User inputs max number to check, and every prime is found up to that number
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

    return listOfPrimes

max_num_to_check = int(input("Search for primers up to: "))
list_of_primes = getPrimes(max_num_to_check)

for prime in list_of_primes:
    print(prime)



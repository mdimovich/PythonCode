import threading
import time
import random

class BankAccount(threading.Thread):
    accountBalance = 100

    def __init__(self, name, moneyRequest):
        threading.Thread.__init__(self)

        self.name = name
        self.moneyRequest = moneyRequest

    def run(self):
        # Get lock to keep other threads from accessing the account
        threadLock.acquire()

        BankAccount.getMoney(self)

        # Release lock so other threads can now access
        threadLock.release()

    @staticmethod
    def getMoney(customer):
        print("{} tries to withdraw ${} at {}".format(customer.name, customer.moneyRequest,
                                                      time.strftime("%H:%M:%S", time.gmtime())))
        if BankAccount.accountBalance - customer.moneyRequest > 0:
            BankAccount.accountBalance -= customer.moneyRequest
            print("New account balance: {}".format(BankAccount.accountBalance))
        else:
            print("Not enough money in account")
            print("Current Balance: {}".format(BankAccount.accountBalance))
        time.sleep(3)

# Create a Lock
threadLock = threading.Lock()

# Create 3 new threads
doug = BankAccount("Doug", 1)
bob = BankAccount("Bob", 100)
sally = BankAccount("Sally", 50)

doug.start()
bob.start()
sally.start()

# Have threads wait for previous threads to terminate
doug.join()
bob.join()
sally.join()
print("Execution Ends")

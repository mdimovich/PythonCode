secret_number = 7

while True:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess == secret_number:
        print("You guessed it")
        break

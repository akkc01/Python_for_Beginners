import random

number = random.randrange(1, 100)

while True:
    guess = int(input("Guess a number between 1 and 100: "))

    if guess < number:
        print("Too low! Try again.")

    elif guess > number:
        print("Too high! Try again.")

    else:
        print("Correct! You won!")
        break
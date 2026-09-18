# import random

# choices = ["rock", "paper", "scissors"]

# computer = random.choice(choices)

# user = input("Choose rock, paper, or scissors: ").lower()

# print("You chose:", user)
# print("Computer chose:", computer)

# if user == computer:
#     print("It's a tie!")

# elif user == "rock" and computer == "scissors":
#     print("You win!")

# elif user == "paper" and computer == "rock":
#     print("You win!")

# elif user == "scissors" and computer == "paper":
#     print("You win!")

# else:
#     print("Computer wins!")


import random

choices = ["rock", "paper", "scissors"]

while True:

    user = input(
        "\nChoose rock, paper, scissors or quit: "
    ).lower()

    if user == "quit":
        print("Thanks for playing!")
        break

    if user not in choices:
        print("Invalid choice!")
        continue

    computer = random.choice(choices)

    print("You:", user)
    print("Computer:", computer)

    if user == computer:
        print("It's a tie!")

    elif (
        (user == "rock" and computer == "scissors")
        or
        (user == "paper" and computer == "rock")
        or
        (user == "scissors" and computer == "paper")
    ):
        print("You win!")

    else:
        print("Computer wins!")
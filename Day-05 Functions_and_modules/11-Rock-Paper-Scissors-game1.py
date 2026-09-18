import random

choices = ["rock", "paper", "scissors"]

wins_against = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

user_score = 0
computer_score = 0

while True:

    user = input(
        "\nChoose rock, paper, scissors or quit: "
    ).lower()

    if user == "q":
        break

    if user not in choices:
        print("Invalid choice!")
        continue

    computer = random.choice(choices)

    print(f"You: {user}")
    print(f"Computer: {computer}")

    if user == computer:
        print("It's a tie!")

    elif wins_against[user] == computer:
        print("You win!")
        user_score += 1

    else:
        print("Computer wins!")
        computer_score += 1

    print(f"Score: You {user_score} - {computer_score} Computer")


print("\n GAME OVER")
print(f"Final Score: You {user_score} - {computer_score} Computer")
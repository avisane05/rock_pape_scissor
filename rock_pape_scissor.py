import random

user_win = 0
computer_win = 0

options = ["rock", "paper", "scissor"]

while True:
    user_input = input("Type Rock/Paper/Scissor or Q o quit: ").lower()

    if user_input == "q":
        break

    if user_input not in options:
        continue
    
    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissor: 2

    computer_pick = options[random_number]

    print("Computer pick", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissor":
        print("You Win!")
        user_win += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You Win!")
        user_win += 1

    elif user_input == "scissor" and computer_pick == "paper":
        print("You Win!")
        user_win += 1

    else:
        print("You Lost!")
        computer_win += 1

print("You won", user_win, "times.")
print("Computer won", computer_win, "times.")
print("GoodBye!")


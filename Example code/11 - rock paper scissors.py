# Import random module so we can generate random numbers
import random

# Get our player choice as a string
print("\nChoices: rock - paper - scissors")
player_choice = input("Which do you choose? -> ")

# Randomly generate a number for our opponent
computer_number = random.randint(0, 2)

# Assign a choice depending on the number
if(computer_number == 0):
    computer_choice = "rock"
elif(computer_number == 1):
    computer_choice = "paper"
else:
    computer_choice = "scissors"

# Output each player's choices before we show the winner
print("\nPlayer: {}\nComputer: {}".format(player_choice, computer_choice))

# If both players choose the same, it's a draw
if(player_choice == computer_choice):
    print("The result is a draw")
# If the player chose rock
elif(player_choice == "rock"):
    if(computer_choice == "paper"):
        print("The computer wins!")
    else:
        print("The player wins!")
# If the player chose paper
elif(player_choice == "paper"):
    if(computer_choice == "scissors"):
        print("The computer wins!")
    else:
        print("The player wins!")
# If the player chose scissors
elif(player_choice == "scissors"):
    if(computer_choice == "rock"):
        print("The computer wins!")
    else:
        print("The player wins!")
# If the player entered anything else
else:
    print("That's not a valid option")

import random
choices = ["rock", "paper", "scissors"]

print("\nChoices: {} - {} - {}".format(choices[0], choices[1], choices[2]))
player_choice = input("Which do you choose? -> ")
computer_choice = random.choice(choices)

print("\nPlayer: {}\nComputer: {}".format(player_choice, computer_choice))

if(player_choice == computer_choice):
    print("The result is a draw")
elif(player_choice == "rock"):
    if(computer_choice == "paper"):
        print("The computer wins!")
    else:
        print("The player wins!")
elif(player_choice == "paper"):
    if(computer_choice == "scissors"):
        print("The computer wins!")
    else:
        print("The player wins!")
elif(player_choice == "scissors"):
    if(computer_choice == "rock"):
        print("The computer wins!")
    else:
        print("The player wins!")
else:
    print("That's not a valid option")

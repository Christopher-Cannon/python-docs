import random

def choice_menu_ui():
    return '''
----------------------------------
Please select an option

Enter a number to select an option
----------------------------------
1 - Rock
2 - Paper
3 - Scissors
----------------------------------
'''

# Get player choice
def choice():
    print(choice_menu_ui())

    while(True):
        # Handle invalid input type
        try:
            user_input = int(input("-> "))
        except:
            print("Invalid input, please try again")
            continue

        # If input is not 1-3 display error
        if((user_input < 1) or (user_input > 3)):
            print("Invalid input, please try again")
        else:
            if(user_input == 1):
                print("Rock selected\n")
                return "rock"
            elif(user_input == 2):
                print("Paper selected\n")
                return "paper"
            else:
                print("Scissors selected\n")
                return "scissors"

# Randomly generate a number for our opponent
def cpu_choice():
    computer_number = random.randint(0, 2)

    # Assign a choice depending on the number
    if(computer_number == 0):
        return "rock"
    elif(computer_number == 1):
        return "paper"
    else:
        return "scissors"

def rock_paper_scissors():
    player_choice = choice()
    computer_choice = cpu_choice()

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

    return 0

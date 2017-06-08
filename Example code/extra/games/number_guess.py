import random

def clear_screen():
    for x in range(50):
        print("")

# Returns the ui for the difficulty selection menu
def difficulty_menu_ui():
    return '''
----------------------------------
Please select a difficulty

Enter a number to select an option
----------------------------------
1 - Easy
2 - Medium
3 - Hard
----------------------------------
'''

def difficulty():
    print(difficulty_menu_ui())

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
            clear_screen()
            if(user_input == 1):
                print("Easy selected\n")
                return 1
            elif(user_input == 2):
                print("Medium selected\n")
                return 2
            else:
                print("Hard selected\n")
                return 3

def guess_the_number():
    # Determine difficulty level
    difficulty_level = difficulty()
    # The player has 3 attempts to guess the correct number
    guess_attempts = 4

    # The volume of available numbers increases with difficulty
    if(difficulty_level == 1):
        random_number = random.randint(0, 20)
        limit = 20
    elif(difficulty_level == 2):
        random_number = random.randint(0, 50)
        limit = 50
    else:
        random_number = random.randint(0, 100)
        limit = 100

    while(guess_attempts > 0):
        # Ask the player to guess a number
        print("Guesses remaining: {}".format(guess_attempts))

        # Handle invalid input type
        try:
            player_guess = int(input("Please guess a number\n-> "))
        except:
            print("Invalid input, please try again")
            continue

        # Check if player guessed correctly
        if(not(0 <= player_guess <= limit)):
            print("That number is out of range, please try again")
            continue
        # Player guess correctly
        elif(player_guess == random_number):
            print("Well done, {} was the correct number!".format(random_number))
            print("You had {} guesses remaining.".format(guess_attempts))
            return 0
        else:
            clear_screen()

            if(abs(random_number - player_guess) <= 5):
                print("Hot\n")
            elif(5 < abs(random_number - player_guess) <= 15):
                print("Warm\n")
            elif(15 < abs(random_number - player_guess) <= 25):
                print("Cool\n")
            else:
                print("Cold\n")

        guess_attempts -= 1
        # print out previous guess for reference
        print("Previous guess: {}".format(player_guess))

    # The player runs out of guesses
    print("Unfortunately you ran out of guesses")
    print("The number was {}".format(random_number))

    return 0

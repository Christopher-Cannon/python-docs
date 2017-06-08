import sys
import number_guess
import rps

# Output the menu ui
def menu_ui():
    return '''
----------------------------------
What would you like to play?

Enter a number to select an option
----------------------------------
1 - Guess the Number
2 - Rock Paper Scissors
3 - Quit
----------------------------------
'''

# Display a menu of choices
def menu():
    print(menu_ui())

    while(True):
        # Handle invalid input type
        try:
            user_input = int(input("-> "))
        except:
            print("Invalid input, please try again")
            continue

        # If input is a string or is not 1-3 display error
        if((user_input < 1) or (user_input > 3)):
            print("Invalid input, please try again")
        else:
            if(user_input == 1):
                print("Guess the Number selected\n")
                return 1
            elif(user_input == 2):
                print("Rock Paper Scissors selected\n")
                return 2
            else:
                print("Quit selected\nExiting...")
                sys.exit()

# Main logic function
def main():
    while(True):
        game_choice = menu()

        # Play game depending on choice
        if(game_choice == 1):
            number_guess.guess_the_number()
        else:
            rps.rock_paper_scissors()

main()

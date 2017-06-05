import random

random_number = random.randint(1, 100)

player_choice = int(input("Choose a number between 1 and 100: "))

if(player_choice > 100) or (player_choice < 1):
    print("That number is out of range")
else:
    if(player_choice > random_number):
        difference = player_choice - random_number

        print("That number was too big.")
        print("Number was {}, {} off".format(random_number, difference))
    elif(player_choice < random_number):
        difference = random_number - player_choice

        print("That number was too small.")
        print("Number was {}, {} off".format(random_number, difference))
    else:
        print("You guessed right!")

user_input = ""

# Continue looping until user enters "quit"
while(user_input != "quit"):
    print("Options: a - b - quit")
    user_input = input(" -> ")

    if(user_input == "a"):
        print("a selected")
    elif(user_input == "b"):
        print("b selected")
    elif(user_input == "quit"):
        print("Quitting...")
        # Re-evaluate loop condition
        continue
    else:
        print("Invalid option")

    print("Other code here...")

# Move around a virtual grid using text commands

# Update movement list with new coords, removing one if the list
# is more than 7 elements in length
def update_list(lst, new_x, new_y):
    # List has less than 7 elements
    if(len(lst) < 7):
        lst.append([new_x, new_y])
    else:
        # Shift each element to the left before adding the new coords
        for x in range(len(lst) - 1):
            lst[x] = lst[x + 1]

        lst[-1] = [new_x, new_y]

    return lst

my_list = []
user_input, last_action = "", "up"
x, y = 0, 0

# Keep looping for input until user inputs 'quit'
while(user_input != "quit"):
    # Attempt to get input from the user
    try:
        user_input = str(input("-> "))
    except:
        continue

    # If 'quit' entered, go to next iteration and end script
    if(user_input == "quit"):
        continue
    elif((user_input != "up") and (user_input != "down") and (user_input != "left") and (user_input != "right")):
        # Default to previous action if input is not one of the directions
        user_input = last_action

    if(user_input == "up"):
        x += 1
        last_action = "up"
    elif(user_input == "down"):
        x -= 1
        last_action = "down"
    elif(user_input == "right"):
        y += 1
        last_action = "right"
    elif(user_input == "left"):
        y -= 1
        last_action = "left"
    else:
        pass

    # Update new coordinates according to input
    my_list = update_list(my_list, x, y)

    print(my_list)

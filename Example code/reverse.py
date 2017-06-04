# Define our string reversing function
def reverse_string(string):
    # Set position to 0, new string to a blank string
    position, new_string = 0, ""

    # While position does not exceed the length of the string
    while(position < len(string)):
        # Add the letter at the current position in the string to the
        # start of our new string
        new_string = string[position] + new_string

        # Add 1 to position, i.e. go to the next position in the string
        position += 1

    # Return our new string
    return new_string

# Print out the output of our functions
print(reverse_string("Hello"))
print(reverse_string("This is a longer string than the previous one."))

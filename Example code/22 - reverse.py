# Function to reverse a string

def reverse_string(string):
    position, new_string = 0, ""
    # While position does not exceed the length of the string
    while(position < len(string)):
        # Place current letter at start of new_string
        new_string = string[position] + new_string
        # Go to next letter
        position += 1

    return new_string

print(reverse_string("Hello"))
print(reverse_string("This is a longer string than the previous one."))

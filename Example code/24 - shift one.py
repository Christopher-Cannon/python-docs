# Attempt to match a letter to its position in the alphabet and return that number
def find_letter(letter, my_list):
    for x in range(len(my_list)):
        # Return alphabet position if match
        if(letter == my_list[x]):
            return x

    # If no match, return original character
    return letter

# Shift each letter in a string to the next letter in the alphabet
def shift_one(string):
    alphabet, new_string = "abcdefghijklmnopqrstuvwxyz", ""

    for x in range(len(string)):
        # Check if letter is in the alphabet
        char_pos = find_letter(string[x].lower(), alphabet)

        # Int returned, we have a letter to shift along
        if(isinstance(char_pos, str) == False):
            # If pos == 25 (z) then pos = 0 (a), else shift by 1
            if(char_pos == 25):
                char_pos = 0
            else:
                char_pos += 1

            # Insert char + 1 to new string
            new_string = new_string + alphabet[char_pos]
        # String returned, append char
        else:
            new_string += char_pos

    print("Original: {}\nShifted:  {}".format(string, new_string))

shift_one("Shift each letter along one.")

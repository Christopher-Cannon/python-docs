# Attempt to match a letter to its position in the alphabet and return that number
def find_letter(letter, my_list):
    position = 0

    # Go through the whole alphabet list
    while(position < len(my_list)):
        # If there is a match at that position
        if(letter == my_list[position]):
            # If there is a match, return position
            return position
        else:
            # Otherwise go to next position
            pass

        position += 1

    # If no match, return original character
    return letter

# Take each letter in a string and shift each along to the next letter in the alphabet
def shift_one(string):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    position, new_string = 0, ""

    # Iterate through each letter in the string
    while(position < len(string)):
        # Check if letter is in the alphabet
        char_pos = find_letter(string[position], alphabet)

        # If it is, char_pos will be an integer
        if(isinstance(char_pos, str) == False):
            # If position 25 (z) position = 0 (a)
            if(char_pos == 25):
                char_pos = 0
            # Increment position by 1
            else:
                char_pos += 1

            # Insert char + 1 to new string
            new_string = new_string + alphabet[char_pos]
        # Otherwise it is a string
        else:
            new_string += char_pos

        position += 1

    print("Original string: {}".format(string))
    print("Shifted string:  {}".format(new_string))

shift_one("shift each letter along one.")

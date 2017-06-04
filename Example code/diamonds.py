''' This function outputs a series of diamonds.

    It takes two arguments:
    loops - how many diamonds to create
    size - how big the diamonds should be
'''

def diamonds(loops, size):
    # These are the characters our diamond and spaces will be made up of
    char_block = "#"
    char_space = " "

    # Initialise the variables that will physically represent our
    # diamond and surrounding space
    text = ""
    space = ""

    # Fill space with 'size' number of chars
    while(len(space) < size):
        space = space + char_space

    # Print out first line of space chars for neatness
    print(space * 2)

    # While we haven't reached the max number of loops
    for x in range(loops):
        # If the remainder of count / 2 is equal to 0
        if(x % 2 == 0):
            # While the string length is less than our desired size
            # We divide the text length by 2 otherwise the diamond is too small
            while((len(text) / 2) < size):
                # Add two X's and surround it with spaces
                text = text + (char_block * 2)
                # Remove a space on either side as the shape grows
                space = space.replace(char_space, "", 1)
                print(space + text + space)
        else:
            # While there are characters in the string
            while((len(text) / 2) > 0):
                # Remove an X from text and print out the string
                text = text.replace(char_block, "", 2)
                # Add spaces on either side as the shape shrinks
                space = space + char_space
                print(space + text + space)

# Main execution function
def main():
    # Ask the user to define loop count and diamond size
    # We multiply loops by 2 because a diamond is made of
    # 2 triangles
    loops = int(input("How many diamonds to create? ")) * 2
    size = int(input("How big should the diamonds be? "))

    # Execute diamonds function
    diamonds(loops, size)

main()

# Output a series of diamonds in the console window

def diamonds(loops, size):
    # Diamond and spaces characters
    char_block, char_space = "#", " "

    # Represents the growing/shrinking diamond and padding
    text, space = "", ""

    # Fill space with 'size' number of chars
    while(len(space) < size):
        space += char_space

    # Print out empty line for neatness
    print('')

    for x in range(loops):
        # If the remainder of count / 2 is equal to 0
        if(x % 2 == 0):
            # While the string length is less than our desired size
            while((len(text) / 2) < size):
                # Add two X's and surround it with spaces
                text += char_block * 2
                # Remove a space as the shape grows
                space = space.replace(char_space, "", 1)
                print(space + text)
        else:
            # While there are characters in the string
            while((len(text) / 2) > 0):
                # Remove an X from text and print out the string
                text = text.replace(char_block, "", 2)
                # Add a space as the shape shrinks
                space += char_space
                print(space + text)

def main():
    # We multiply loops by 2 because a diamond is made of 2 triangles
    loops = int(input("How many diamonds to create? ")) * 2
    size = int(input("How big should the diamonds be? "))

    diamonds(loops, size)

main()

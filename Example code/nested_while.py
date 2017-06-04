''' This function outputs a series of triangles
    in a wave-like pattern.

    It takes two arguments:
    loops - how many triangles to create
    size - how big the triangles should be
'''

def triangles(loops, size):
    text = ""

    # For each loop
    for x in range(loops):
        # If the remainder of count / 2 is equal to 0
        if(x % 2 == 0):
            # While the string length is less than our desired size
            while(len(text) < size):
                # Add an X and print out the string
                text = text + "X"
                print(text)
        else:
            # While there are characters in the string
            while(len(text) > 0):
                # Remove an X from text and print out the string
                text = text.replace("X", "", 1)
                print(text)

# Main execution function
def main():
    # Ask user to define loop count and triangle size
    loops = int(input("How many triangles to create? "))
    size = int(input("How big should the triangles be? "))

    # Execute triangles function
    triangles(loops, size)

main()

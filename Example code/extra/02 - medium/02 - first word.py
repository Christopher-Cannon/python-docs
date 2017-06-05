# Find the first word in a string

string = "this is a string"
space = " "

for x in range(len(string)):
    # Stop iterating through string once a space is found
    if(string[x] == space):
        # Print string from the start to current position
        print(string[0:x])
        break

import random

# Generate a random list of a given length
def random_list(length):
    return_list = []

    for x in range(length):
        return_list.append(random.randint(0, 100))

    return return_list

# Use binary search to attempt to find a number in a list
def number_search(num, lst):
    # Print out the state of our list at the start
    print("\nList: {}".format(lst))

    while(int(len(lst)) > 0):
        # Get the number at the middle of our list
        middle_number = int(len(lst) / 2)

        # Print out the current middle number
        print("\nNumber at middle: {}".format(lst[middle_number]))

        # If the number halfway along matches, return success
        if(lst[middle_number] == num):
            return "found {}".format(num)
        # If middle number is greater than our number
        elif(lst[middle_number] > num):
            # Slice the old list from the first element to halfway
            lst = lst[0:middle_number]

            # Print out the current state of the list
            print("\nList: {}".format(lst))
        else:
            # Slice the old list from halfway to the last element
            lst = lst[middle_number:-1]

            # Print out the current state of the list
            print("\nList: {}".format(lst))

    # If the list ends up with no elements in it, the number is not in it
    return "Number is not in the list"

# Create a new randomised list and order it
list_to_search = sorted(random_list(50))

# Ask the user what number they want to search for, make sure it's an int value
number_to_find = int(input("What number do you want to find? -> "))

# Get result from number_search, giving it our number to find and list to search
result = number_search(number_to_find, list_to_search)

# Print out our number, and whether it was in the list or not
print("Number: {}".format(number_to_find))
print("Result: {}".format(result))

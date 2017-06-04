# A function that attempts to find a number in a randomly generated
# list using binary search

import random

# Generate a random list of a given length
def random_list(length):
    return_list = []

    for x in range(length):
        return_list.append(random.randint(0, 100))

    return return_list

# Use binary search to attempt to find a number in a list
def number_search(num, lst):
    # While there are still elements left in the list
    while(int(len(lst)) > 0):
        # If the number halfway along matches, return success
        if(lst[int(len(lst) / 2)] == num):
            return "Number exists in the list"
        # If number halfway is greater, cut off the second half
        elif(lst[int(len(lst) / 2)] > num):
            lst = lst[0:int(len(lst) / 2)]
        # Otherwise cut off the first half
        else:
            lst = lst[int(len(lst) / 2):-1]

    # Return failure if no match found
    return "Number is not in the list"

# Create a new randomised list and order it
list_to_search = sorted(random_list(50))

# Get number to search from user
number_to_find = int(input("What number do you want to find? -> "))

# Get result from number_search, giving it our number to find and list to search
result = number_search(number_to_find, list_to_search)

# Print out the list, our number, and whether it was in it or not
print("List: {}".format(list_to_search))
print("Number: {}".format(number_to_find))
print("Result: {}".format(result))

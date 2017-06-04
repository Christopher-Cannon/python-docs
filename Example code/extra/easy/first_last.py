# This function returns a list containing the first and last
# elements of a given list.

def return_ends(my_list):
    # Get the first and last element from the list
    first = my_list[0]
    last = my_list[-1]

    # Return a new list containing the above variables
    return [first, last]

old_list = [5, 2, 8, 64, 12, 99, 403, 56]

# Print out the returned list from return_ends()
print(return_ends(old_list))

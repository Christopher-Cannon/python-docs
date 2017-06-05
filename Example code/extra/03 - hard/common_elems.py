# A function that returns a list of the common elements found
# in two separate lists of any length

import random

# This is our random list function from before
def random_list(length):
    return_list = []

    for x in range(length):
        return_list.append(random.randint(0, 100))

    return return_list

# Return a list containing common elements of 2 variable length lists
def common_elems(list_one, list_two):
    # Create an empty list
    common_list = []

    # For each element in the first list
    for x in list_one:
        # For each element in the second list
        for y in list_two:
            # Append element to new list if elements match
            if(x == y):
                common_list.append(x)

    return common_list

# Create two randomised lists of different length
list_one = random_list(20)
list_two = random_list(15)

print("List one: {}".format(list_one))
print("List two: {}".format(list_two))

print("Common elements: {}".format(common_elems(list_one, list_two)))

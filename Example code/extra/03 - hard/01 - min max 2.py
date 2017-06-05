# A version of min_max.py that does not use the built-in min/max_no
# functions
import random

# This is our random list function from before
def random_list(length):
    return_list = []

    for x in range(length):
        return_list.append(random.randint(0, 100))

    return return_list

def return_min_max(my_list):
    maximum = 0

    # For each element in the given list
    for elem in my_list:
        # If element is bigger than max, max equals element
        if(elem > maximum):
            maximum = elem

    # Set min to max value
    minimum = maximum

    # Again, for each element in the given list
    for elem in my_list:
        # If element is smaller than min, min equals element
        if(elem < minimum):
            minimum = elem

    # Return a new list containing the min and max elements
    return [minimum, maximum]

rand_list = random_list(20)

print(rand_list)
print(return_min_max(rand_list))

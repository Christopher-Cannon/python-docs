# Generate a list of random integers then create a new list from it that
# contains only numbers cleanly divisible by 5

import random

# Generate a random list of a given length
def random_list(length):
    return_list = []

    for x in range(length):
        return_list.append(random.randint(0, 100))

    return return_list

def div_by_5(rand_list):
    new_list = []

    for elem in rand_list:
        if(elem % 5 == 0):
            new_list.append(elem)

    return new_list

print(div_by_5(random_list(100)))

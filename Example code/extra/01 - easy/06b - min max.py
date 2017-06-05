# A function that returns a list of the smallest and largest elements
# from a randomly generated list
import random

# Generate a random list of a given length
def random_list(length):
    return_list = []

    for x in range(length):
        return_list.append(random.randint(0, 100))

    return return_list

# Fine smallest and largest list elements
def return_min_max(my_list):
    maximum = max(my_list)
    minimum = min(my_list)

    return [minimum, maximum]

rand_list = random_list(20)

print(return_min_max(rand_list))

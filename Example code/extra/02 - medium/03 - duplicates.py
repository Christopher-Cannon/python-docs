# Generate a list of random integers then remove all duplicate numbers.
import random

# Create a list of random integers of a given length
def random_list(length):
    return_list = []

    for x in range(length):
        return_list.append(random.randint(0, 100))

    return return_list

# Return list as a set to remove duplicate entries
def remove_duplicates(lst):
    return set(lst)

list_one = random_list(50)

print(list_one)
print(remove_duplicates(list_one))

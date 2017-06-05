# A function that returns a list of random integers as long
# as a given length
import random

# Generate a random list of a given length
def random_list(length):
    # This will be our list to return
    return_list = []

    # For <length> number of times add a random integer between
    # 0 and 100 to our return list
    for x in range(length):
        return_list.append(random.randint(0, 100))

    return return_list

# Output several randomised lists
print(random_list(10))
print(random_list(20))
print(random_list(50))

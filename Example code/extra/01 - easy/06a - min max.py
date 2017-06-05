# A function that returns a list of the smallest and largest elements
# from a larger list of numbers

def return_min_max(my_list):
    # We can get the largest and smallest element from a list of numbers
    # using the built-in min() and max() functions
    maximum = max(my_list)
    minimum = min(my_list)

    # Return a new list containing the above variables
    return [minimum, maximum]

old_list = [5, 2, 8, 64, 12, 99, 403, 56]

print(return_min_max(old_list))

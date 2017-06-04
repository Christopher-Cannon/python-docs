def return_min_max(my_list):
    maximum = 0

    # Find maximum value
    for elem in my_list:
        # If element is bigger than max, max equals element
        if(elem > maximum):
            maximum = elem

    # Set min to max value
    minimum = maximum

    # Find minimum value
    for elem in my_list:
        # If element is smaller than min, min equals element
        if(elem < minimum):
            minimum = elem

    return [minimum, maximum]

old_list = [5, 2, 8, 64, 12, 99, 403, 56]

new_list = return_min_max(old_list)

print(new_list)

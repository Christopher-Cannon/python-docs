# A function that takes two numbers and prints out that
# the numbers are equal or that one is bigger than the other

def number_compare(num_one, num_two):
    # If the numbers are equal
    if(num_one == num_two):
        print("{} and {} are equal.".format(num_one, num_two))
    # If the first number is bigger than the second
    elif(num_one > num_two):
        print("{} is bigger than {}.".format(num_one, num_two))
    # If the second number is bigger than the first
    else:
        print("{} is bigger than {}.".format(num_two, num_one))

# Compare some numbers
number_compare(1, 8)
number_compare(16, 8)
number_compare(8, 8)

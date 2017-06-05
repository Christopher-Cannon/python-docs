# A function that takes a number and returns the sum of all numbers from
# 0 to a given number

def sum_of_range(max_no):
    # Our sum, which starts at 0
    total = 0

    # For each number from x to max_no, add it to total
    for x in range(max_no):
        total += x

    # Return our sum
    return total

# Test our function a few times
print("Sum of digits from 1 to 36: {}".format(sum_of_range(36)))
print("Sum of digits from 1 to 107: {}".format(sum_of_range(107)))

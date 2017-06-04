# A function that takes two strings and prints out that
# the strings are equal or that one is longer than the other

def string_compare(string_one, string_two):
    # Use len() to get the lengths of our strings as integer values
    len_one = len(string_one)
    len_two = len(string_two)

    # If both strings are the same length
    if(len_one == len_two):
        print("{} and {} are the same length.".format(string_one, string_two))
    # If string one is longer than string two
    elif(len_one > len_two):
        print("{} is longer than {}.".format(string_one, string_two))
    # If string two is longer than string one
    else:
        print("{} is longer than {}.".format(string_two, string_one))

# Compare some strings
string_compare("apple", "banana")
string_compare("apple", "lemon")
string_compare("pineapple", "banana")

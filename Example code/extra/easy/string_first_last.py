# This function attaches the last character in the string to
# the first and last position of the string.

def wrap_with_last(string):
    # Get the last character of our string
    last_char = string[-1]

    # Use concatenation to output our string in the intended manner
    print(last_char + string + last_char)

wrap_with_last("This is a string")

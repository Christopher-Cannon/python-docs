def reverse_string(string):
    position, reversed_string = 0, ""

    while(position < len(string)):
        reversed_string = string[position] + reversed_string
        position += 1

    return reversed_string

print(reverse_string("Hello"))
print(reverse_string("This is a longer string than the previous one."))

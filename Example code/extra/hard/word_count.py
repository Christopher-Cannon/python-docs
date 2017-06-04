def count_words(string):
    space, word_count, previous = " ", 0, " "

    # Inserting a space at the end allows the following loop to correctly
    # detect words
    string += space

    # If the current char is a space and the previous was an alphanumeric,
    # count it as a word
    for x in string:
        if((x == space) and (previous != space)):
            word_count += 1

        previous = x

    return word_count

my_string = "This is a simple sentence"

print("my_string: [{}]".format(my_string))
print("my_string has {} words in it.".format(count_words(my_string)))

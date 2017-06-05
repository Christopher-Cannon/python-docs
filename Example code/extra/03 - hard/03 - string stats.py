# Output various statistics about a piece of text

# Return the length of a split string
def word_count(string):
    return len(string.split())

# Find the average word length of a piece of text
def word_length(string):
    split_string, total_letters = string.split(), 0

    for x in split_string:
        total_letters += len(x)

    return total_letters / word_count(string)

my_string = "This is a simple sentence"

print("\nmy_string: [{}]".format(my_string))
print("words: {}\naverage word length: {}\n".format(word_count(my_string), word_length(my_string)))

# Output the number of words in a string and the average word length in letters

def word_split(string):
    return string.split()

def word_count(string):
    return len(word_split(string))

def word_length(string):
    total_letters = 0

    for x in split_string:
        total_letters += len(x)

    return total_letters / word_count(split_string)

my_string = "This is a simple sentence"

print("\nmy_string: [{}]".format(my_string))
print("words: {}\naverage word length: {}\n".format(word_count(my_string), word_length(split_string)))

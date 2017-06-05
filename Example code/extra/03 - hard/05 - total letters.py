# Count how many letters are in a string

def find_total_letters(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter_count = 0

    for str_char in string:
        for alpha_letter in alphabet:
            if(str_char == alpha_letter):
                letter_count += 1
            else:
                pass

    return letter_count

test_string = "This is a fairly long sentence that surely can't contain any punctuation"

print("test_string: {}".format(test_string))
print("Total letters in test_string: {}".format(find_total_letters(test_string)))

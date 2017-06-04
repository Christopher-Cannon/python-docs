def find_total_vowels(string):
    vowels = "aeiou"
    total = 0

    for letter in string:
        for x in vowels:
            if(letter == x):
                total += 1
            else:
                pass

    return total

test_string = "This is a fairly long sentence that surely can't contain any punctuation"

print("test_string: {}".format(test_string))
print("Total vowels in test_string: {}".format(find_total_vowels(test_string)))

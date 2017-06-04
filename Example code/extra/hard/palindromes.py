# Determine if a given string is a palindrome or not

import math

def palindromes(string):
    f_pos = 0
    l_pos = -1

    count = 0

    for x in range(math.floor(len(string) / 2)):
        if(string[f_pos] == string[l_pos]):
            count += 1
        else:
            pass

        f_pos += 1
        l_pos -= 1

    if(count == math.floor(len(string) / 2)):
        print("{} is a palindrome.".format(string))
    else:
        print("{} is not a palindrome.".format(string))

palindromes("racecar")
palindromes("hannah")
palindromes("warehouse")

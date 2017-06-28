# Determine if a given string is a palindrome or not

import math

def palindromes(string):
    f_pos, l_pos, count = 0, -1, 0

    # Compare all letters except the one in the middle
    for x in range(len(string) // 2):
        if(string[f_pos] == string[l_pos]):
            count += 1

        f_pos += 1
        l_pos -= 1

    if(count == len(string) // 2):
        print("{} is a palindrome.".format(string))
    else:
        print("{} is not a palindrome.".format(string))

palindromes("racecar")
palindromes("hannah")
palindromes("warehouse")

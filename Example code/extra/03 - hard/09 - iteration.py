# Don't go too high, 6-7 or higher may cause memory error
from itertools import product

def pass_combos(length):
    alpha, return_list = "abcdefghijklmnopqrstuvwxyz1234567890", []

    for x in range(length):
        combo_list = product(alpha, repeat = (x + 1))
        for y in combo_list:
            return_list.append(y)

    return return_list

def output_list(lst):
    for x in lst:
        out = ""
        for y in x:
            out += y

        print(out)

length = int(input("How many combinations to generate? -> "))
output_list(pass_combos(length))

from itertools import product

def pass_combos(length):
    alpha, nums = "abcdefghijklmnopqrstuvwxyz", "1234567890"

    for x in range(length):
        combo_list = product(alpha + alpha.upper() + nums, repeat = (x + 1))
        for y in combo_list:
            out = ''
            for z in y:
                out += z

            print(out)

length = int(input("How many combinations to generate? -> "))
pass_combos(length)

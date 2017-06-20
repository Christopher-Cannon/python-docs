# Simple recursion example
# Given a starting number and a limit,
# print out numbers till the limit is reached

def recurse(num, limit):
    if(num < limit):
        print(num)
        recurse(num + 1, limit)
    else:
        print("Reached limit")

recurse(2, 9)

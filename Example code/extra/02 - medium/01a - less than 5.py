# Find all numbers less than 5 in a list and return a new list
# containing those numbers

def less_than_5(lst):
    new_lst = []

    for elem in lst:
        if(elem < 5):
            new_lst.append(elem)
        else:
            pass

    return new_lst

my_list = [1, 7, 16, 3, 18, 2, 44, 6, 0, 9, 300, 2, 1, 23]

print(less_than_5(my_list))

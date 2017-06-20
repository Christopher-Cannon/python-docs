# Sort a list from smallest to largest value
# Count +1 every time we don't need to swap values
# If we can get through with swapping the list is sorted

def order_list(lst):
    while(True):
        count = 1
        for x in range(len(lst) - 1):
            if(lst[x] > lst[x + 1]):
                lst[x], lst[x + 1] = lst[x + 1], lst[x]
            else:
                count += 1

        if(count == len(lst)):
            return lst

my_list = [5, 1, 8, 4, 14, 88, 34, 9, 87]

print("Original list:\t{}".format(my_list))
print("Sorted list:\t{}".format(order_list(my_list)))

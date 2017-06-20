# Create a list containing every number from 0 to 9 to the power of 2
my_list = [x**2 for x in range(10)]

print(my_list)
# Print out every even number in the above list
for elem in my_list:
    if(elem % 2 == 0):
        print(elem)

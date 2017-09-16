'''
Correct the indentation in this example so that it runs correctly.

Once it runs without errors, add some comments to describe what each
print statement is doing.
'''

def number_compare(num_one, num_two):
if(num_one == num_two):
print("{} and {} are equal.".format(num_one, num_two))
elif(num_one > num_two):
print("{} is bigger than {}.".format(num_one, num_two))
else:
print("{} is bigger than {}.".format(num_two, num_one))

number_compare(1, 8)
number_compare(16, 8)
number_compare(8, 8)

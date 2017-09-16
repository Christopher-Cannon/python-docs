'''
Print out the sum of all numbers between 50 and 100.
'''

minimum = 50
maximum = 100
result = 0

# Write your solution here
for x in range(minimum, maximum):
    result += x

print("Sum: {}".format(result))

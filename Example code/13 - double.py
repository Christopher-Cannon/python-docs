my_num = 10

def double(number):
    return number * 2

print("Before doubling:", my_num)
my_num = double(my_num)
print("After doubling:", my_num)

num_two = double(double(double(25)))

print("Doubling a number multiple times:", num_two)

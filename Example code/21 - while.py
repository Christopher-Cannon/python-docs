text = ""

# While text is less than 10 characters long
while(len(text) < 10):
    text = text + "X"
    print(text)

my_list = []

# Do something an arbitrary number of times
for x in range(10):
    my_list.insert(0, x)
    print(my_list)

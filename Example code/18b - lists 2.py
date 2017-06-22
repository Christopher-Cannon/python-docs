# Create a new list
a_list = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
b_list = a_list[1:5] + [4, 9, 2, 6, 1]
print("b_list", b_list)
print("a_list[2]", a_list[2])

# Append a value at the end
a_list.append(3)

# Insert a value (9) at the given position (1)
a_list.insert(1, 9)

print("a_list", a_list)
# Remove and return the given (last by default) item in a list
b_list.pop()
b_list.pop(0)

# Delete the item at the given position
del a_list[3]

# Sort a list
b_list.sort()

# Reverse a list
b_list.reverse()

print("a_list", a_list)
print("b_list", b_list)

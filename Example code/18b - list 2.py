# Create a new list
a_list = [0, 1, 2, 3, 4, 5, 6]

# Append a value at the end
a_list.append(3)

# Insert a value (9) at the given position (1)
a_list.insert(1, 9)

print(a_list)
# Remove and return the given (last by default) item in a list
a_list.pop()
a_list.pop(0)

# Delete the item at the given position
del a_list[3]

# Sort a list
a_list.sort()

# Reverse a list
a_list.reverse()

print(a_list)

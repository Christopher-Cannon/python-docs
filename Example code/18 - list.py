days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

choice = int(input("Which day of the week? 1-7: "))

# We subtract one because arrays are zero-indexed
print("Day:", days[choice - 1])

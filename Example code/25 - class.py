# Define person class
class person:
    def __init__(self, first, last):
        self.first, self.last = first, last

    def return_full_name(self):
        return "{} {}".format(self.first, self.last)

# Get names from user
first_name = str(input("What is your first name? -> "))
last_name = str(input("What is your last name? -> "))

# Instantiate class
instance = person(first_name, last_name)

# Print full name of person instance
name = instance.return_full_name()

print(name)

# Global variable called my_var
my_var = 10

def print_number():
    # Local variable called my_var
    my_var = 5

    print("print_number():", my_var)

print_number()
print("global:", my_var)

# A function that determines whether a number is odd or even using
# the modulo operator. A try catch block handles invalid input.

def odd_even(num):
    try:
        # If number divides cleanly by 2, it is even
        if(num % 2 == 0):
            print("{} is an even number.".format(num))
        else:
            print("{} is an odd number.".format(num))
    # If input isn't a number, tell the user
    except:
        print("That input is invalid.")

odd_even(2)
odd_even(17)
odd_even("banana")

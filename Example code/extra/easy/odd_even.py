def odd_even(num):
    try:
        if(num % 2 == 0):
            print("{} is an even number.".format(num))
        else:
            print("{} is an odd number.".format(num))
    except:
        print("That input is invalid.")

odd_even(2)
odd_even(17)
odd_even("banana")

print("Enter a number between 0 - 50")
number = int(input(" -> "))

if(0 < number < 50):
    if(number > 25):
        print("{} greater than 25".format(number))

        if(number % 5 == 0):
            print("Divides cleanly by 5")
    elif(number < 20):
        print("{} less than 20".format(number))
    else:
        print("{} is between 20 and 25".format(number))

        if(number % 3 == 0):
            print("Divides cleanly by 3")
else:
    print("Sorry, that number is out of range")

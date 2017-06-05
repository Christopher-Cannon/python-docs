# Use our divisors function to determine if a number is a prime number

def divisors(num):
    divisors_list = []

    for x in range(1, num + 1):
        if(num % x == 0):
            divisors_list.append(x)
        else:
            pass

    return divisors_list

# If the number has only 2 divisors it is a prime number
def primality(num):
    num_list = divisors(num)

    if(len(num_list) > 2):
        return "{} is not a prime number\n".format(num)
    else:
        return "{} is a prime number\n".format(num)

user_input = int(input("\nWhich number to check? -> "))

print(primality(user_input))

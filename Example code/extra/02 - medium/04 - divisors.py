# Find all divisors of a particular number

def divisors(num):
    divisors_list = []
    # num + 1 because because we also want the divisors of the number we input
    for x in range(1, num + 1):
        # If our number divides cleanly into x, add it to list of divisors
        if(num % x == 0):
            divisors_list.append(x)
        else:
            pass

    return divisors_list

user_input = int(input("Which number to check? -> "))

print(divisors(user_input))

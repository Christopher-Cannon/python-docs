# Function to convert decimals to hexadecimal

def dec_to_hex(number):
    hexa = "0123456789ABCDEF"
    hex_num = ""

    while(number != 0):
        # Get the remainder
        remainder = number % 16
        # Determine hex digit from remainder
        hex_num = hexa[remainder] + hex_num
        # Get the next number
        number = number // 16
        print("Number: ", number)
        print("Remainder: ", remainder)

    return hex_num

to_convert = int(input("Input decimal number to convert to hex -> "))
print("Dec: {}, Hex: {}".format(to_convert, dec_to_hex(to_convert)))

# Function to convert decimals to hexadecimal

def dec_to_hex(num):
    hexa = "0123456789ABCDEF"
    hex_num = ""

    while(num != 0):
        # Determine hex digit from remainder
        hex_num = hexa[num % 16] + hex_num
        # Get the next number
        num = num // 16

    return hex_num

to_convert = int(input("Input decimal number to convert to hex -> "))
print("Dec: {}, Hex: {}".format(to_convert, dec_to_hex(to_convert)))

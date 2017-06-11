# Recursive version of the previous example

def dec_to_hex(num, hex_num):
    hexa = "0123456789ABCDEF"

    hex_num = hexa[num % 16] + hex_num
    num = num // 16

    if(num == 0):
        return hex_num
    # Pass hex_num back up the call chain
    return dec_to_hex(num, hex_num)

to_convert = int(input("Input decimal number to convert to hex -> "))
print("Dec: {}, Hex: {}".format(to_convert, dec_to_hex(to_convert, "")))

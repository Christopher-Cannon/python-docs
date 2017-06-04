def c_to_f(centigrade):
    calculation = int((centigrade * (9 / 5)) + 32)

    return calculation

def f_to_c(fahrenheit):
    calculation = int((fahrenheit - 32) * (5 / 9))

    return calculation

temp_f = 50
temp_c = 30

print("{}F = {}C".format(temp_f, f_to_c(temp_f)))
print("{}C = {}F".format(temp_c, c_to_f(temp_c)))

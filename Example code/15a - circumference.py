pi = 3.14159

radius_one = 46
radius_two = 12
radius_three = 308
radius_four = 88
radius_five = 299

circ_one =  int(2 * pi * radius_one)
area_one =  int(pi * (radius_one ** 2))

circ_two =  int(2 * pi * radius_two)
area_two =  int(pi * (radius_two ** 2))

circ_three =  int(2 * pi * radius_three)
area_three =  int(pi * (radius_three ** 2))

circ_four =  int(2 * pi * radius_four)
area_four =  int(pi * (radius_four ** 2))

circ_five =  int(2 * pi * radius_five)
area_five =  int(pi * (radius_five ** 2))

result_one = "Circumference: {}\nArea: {}".format(circ_one, area_one)
result_two = "Circumference: {}\nArea: {}".format(circ_two, area_two)
result_three = "Circumference: {}\nArea: {}".format(circ_three, area_three)
result_four = "Circumference: {}\nArea: {}".format(circ_four, area_four)
result_five = "Circumference: {}\nArea: {}".format(circ_five, area_five)

print("\nCircle radius: {}\n{}".format(radius_one, result_one))
print("\nCircle radius: {}\n{}".format(radius_two, result_two))
print("\nCircle radius: {}\n{}".format(radius_three, result_three))
print("\nCircle radius: {}\n{}".format(radius_four, result_four))
print("\nCircle radius: {}\n{}".format(radius_five, result_five))

pi = 3.14159

def circumference(radius):
    global pi
    return int(2 * pi * radius)

def circle_area(radius):
    global pi
    return int(pi * (radius ** 2))

def print_circle_info(radius):
    result = "Circumference: {}\nArea: {}".format(circumference(radius), (circle_area(radius)))

    print("\nCircle radius: {}\n{}".format(radius, result))

print_circle_info(46)
print_circle_info(12)
print_circle_info(308)
print_circle_info(88)
print_circle_info(299)

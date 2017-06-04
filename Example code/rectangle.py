def rectangle_area(width, height):
    return width * height

def rectangle_perimeter(width, height):
    return (width * 2) + (height * 2)

width = int(input("Width of rectangle?: "))
height = int(input("Height of rectangle?: "))

area = rectangle_area(width, height)
perimeter = rectangle_perimeter(width, height)

print("Your rectangle is {} by {}".format(width, height))
print("Area: {}\nPerimeter: {}".format(area, perimeter))

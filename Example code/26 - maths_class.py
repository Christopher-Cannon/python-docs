class maths:
    def __init__(self):
        self.pi = 3.14159

    def add(self, num_a, num_b):
        return num_a + num_b

    def r_area(self, width, height):
        return width * height

    def r_perimeter(self, width, height):
        return (width * 2) + (height * 2)

    def circ(self, radius):
        return int(2 * self.pi * radius)

    def circle_area(self, radius):
        return int(self.pi * (radius ** 2))

    def is_even(self, number):
        if(number % 2 == 0):
            return True
        else:
            return False

m = maths()

print("18 + 83 = {}".format(m.add(18, 83)))

print("Area of 16x43 rectangle: {}".format(m.r_area(16, 43)))

print("Area of circle with radius 210: {}".format(m.circle_area(210)))

for x in range(20):
    if(m.is_even(x)):
        print(x)

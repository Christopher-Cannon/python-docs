class vehicle:
    def __init__(self, make, model, colour):
        self.make = make
        self.model = model
        self.colour = colour

    def print_info(self):
        print("\nVehicle:\t{} {} in {}".format(self.make, self.model, self.colour))

    def modify_colour(self, new_colour):
        self.colour = new_colour

class car(vehicle):
    def __init__(self, make, model, colour, car_type, top_speed, accel):
        vehicle.__init__(self, make, model, colour)
        self.car_type = car_type
        self.top_speed = top_speed
        self.accel = accel

    def print_info(self):
        vehicle.print_info(self)
        print("Type:\t\t{}\nTop speed:\t{}km".format(self.car_type, self.top_speed))
        print("Accel:\t\t0-100kmh in {} seconds".format(self.accel))

class aeroplane(vehicle):
    def __init__(self, make, model, colour, plane_type, top_speed, max_range):
        vehicle.__init__(self, make, model, colour)
        self.plane_type = plane_type
        self.top_speed = top_speed
        self.max_range = max_range

    def print_info(self):
        vehicle.print_info(self)
        print("Type:\t\t{}\nTop speed:\t{}km".format(self.plane_type, self.top_speed))
        print("Max range:\t{}km".format(self.max_range))

class jet_fighter(aeroplane):
    def __init__(self, make, model, colour, top_speed, max_range, ammo, hardpoints):
        aeroplane.__init__(self, make, model, colour, "Jet fighter", top_speed, max_range)
        self.ammo = ammo
        self.hardpoints = hardpoints

    def print_info(self):
        aeroplane.print_info(self)
        print("Ammo:\t\t{}\nHardpoints:\t{}".format(self.ammo, self.hardpoints))

red_car = car("Nissan", "GT-R", "red", "Sports car", 311, 2.7)
white_plane = aeroplane("Boeing", "777", "white", "Airliner", 945, 15844)
grey_fighter = jet_fighter("Eurofighter", "Typhoon", "grey", 2495, 2900, 150, 13)

red_car.print_info()
white_plane.print_info()
grey_fighter.print_info()

red_car.modify_colour("blue")
red_car.print_info()

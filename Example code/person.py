class person:
    def __init__(self, f_name, l_name, gender, height, weight):
        self.f_name = f_name
        self.l_name = l_name
        self.gender = gender
        self.height = height
        self.weight = weight
        self.species = "Human"

    def display_info(self):
        print("\nName: {} {}\nGender: {}".format(self.f_name, self.l_name, self.gender))
        print("Height: {}cm\nWeight: {}kg".format(self.height, self.weight))
        print("Species: {}".format(self.species))

    def modify_weight(self, value):
        self.weight += value

david = person("David", "Stephenson", "Male", 180, 80)
nick = person("Nick", "Wood", "Male", 177, 66)

david.display_info()

david.modify_weight(-10)

david.display_info()

print("\n{} {}".format(nick.f_name, nick.l_name))

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

class student(person):
    def __init__(self, f_name, l_name, gender, height, weight, school, subject):
        person.__init__(self, f_name, l_name, gender, height, weight)
        self.school = school
        self.subject = subject

    def student_info(self):
        person.display_info(self)
        print("School: {}\nSubject: {}".format(self.school, self.subject))

    def modify_subject(self, new_subject):
        self.subject = new_subject

mary = student("Mary", "Hill", "Female", 157, 61, "University of St. Andrews", "Social Sciences")

mary.student_info()

mary.modify_subject("Liberal Arts")
mary.modify_weight(5)

mary.student_info()

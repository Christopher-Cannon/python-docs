# Define person class
class person:
    def __init__(self, first, last):
        self.first, self.last = first, last

    def return_full_name(self):
        return "{} {}".format(self.first, self.last)

# Employee class extends person class
class employee(person):
    def __init__(self, first, last, employee_number, job_title):
        person.__init__(self, first, last)
        self.employee_number, self.job_title = employee_number, job_title

    def return_employee_number(self):
        return self.employee_number

    def return_job_title(self):
        return self.job_title

# Get names from user
first_name = str(input("What is your first name? -> "))
last_name = str(input("What is your last name? -> "))

# Instantiate class
emp = employee(first_name, last_name, "000984", "Store manager")

# Print employee details
name = emp.return_full_name()
emp_no = emp.return_employee_number()
job_title = emp.return_job_title()

print("Name:", name)
print("Employee number:", emp_no)
print("Job title:", job_title)

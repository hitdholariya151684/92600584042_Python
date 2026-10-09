class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name

    # Instance method
    def display(self):
        print("Student Name:", self.name)

    # Class method
    @classmethod
    def show_school(cls):
        print("School Name:", cls.school)

    # Static method
    @staticmethod
    def message():
        print("Welcome to Python Programming")


# Creating an object
s = Student("Rahul")

# Calling methods
s.display()
Student.show_school()
Student.message()

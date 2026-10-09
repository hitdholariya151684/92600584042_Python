#3.Write a program to illustrate instance variables and class variables.

class Student:
    # Class variable
    university = "marwadi university"

    def __init__(self, name):
        # Instance variable
        self.name = name


# Creating objects
s1 = Student("Rahul")
s2 = Student("Priya")
print("university:", Student.university)

print("Student 1:", s1.name)
print("Student 2:", s2.name)



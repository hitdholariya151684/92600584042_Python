#2.Write a program to demonstrate constructor and destructor usage.

class Student:
    # Constructor
    def __init__(self):
        print("Constructor is called.")


    # Destructor
    def __del__(self):
        print("Destructor is called.")
       
# Creating an object
s1 = Student()

# Deleting the object
del s1

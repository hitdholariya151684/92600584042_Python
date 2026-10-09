# Single Inheritance
class A:
    def show(self):
        print("Class A")

class B(A):
    def display(self):
        print("Class B")


# Multilevel Inheritance
class C(B):
    def message(self):
        print("Class C")


# Multiple Inheritance
class X:
    def method1(self):
        print("Class X")

class Y:
    def method2(self):
        print("Class Y")

class Z(X, Y):
    def method3(self):
        print("Class Z")


print("Single Inheritance:")
b = B()
b.show()
b.display()

print("\nMultilevel Inheritance:")
c = C()
c.show()
c.display()
c.message()

print("\nMultiple Inheritance:")
z = Z()
z.method1()
z.method2()
z.method3()

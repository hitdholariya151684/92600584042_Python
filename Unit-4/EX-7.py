class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    pass

class D(B, C):
    def __str__(self):
        return "Class D"

obj = D()
obj.show()
print(obj)
print(D.mro())

#Diamond Shape problem
#Scenario let B & C class inherit from A, D class inherit from B & C


class A:
    def met(self):
        print ("This is a method of class A")


class B(A):
    pass
    def met(self):
        print("This is a method of class B")


class C(A):
    pass
    def met(self):
        print("This is a method of class C")


class D(C,B):
    pass
    # def met(self):
    #     print("This is a method of class D")


a=A()
b=B()
c=C()
d=D()

d.met()
# print()
#Overriding Concept

class A:
    classvar1= "I am a class variable in class A"
    def __init__(self):
        self.var1="I am inside class A's constructor"
        self.classvar1="I am instance variable of class A"
        self.special="Special"


class B(A):
    classvar2="I am in class B"
    classvar1="I am variable of class B"

    def __init__(self):


        # super().__init__()
        # self.var1="Hello World"
        self.classvar1="I am instance variable of class B"
        super().__init__()
        # print(super().classvar1)
        pass

a=A()
b=B()
print(b.classvar1)
# print (b.special,b.classvar1)
# print(b.special)
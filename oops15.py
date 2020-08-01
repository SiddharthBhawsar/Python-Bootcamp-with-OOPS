#Operator overloading and Dunder method(those method which have trailing and heading of two underscore like __init__)

class Employee:
    no_of_leaves=8
    #self is the instance in which this function is applied if it i

    def __init__(self, aname, asalary, arole):
        self.name=aname
        self.salary=asalary
        self.role=arole
    def printdetails(self):
        return (f"Name is {self.name}. Salary is {self.salary}. Role is {self.role}")

    # Class method decorator used for changing the class variables
    @classmethod
    def change_no_of_leaves(cls, newleaves):
        cls.no_of_leaves=newleaves


# __add__ is a dunder methd & it helps in operator overloading
# And for remaining see it in google Mapping operators to functions
    def __add__(self, other):
        return  self.salary + other.salary
#
    def __truediv__(self, other):
        return self.salary / other.salary
# #
# # #To represent your object in proper way we use __repr__ and __int__  dunder method
# # #But __str__ has more priority than __repr__
# #
    def __repr__(self):
        return (f"Employee ( '{self.name}')  {self.salary} ('{self.role}')")

    def __str__(self):
        return (f"Name is {self.name}. Salary is {self.salary}. Role is {self.role}")


emp1=Employee("Nitesh", 250, "Teacher")
emp2=Employee("Rohan", 125, "Cleaner")




print(emp1 + emp2)
print(emp1 / emp2)


print(repr(emp1))
print(str(emp1))
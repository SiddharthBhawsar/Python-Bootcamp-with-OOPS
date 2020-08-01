#Code for alternative Constructor, if we pass vbariables to some other

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

    # Class method decorator used as a alternative constructor to get variable from oblect in other form than constructor
    @classmethod
    def from_str(cls, str):
        x=str.split("-")
        return cls(x[0],x[1],x[2])
        # return cls(*str.split("-") )


harry= Employee("Harry",455,"Instructor")
rohan=Employee("Rohan",777,"Student")
karan=Employee.from_str("Karan-333-Doctor")
# karan=Employee("Karan-333-Doctor")

print(karan.printdetails())



# #It can be accesable by object also
# rohan.change_no_of_leaves(34)
# print(rohan.no_of_leaves)
#
# #It can be accesable by class also
# Employee.change_no_of_leaves(34)
# print(Employee.no_of_leaves)
#
# #It also change for harry as class method change the class variables
# print(harry.no_of_leaves)
#
# # print(harry.printdetails())
# # print(rohan.printdetails())
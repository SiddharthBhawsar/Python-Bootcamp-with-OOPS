#Public, Protected and Private access Specifiers

class Employee:
    no_of_leaves=8
    _protect=9
    __private=98

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

    # Class method decorator used as a alternative constructor to get variable from
    # oblect in other form than constructor
    @classmethod
    def from_str(cls, str):
        # params=str.split("-")
        # return cls(params[0],params[1],params[2])
        return cls(*str.split("-") )



emp=Employee("Harry", 343, "Programmer")
print(emp._protect)
# print(emp.__private)
# print(Employee.__private)
print(emp._Employee__private)
#its not a private but it is name mangling
# print(emp._Employee__private)
# print(emp.__private)

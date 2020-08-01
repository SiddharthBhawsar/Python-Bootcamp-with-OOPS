#Static method means i dont required instance variables or
# class variables

#Code for alternative Constructor,
# if we pass vbariables to some other

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
    def dash_str(cls, str):
        params=str.split("^")
        return cls(params[0],params[1],params[2])
        #  return cls(*str.split("^") )

    @staticmethod
    def printgood(string):
        return ("This is good " + string)




harry= Employee("Harry",455,"Instructor")
rohan=Employee("Rohan",777,"Student")
karan=Employee.dash_str("Karan^333^Doctor")
# print(karan.printdetails())

print(karan.printgood("hello"))


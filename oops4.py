#self and __init__ constructor
#method ie __init__ to which class gets an argument
# is known as constructors

class Employee:
    no_of_leaves=8
    #self is the instance in which this function is applied if it is applied for harry than self = harry


#constructor used to pass variables from object to class
    def __init__(self, aname, asalary, arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    def printdetails(self):
        return f" Name is {self.name}. Salary is {self.salary}. Role is {self.role}"

harry= Employee("Harry",455,"Instructor")
rohan=Employee("Rohan",777,"Student")

# harry.name="Harry"
# harry.salary=455
# harry.role="Instructor"

#
# rohan.name="Rohan"
# rohan.salary=777
# rohan.role="Student"


#Below rohan is self only
print(harry.printdetails())
print(rohan.printdetails())
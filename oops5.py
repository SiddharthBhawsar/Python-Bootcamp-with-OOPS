#Code for ClassMethod decorator if i does want to
# use self for purpose of latency or if
# I want to change the value of class variable for object
# instance Class method is able to access class variables
#It can be also used as alternative constructor in next program


class Employee:
    no_of_leaves=8
    #self is the instance in which this function is applied if it i
    def printdetails(self):
        return (f"Name is {self.name}. Salary is {self.salary}. Role is {self.role}")


    @classmethod
    def change_no_of_leaves(cls, newleaves):
        cls.no_of_leaves=newleaves

harry=Employee()
rohan=Employee()

harry.name="Harry"
harry.salary=455
harry.role="Instructor"


rohan.name="Rohan"
rohan.salary=777
rohan.role="Student"

#It can be accesable by object also
harry.change_no_of_leaves(34)
print(harry.no_of_leaves)

#It can be accesable by class also
# Employee.change_no_of_leaves(34)
print(Employee.no_of_leaves)
#
# #It also change for rohan as class method change the class variables
# print(rohan.no_of_leaves)


# print(harry.printdetails())
# print(rohan.printdetails())
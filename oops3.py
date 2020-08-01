#Class Method and concept of init

class Employee:
    no_of_leaves=8
    #self is the instance in which this function is applied if it is
    # def printdetails(self):
    def printdetails(self):
        return (f"Name is {self.name}. Salary is {self.salary}. Role is {self.role}")

harry=Employee()
rohan=Employee()

harry.name="Harry"
harry.salary=455
harry.role="Instructor"


rohan.name="Rohan"
rohan.salary=777
rohan.role="Student"

print(harry.printdetails())
print(rohan.printdetails())
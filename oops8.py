#Single InHeritance

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
        # params=str.split("-")
        # return cls(params[0],params[1],params[2])
        return cls(*str.split("-") )

    @staticmethod
    def printgood(string):
        print("This is good " + string)

class Programmer(Employee):
    def __init__(self,  aname, asalary, arole, alanguage):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.language=alanguage
    def printprog(self):
        return (f"Name is {self.name}. Salary is {self.salary}. Role is {self.role}. Language is {self.language}")


shubam=Programmer("Shubam", 676, "Programmaer",["python"])
nitesh=Programmer("Nitesh", 555, "Programmaer",["Python"])


print(nitesh.printprog())
print(nitesh.printdetails())

print(nitesh.no_of_leaves)
#Multiple Inheritance

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


class Player:
    def __init__(self, name, game):
        self.name=name
        self.game=game

    def printdetails(self):
        return (f"Name is {self.name}. ")


class Music:
    def __init__(self, instrument):
        self.instrument= instrument
    pass
    # def printdetails(self):
    #     return (f"Instrument is {self.instrument}")
class CoolProgrammer(  Music, Player, Employee):

    pass
harry=Employee("Harry", 676, "Instructor")
rohan=Employee("Rohan", 555, "Student")


shubam=Player("Shubam", ["Cricket"])

nitesh=CoolProgrammer("nitesh", "test")
print(nitesh.printdetails())



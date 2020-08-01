#Abstract class used to force child class to
#make method which it have
#You can't create object of abstract base class

from abc import (ABC, abstractmethod)

class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0


class Rectangle(Shape):

    def __init__(self):
        self.length=6
        self.breadth=7
        # print(self.length*self.breadth)

#
    def printarea(self):
        return self.length * self.breadth

#
a=Rectangle()
print(a.printarea())


# b=Shape()
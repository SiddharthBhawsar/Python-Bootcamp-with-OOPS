#Object introspection is basically to know type of  the object

class Employee:
    def __init__(self, fname, lname):
        self.fname=fname
        self.lname=lname
        # self.email=f"{fname}.{lname}@gmail1.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"



#This property decorator is used if you want to access method as a attribute in order to full fill the concept of encapsulation
    # @property
    # def email(self):
    #     if self.fname==None or self.lname==None:
    #         print ("Email is not set Yet.....")
    #     return f"{self.fname}.{self.lname}@gmail1.com"


#I want to give input to email so accordingly it changes the first and last name of email for this we use setter
    # @email.setter
    # def email(self,string):
    #     print("Setting now..........")
    #     names=string.split("@")[0]
    #     self.fname=names.split(".")[0]
    #     self.lname = names.split(".")[1]
    #
    # @email.deleter
    # def email(self):
    #     self.fname=None
    #     self.lname=None

# skillf=Employee("Skill", "F")
# print(skillf.email)
# #
# print(type(skillf))
# print((type("This is a string")))
# print((id("This is a string")))
# print((id("This is a new string")))
# #
# o="This is a string"
# print(dir(o))
#
# #
# import inspect
# print(inspect.getmembers(skillf))

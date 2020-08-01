#Setter & Getter Decorator Property


class Employee:
    def __init__(self, fname, lname):
        self.fname=fname
        self.lname=lname
        # self.email=f"{fname}.{lname}@gmail1.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"



# #This property decorator is used if you want to access method
    # as a attribute/variables in order to full fill the concept of
    # encapsulation
    @property
    def email(self):
        if self.fname==None or self.lname==None:
            print ("Email is not set Yet.....")
        return f"{self.fname}.{self.lname}@gmail1.com"
#
# #
# # #I want to give input to email so accordingly it changes the first and last name of email for this we use setter
    @email.setter
    def email(self,string):
        print("Setting now..........")
        names=string.split("@")[0]
        self.fname=names.split(".")[0]
        self.lname = names.split(".")[1]
# # #
    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None
#
hindustani_supporter=Employee("Hindustani", "Supporter")
#
print(hindustani_supporter.explain())
# #
# print(hindustani_supporter.email())
print(hindustani_supporter.email)
#
# #It does not chage the output because at run time it sets the value
# #of constructor as Hindustani Supporter so to deal with this we
# #required another decorator and ie setter
hindustani_supporter.fname="US"
# # #
print(hindustani_supporter.email)
# # print(hindustani_supporter.email)
# #
# #
# # #in order to set this attribute we use setter
hindustani_supporter.email="Hello.World@gmail.com"
print(hindustani_supporter.email)
# # #
# #
del hindustani_supporter.email
print(hindustani_supporter.email)

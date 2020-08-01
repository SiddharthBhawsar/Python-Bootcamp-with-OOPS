class Employee:
    def __init__(self, fname, lname):
        self.fname=fname
        self.lname=lname
        # self.email=(f"{self.fname}.{self.lname}@gmail.com")


    @property
    def email(self):
        if self.fname==None or self.lname==None:
            print ("Email is not set Yet.....")
        return (f"{self.fname}.{self.lname}@gmail.com")

    @email.setter
    def email(self, string):
        print("Setting now..........")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
            self.fname = None
            self.lname = None


maac_animation=Employee("maac", "animation")



maac_animation.fname="maaya"
print(maac_animation.email)

maac_animation.email="arena.animation@gmail.com"
print(maac_animation.email)

del maac_animation.email
print(maac_animation.email)
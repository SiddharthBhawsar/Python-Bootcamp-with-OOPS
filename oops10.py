#Multi Level Inheritance

class Dad:
    basketball=1
    dance = 2

    # basketball = 8
    def isdance(self):
        return f"dance no is{self.dance}"


class Son(Dad):
    pass
    dance=1
    basketball = 8
    def isdance(self):
        return f"dance no is{self.dance}"

class Grandson(Son):
    pass

    dance=7
    # def isdance(self):
    #     return f"dance no is{self.dance}"


darry=Dad()
larry=Son()
harry=Grandson()

print(harry.isdance())
# print(harry.basketball)
#How to create Class, Object and Instance Variable


#Class Creation
class Student:
    pass


#Object Creation
harry=Student()
larry=Student()
#
print(harry,larry)



# Instance Variable Creation
harry.name="Harry"
harry.std=12
harry.section=1

print(harry.name)
print(harry.std)
print(harry.section)
#
larry.subject=["Physics", "Chemistry"]
print(harry.section, larry.subject)
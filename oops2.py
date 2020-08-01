#Difference Between Instance Variables and Class Variables
# & it also give the concept that class variables would not change
# by instance variables it only accessed by it

class Employee:
#Class Variables which is for both ie for harry and Rohan
    no_of_leaves=8
    # pass

harry=Employee()
rohan=Employee()


#Below is the property of Harry and Rohan itself it does not occupied it from class and this are instance variable
harry.name="Harry"
harry.salary=455
harry.role="Instructor"


rohan.name="Rohan"
rohan.salary=777
rohan.role="Student"

# print(harry.no_of_leaves)
# print(rohan.no_of_leaves)


#If we change rohan number of leaves it would not change the employee number of list

rohan.no_of_leaves=9
print(rohan.no_of_leaves)
# #
print(harry.no_of_leaves)
# # #
# #
print(Employee.no_of_leaves)
# #
#If i use dict attribute for rohan then it gives it returns ditionary which shows what instance variables have this object
print(rohan.__dict__)
print(Employee.__dict__)
# #
# # #but for emplyee it would remains same as it is in class variablesS returns ditionary which shows what  variables are for class
# # prin



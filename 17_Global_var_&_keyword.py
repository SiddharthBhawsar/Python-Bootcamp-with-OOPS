# #
# l=10 #Global Variables
# def function1(n):
#     print(n, "I have already Printed")
# # #     # local variable only defined under this function
# # #
#     global m
#     m=8
#     global l #Global keyword is used to change the global variable from local scope
#     l = 5
#     print(l , m)
# # # # #
# function1("This is me")
# print(l)
# print(m)


x=0
def func():
    x=20
    def rohan():
        global x
        x=98



    print("before calling rohan", x)
    rohan()
    print("After calling rohan", x)# It would not change the value of X because it searches in the main function while not in any function

func()
print(x)
#Decorators-Which modifies the functionality of a function
# def function1():
#     print("Subscribe Now")
# #
# func2=function1 #Here function1 is assigned to func2
# del function1 #Is func2 prints or not
# func2()
# function1()


# Code under is to return a function from a function
# def funcret(num):
#     if num==1:
#         return print
#
#     if num==0:
#         return sum
#
# a=funcret(0)
# b=[1,2,3]
# # print(sum(b))
# print(a(b))

# a(int(2,3))
# sum(int(5))


#Below code is to pass function as an argument
# def executor(func):
#     func("This")
#
# executor(print)


#Decorators
def dec1(func1):
    def nowexec():
        print("Executing Now")
        func1()
        print("Executed")
        # return "Hello"
    return nowexec

@dec1
def who_are_you():
    print("We are Engineers")
    # return "Hello"
# # #
# who_are_you=dec1(who_are_you)
who_are_you=dec1(who_are_you)
#
print(who_are_you())

# a=9
# b=8
#
# # #Built in Function
# # c=sum((a,b))
# # print(c)
# #
# # #User Defined Function
def function1():
    print("You are in function1")
    return "Hello"
print(function1())
# function1()
def function2(a,b):
    """This is a Function used to calculate
    average of two values"""
    average=(a+b)/2
    # print(average)
    return average

# print(average)
# #
average=function2(6,8)
print(average)
# print(average)
# print(v)
# #
# # #Docstring very important when in a file there are many functions
# # print(function2.__doc__)
print(function2.__doc__)
# #
# #

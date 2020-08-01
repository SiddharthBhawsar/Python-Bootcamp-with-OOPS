#Recursion- To use Function inside Function

# def print2(str1):
#     print2(str1)
#     #print("This is " + str1)
#
# print2("Python")


#n! = n*n-1*n-2*n-3.....1
#n! = n*(n-1)!
def factorial_itrative(n):
#     """
#     :param n: Integer
#     :return: n*n-1*n-2*n-3.....1
#     """
    fac=1
    for i in range(n):
        fac=fac * (i+1)
    return fac
#
#
# # #
# #
# #
# #
#
def factorial_recursive(n):
    if n==1 or n==0:
        return 1

    else:        return n*factorial_recursive(n-1)
    # print(a)
number=int(input("Enter the number"))
print("Factorial using iterative method", factorial_itrative(number))
print("Factorial using recursive method", factorial_recursive(number))

# print(a)



#Fibonacci sequence
#0 1 1 2 3 5 8 13 ....

def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
number=int(input("Enter number you want to calculate fibonacci series"))
print("Fibonacci series of number is: ", fibonacci(number))

# num1=int(input())
num1=input("Number 1")
print("Number 2")
# num2=int(input())
num2=input()
# print(f"Sum of numbers {num1} and {num2} is {int(num1) + int(num2)}")

# This type of scenario is valuable in case of internet
try:
    # print("The sum of this two number is ", num1 + num2)
    print("The sum of this two number is ", int(num1) + int(num2))
# # #
except Exception as e:
    print(e)
#
print("This Line is very Important")

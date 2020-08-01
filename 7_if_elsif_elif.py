var1=6
var2=56
#z
var3=int(input())
if var3 > var2:
    print("Greater")
#

if var3 != var2:
    pass



# if var3 > var2:
#     print("Greater")
#
elif var3==var2:
    print ("Equal")
# #
else:
#
 print("Lesser")

list1=[5,7,3]
if 5 in list1:
    print("Yes its in the list")
#
if 15 not in list1:
    print("No its not in the list")
#
#Short Hand if else Operator
a= int(input("enter a\n"))
b= int(input("enter b\n"))

# if a>b:
#     print("A is greater than B")
#
print("A is greater than B") if a>b else print("A is Less than B")
#

# #File IO Basics
#
# """
# "r" - Open File in Read Mode
# "w" - Open File in Write Mode
# "x" - Creates File if not exist
# "a" - Add more content of file/append
# "t" - Text mode
# "b" - Binary Mode
# "+" - Read and Write both
# """
#
#
# #Here open function returns a file pointer and
# # in our case it gets stores in f
# f=open("piemr")
# content=f.read()
# print(content)
# #
# f.close()
#
# #r is default mode and t(text file) is default type
# f=open("piemr", "rt")
# content=f.read()
# print(content)
# #
# f.close()
# #
# f=open("piemr", "rt")
# content=f.read(3)
# print(content)
#
# #
# content=f.read(3)
# print(content)
# #
# f.close()
#
#
#
# #If you want to read line line by line than you may itrerate the lines
# f=open("piemr", "rt")
# content=f.read()
# # #
# for char in content:
#     print(char, end=" ")
# #
# f.close()
#
#
# # f=open("piemr", "rt")
# # # content=f.read()
# #
# # for line in content:
# #     print(line, end="")
# #
# # f.close
#
#
# #Read line function
# f=open("piemr", "rt")
# # for i in range(3):
# print(f.readline())
# print(f.readline())
# print(f.readline())


# #
# # # #readlines for print in form of list
# f=open("piemr", "rt")
# print(f.readlines())
# f.close()

#
# #Writing and Appending to file
# f=open("piemr", "w")
# f.write("Python Scripting")
# f.close()
# #
# f=open("piemr", "w")
# # f.write("Hello World")
# (f.write("I hope you are Enjoying"))
#
# f.close()
# # #
# f=open("piemr", "a")
# f.write("I hope you are Enjoying")
# f.close()

#
#
# # #Handle read and write both
# f=open("piemr","r+")
# # print(f.read())
# f.write("Thank You")

#
#
# f=open("piemr1")
# #Access file by  with Block
with open("piemr1") as f:#it replaces both functions like open and close
    a=f.read()
    print(a)

#
#

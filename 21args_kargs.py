def func1(a,b,c,d):
    print(a,b,c,d)

# func1(4,5,6,7)
# # # If i has one more value than it is not going to
# # accept as it exceeds the length of variables
# func1(1,2,3,4,5)
# #
# # # To handle this we use *args & **kwargs and type of args is
# # always tuple
# # #
# def funargs( *args):
#      print(type(args))
#      for item in args:
#          print(item, end=" ")
# #
# a=[1,2,3,4,5,6,7,8]
# # #
# funargs(*a)
# # #
def funargs( *args, **kargs):
    # print(normal)
    print(type(args)) # Its type is tuple
    for item in args:
        print(item, end=" ")
        # print()
    for key, value in kargs.items():
        print(f"\n {key} is  {value}")

normal="Python scripting is fun"
arg = [1, 2, 3, 4, 5, 6, 7]
karg={"Clg":"Piemr", "Subject":"Python", "Workshop": "IOT"}
# #
funargs( normal, *arg,  **karg)
# #
#

# list=[]
# for i in range(100):
#     if i % 3 == 0:
#         list.append(i)
#
# print(list)
# #
# # #Above code will be done by list comprehension
# #
# list=[i for i in range(100) if i % 3 == 0 ]
# print(list)
# # #
# # #Dictionary Comprehension
dict1={i:f"Item {i}" for i in range(5)}
dict2={a:b for b,a in dict1.items()}
print(dict1)
print(dict2)

# # #
# # #
# # #set Comprehension
# # dresses={dress for dress in ["dress1", "dress2", "dress3", "dress2"]}
# # print (dresses)
# # # #
# #
# #
# # # #Generators Comprehensions
# evens=(i for i in range(100) if i % 5 ==0)
# for i in range(5):
#     print(evens.__next__())
# print(evens.__next__())
# print(evens.__next__())
# print(evens.__next__())
# print(evens.__next__())
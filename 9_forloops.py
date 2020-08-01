# list=["Harry", "Larry", "Carry", "Marie"]
# # # # #
# for item in list:
#     print(item)
#
list1=[["Harry", 80], ["Larry", 70], ["Carry", 85], ["Marie", 90]]
# for item in list1:
#     print (item)
# for item, Marks in list1:
#     print(f"{item} and mark is {Marks}")

# #
dict1=dict(list1)
print(dict1)

# for item in dict1:
#     print(item)
# #
# #
for item, Marks in dict1.items():
    print(item, "and Marks is", Marks)
# #

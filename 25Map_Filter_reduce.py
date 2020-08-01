#Map Function: Apply Any Function to a List

# lis=["3","34","64"]
# lis=list(map(int, lis))
# #
# for i in range(len(lis)):
#     lis[i] = int(lis[i])
# lis[2] = lis[2] + 1
#
# print(lis[2])

# num=[1,2,3,4,5,6]
# lst=[]
# def sq(a):
#     for item in a:
#         # b=0
#         b=item*item
#         lst.append(b)
# #
# sq(num)
# print(lst)
#     return a * a
#
# print(sq(num))

# num=list(map(sq, num))
# print(num)

# num=[1,2,3,4,5,6]
# print(num)
# num=list(map(lambda x : x * x, num))
# print(num)

# def sqr(a):
#         return a * a
# def cube(a):
#         return a*a*a
# #
# func=[cube, sqr]
# #
# for i in range(5):
#     val = list(map(lambda x:x(i), func))
#     print(val)


#Filter Function

list_1=[1,2,3,4,5,6,7,8,9]
# print(list_1)

# def is_greater_5(num):
#     lis = []
#     for item in num:
#         if item > 5:
#             lis.append(item)
#             # print(lis)
#     return (lis)
#
#
# print(is_greater_5(list_1))
# #
# gr_thn_5=list(filter(is_greater_5, list_1))
# gr_thn_5=list(filter(lambda x : x>5, list_1))
# print(gr_thn_5  )



# REDUCE
from functools import reduce
# #
list1=[1,2,3,4,5]
num=reduce(lambda x,y: x+y, list1)
print(num)
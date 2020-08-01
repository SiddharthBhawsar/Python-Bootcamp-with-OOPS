"""
Iterable- __iter__ or __getitem__  this method provides Iterator to that object in which it runs
Iterator - __next__
Iteration- Process of Iterate is  known as Iteration

Generator- Are the Iterators which get traverse only once
"""

#
# for i in range(100000000):
#     print(i)
#
# def gen(n):
#     for i in range (n):
#         yield i # Yield is a generator ie it generates values on the fly so that we save our ram
# #
# g=gen(5)
# # print(g)
# # for i in range(4):
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())


name="Nitesh"
ier=iter(name)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
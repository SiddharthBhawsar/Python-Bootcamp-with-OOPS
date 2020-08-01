s=set()
print(type(s))
#
s_from_list=set([1,2,3,4])
# # #
print(s_from_list)
#
s.add(1)
s.add(2)
print(s)
#
# # #
# # #
s1=s.union({1,2,3})
print(s, s1)

# #len, type, max, min, difference, issubset, isdisjoint , issupperset etc
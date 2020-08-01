# d1={}
# print(type(d1))
# # # # # # # #
# A={"Item1":50 , "Item2": 100, "Item3":50}
# # print(A["Item1"])
# # # # # #
# # # # # #
# # # # # #
# # # # # # #Keys should be or different and values may be either list, dictionary , Tuple etc
# # # # # #
d2={"College" : "Piemr", "Subject" : "IOT", "Language" : "Python", "Branch" :{"CS":"Computer", "EC": "Electronics", "ME":"Mechanical"}}
# # # # #
# print(d2["College"])
# print(d2["Branch"])
# d2["Branch"]["CE"]="CIVIL"
# d2["Library"]="Central"
# print(d2)
# d2["Branch"]["CE"]="XYZ"
# print(d2["Branch"])
# # # # # #
# # # d3={"A":1, "B":2, "C":1}
# # # print(d3["A"])
# # print(d2["list"][2])
# # # # print(d4) #Try to change the value for branch key
# # print(d2["Branch"]["ME"])
# # # # # # # #
# # # # # # #
# # # # # #
# # # # # # # #To add content in dictionary
# d2["CE"]="civil"
# d2["EE"]="Electrical"
# d2["Branch"]
# # # # #
# # print(d2)
# # # # # # #
# del d2["EE"]
# # # print(d2)
# # # # # # #
# # # # # # # # #As d2 and d3 are the pointers which points to dictionory so if you remove content from d3 it automatically gets remove from dictionary so it would not display with d2 as well
# d3=d2
# del d3["College"]
# print(d2)
# # # # # # #
# # # # # # # # #So to avoid above problem we have to use copy function
d3=d2.copy()
del d3["College"]
print(d2)
# # # # # #
# # # # # #
# print(d2["College"])
print(d2.get("College"))
# d2["url"]="piemr.com"
# d2.update({"url":"piemr.com"})
# # # # d4=d2["Branch"][0]
# # # # d4["EE"]="Electrical"
# # # # print(d4)
# # # # print(d2)
# # #
# # # # #
# # #
print(d2.keys())
print(d2)
d2.
print(d2.items())
# print(d2)
#
# # # # #
# # # # # #
# # d2.pop()
# d2.popitem()
# # #
# # # # # # #Explore Dictionary function of python
# # # # # #
# # # # # #
# # # # # # #Sample: Create dictionary and take input from the users and return the meaning of the word from the dictionary
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #

f=open("piemr1","rt")

print(f.tell()) #It tells where is the position of file pointer in our case f
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())

#
# #Seek moves your file pointer to the position
#
f.seek(0)
print(f.tell())
print(f.readline())



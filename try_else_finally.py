f1=open("oops9.py")

try:
    f=open('does.txt')

except Exception as e:
    print (e)

else:
    print("This will run if except is not running")

finally:
    print("Run this any way")
    f1.close()
    #f.close()

print ("Important Stuff")
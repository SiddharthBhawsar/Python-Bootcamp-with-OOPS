import pickle

#Pickling python object
# cars=["Audi", "BMW", "Maruti Suzuki"]
# file="mycars.pkl"
# fileobj=open (file, 'wb')
# pickle.dump(cars, fileobj)
# fileobj.close()

file="mycars.pkl"
fileobj=open(file, "rb")
mycar=pickle.load(fileobj)
print(mycar)
print(type(mycar))

#Assignment-What is pickle.load
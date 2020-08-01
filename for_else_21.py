#With for loop else gets executed if for loop normaly ended ie without break

khana=["Roti", "Chawal", "Dal"]

for item in khana:
    print(item)
    if item=="Dal" :
        break


else:
    print("This for loop is ended properly")

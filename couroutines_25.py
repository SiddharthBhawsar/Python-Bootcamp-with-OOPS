#This is used to save time
#For example we run a function which take long time for half
#And then it runs through the middle

def searcher():
    import time
    #some 4 second time consuming task
    book="This is a book for python programming. It is a good book"
    time.sleep(4)

    while True:
        text=(yield ) #This is the syntax for using searcher function as coroutine
        if text in book:
            print("Your text is in the book")

        else:
            print("Text is not in the book")

search=searcher()
next(search)

search.send("python")
input("Press any Key")
search.send("goodbye")

search.close()
# search.send("good")

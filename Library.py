## Library management system
## To make a program for library for displaying books,adding books,issuing books,returning books.
import datetime

# To display name of books.
def displaybooks(b):
    for item in b:
        print(item)

#To add a book in the        list by using append method.
def Addabook():
    name = input("Enter name of book:")
    Books.append(name)
    # print(Books)

#To issue a book and then removing the name of the book from the list by using remove method,and also recording the date and time of issuing.
def issuebook(book, name):
    if book in lendbook.keys():
        print(f"Book is already issued {lendbook[book]}")
        return 0
    lendbook.update({book:name})
    print(lendbook)
    # book = input("Enter the name of Book issuing: ")
    # Books.remove(book)
    # name = input("Enter your name: ")
    print(datetime.datetime.today())
    print(issue)

#To return a book and again adding the name in the list by using addpend method.
def returnbook():
    book = input("Enter the name of the book returning: ")
    # Books.append(book)
    lendbook.pop(book)
    name = input("Enter your name: ")
    # print(returned)

if __name__ == '__main__':
    lendbook={}

    Books = ["Python", "Think and Grow Rich", "Rich Dad Poor Dad", "You Can Win", "The Secret"]
    # Books.sort()
    # issue = "Book issued"
    # returned = "Book returned"



    while True:
        print('''Welcome to Readers Library.   
        1)Display Books
        2)Add a Book
        3)Issue Book
        4)Return Book''')
        n = int(input("Select a option:\n"))
        if n == 1:
           displaybooks(Books)
        elif n == 2:
           Addabook()
        elif n == 3:
            book = input("Enter the name of the book returning: ")
            name = input("Enter your name: ")

            issuebook(book, name)
        elif n == 4:
           returnbook()

        else:
            print("Not a valid option")


        print("Press q to quit and c to continue")
        user_choice2 = ""
        while(n!="c" and n!="q"):
            n = input()
            if n == "q":
                exit()

            elif n == "c":
                continue

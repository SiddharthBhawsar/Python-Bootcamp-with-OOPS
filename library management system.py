


def availbooks(booklist):
    for item in booklist:
        print(item)

def issuebook(book,name):
    if book in lendBook.keys():
        print(f"book is already issued to {lendBook[book]}")
    else:
        print("Book is available for issuance")
        lendBook[book] = name
        return 0

def returnbook():
    pass
def addbook():
    pass

# if __name__ == '__main__':
books = ["Python", "C", "Arithmatics", "Samuel George","Fundamentals of Physics"]
lendBook= {}

while True:

        print("""
        Welcome to Studio Library
        Select option-
        1. AVailable books
        2. Issue a Book
        3. Return a Book
        4. Add a book""")

        n=int(input("enter your choice:\n"))

        if n==1:
            availbooks(books)

        elif n==2:
            bookname = input("ENter the book u want to issue\n")
            Name = input("Enter ur name")
            issuebook(bookname, Name)
        elif n==3:
            returnbook()
        elif n==4:
            addbook()
        else:
            print("not a valid option")


        print("press c to continue and q to quit")
        user_choice = ""
        while(n!="c" and n!="q"):
            n=input()
            if n=="q":
                exit()
            if n=="c":
                continue
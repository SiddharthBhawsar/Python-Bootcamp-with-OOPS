# 1. Display Book Function
# 2. Lend a Book
# 3. Add Book
# 4. Return Book
book_info={}
def display_book(books, library_name):
    print(f"We have following books in our library: {library_name}")
    for item in books:
        print(item)

def lend_book(book, name):

    if book not in book_info.keys():
        book_info.update({book, name})
        print("Lender-Book database has been updated. You can take book")

    else:
        print("Book is already issued")
        # print(f"Book is already being used by {book_info[book]})
            # book_info.update({book, name})

def add_book():
    pass

def return_book():
    pass

while True:

    print("Welcome to the MaaC_Library library. Enter your choice to continue")
    print("1. Display Books")
    print("2. Lend a Book")
    print("3. Add a Book")
    print("4. Return a Book")

    user_choice=int(input())


    books=["c++", "compiler design", "python", "java"]
    book_info = {}
    if user_choice==1:

        display_book(books, "IBM Library")

    elif user_choice==2:
        book = input("Enter the name of the book you want to lend: ")
        name = input("Enter your name: ")
        lend_book(book, name)

    elif user_choice==3:
        add_book()

    elif user_choice==4:
        return_book()

    else:
        print("Not a valid option")

    print("Press q to quit and c to continue")
    user_choice2 = ""
    while (user_choice2 != "c" and user_choice2 != "q"):
        user_choice2 = input()
        if user_choice2 == "q":
            exit()

        elif user_choice2 == "c":
            continue
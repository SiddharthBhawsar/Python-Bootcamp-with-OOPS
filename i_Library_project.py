

def display_books(books, library_name):
    print(f"We have following books in our library: {library_name}")
    for item in books:
        print(item)



def lend_books(book, name):
    if book in book_info.keys():
        print (f"book has been issued : {book_info[book]}")
    else:
        print(f"book is available")
        book_info[book]=name

def  books_add(book_2):
    books.append(book_2)

def book_return(book_1):
    book_info.pop(book_1)




book_info={}

books=["java" , "c++" , "python" , "mathematics"]
while True:
    print("Select option you want: ")
    print("1. Display book")
    print("2. Lend book")
    print("3. Add book")
    print("4. Return")

    user_choice=int(input())



    if user_choice==1:
          display_books(books, "IBM library")



    elif user_choice==2:

        student_name =input("enter your name ")
        book_required = input("enter the book you want ")
        lend_books(book_required, student_name)



    elif user_choice==3:
       book_2=input("enter a new book you want to add ")
       books_add(book_2)



    elif user_choice==4:
        book_1=input("book you want to return ")
        book_return(book_1)

    else:
        print("Please enter valid option")

    # print("Press c to continue and q to quit")
    # opt=""
    # while (user_choice != 'c' and user_choice != 'q'):
    #     user_choice=input()
    #     if user_choice == 'c':
    #         continue
    #
    #     elif opt=='q':
    #         exit()

    print("Press q to quit and c to continue")
    user_choice = ""
    while (user_choice != "c" and user_choice != "q"):
        user_choice = input()
        if (user_choice == "q"):
            exit()

        elif (user_choice == "c"):
            continue

#else:
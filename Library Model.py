def display_book(book):
    print("We have following books in our library :")
    for item in book:
        print(item)
def lend_book(name,b_name):
    pass

book_list=["Let us c","Java","Python","Harry Potter"]
book_info={}
while(True):
    print("Welcome to the library. Enter your choice to continue :")
    print("1.Display Books\n2.Lend a Book\n3.Add a Book\n4.Return a Book")

    opt=(input())
    # if opt not in ['1','2','3','4']:
    #     print("Please enter a valid input.")
    #     continue
    # else:
    #     opt=int(opt)


    if (opt=="1"):
        display_book(book_list)
    elif (opt=="2"):
        l_book=input("Enter the name of the book you want : ")
        l_name=input("Enter your name")
        # if l_book in book_info.keys():
        #     print(f"Book is already issued to {book_info[l_book]}")
        # else:
        #     print("Book is been issued.")
        #     print(book_info)
        # book_info[l_book] = l_name
        # print(book_info)
    else:
        print("Not a valid option")

    print("Press c to continue and q to quit")
    opt = ""
    while (opt != "c" and opt != "q"):
        opt = input()
        if (opt == "q"):
            exit()
        elif (opt == "c"):
            continue



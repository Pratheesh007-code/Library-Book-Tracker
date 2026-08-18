books = {}

while True:
    print("\n1.Add 2.Issue 3.Return 4.Check 5.View 6.Exit")
    ch = input("Choice: ")

    if ch == "1":
        i = input("Book ID: ")

        if i not in books:
            q = int(input("Quantity: "))

            if q > 0:
                books[i] = [
                input("Title: "),
                input("Author: "),
                q
                ]
                print("Book Added")
            else:
                print("Invalid Quantity")
        else:
            print("Book Exists")
            
    elif ch == "2":
        i = input("Book ID: ")

        if i in books and books[i][2] > 0:
            books[i][2] -= 1
            print("Book Issued")
        else:
            print("Book Not Available")

    elif ch == "3":
        i = input("Book ID: ")

        if i in books:
            books[i][2] += 1
            print("Book Returned")
        else:
            print("Book Not Found")

    elif ch == "4":
        i = input("Book ID: ")
        print(books.get(i, "Book Not Found"))

    elif ch == "5":
        print(books)

    elif ch == "6":
        break
books = {}

while True:
    print("\n1.Add 2.View 3.Check 4.Issue 5.Return 6.Search 7.Update 8.Delete 9.Exit")
    ch = input("Choice: ")

    if ch == "1":
        i = input("Book ID: ")

        if i not in books:
            books[i] = [
                input("Title: "),
                input("Author: "),
                int(input("Quantity: "))
            ]
            print("Book Added")
        else:
            print("Book Exists")

    elif ch == "2":
        for i, b in books.items():
            print(i, b)

    elif ch == "3":
        i = input("Book ID: ")
    
        if i in books:
            print("Title:", books[i][0])
            print("Author:", books[i][1])
            print("Quantity:", books[i][2])
        else:
            print("Book Not Found")
    elif ch == "4":
        i = input("Book ID: ")

        if i in books and books[i][2] > 0:
            books[i][2] -= 1
            print("Book Issued")
        else:
            print("Book Not Available")

    elif ch == "5":
        i = input("Book ID: ")

        if i in books:
            books[i][2] += 1
            print("Book Returned")
        else:
            print("Book Not Found")

    elif ch == "6":
        key = input("Search: ").lower()
    
        for i, b in books.items():
            if key in b[0].lower() or key in b[1].lower():
                print(i, b)

    elif ch == "7":
        i = input("Book ID: ")
    
        if i in books:
            books[i][0] = input("New Title: ")
            books[i][1] = input("New Author: ")
            print("Book Updated")
        else:
            print("Book Not Found")

    
    elif ch == "8":
        i = input("Book ID: ")
        if i in books:
            del books[i]
            print("Book Deleted")
        else:
            print("Book Not Found")

    elif ch == "9":
        break
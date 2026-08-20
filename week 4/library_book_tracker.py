books = {}

while True:
    print("\n1.Add 2.View 3.Update 4.Delete 5.Exit")
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
            books[i][0] = input("New Title: ")
            books[i][1] = input("New Author: ")
            print("Book Updated")
        else:
            print("Book Not Found")

    elif ch == "4":
        i = input("Book ID: ")
    
        if i in books:
            del books[i]
            print("Book Deleted")
        else:
            print("Book Not Found")

    elif ch == "5":
        break
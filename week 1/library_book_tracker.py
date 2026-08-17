books = []

while True:
    print("\n1.Add 2.Issue 3.Return 4.Check 5.View 6.Exit")
    ch = input("Choice: ")

    if ch == "1":
        i = input("Book ID: ")
        found = False

        for b in books:
            if b[0] == i:
                found = True
        if not found:
            q = int(input("Quantity: "))
            if q > 0:
                books.append([
                    i,
                    input("Title: "),
                    input("Author: "),
                    q
                ])
                print("Book Added")
            else:
                print("Invalid Quantity")
    elif ch == "2":
        i = input("Book ID: ")
        for b in books:
            if b[0] == i and b[3] > 0:
                b[3] -= 1
                print("Book Issued")
                break
        else:
            print("Book Not Available")

    elif ch == "3":
        i = input("Book ID: ")
        for b in books:
            if b[0] == i:
                b[3] += 1
                print("Book Returned")
                break

    elif ch == "4":
        i = input("Book ID: ")
        for b in books:
            if b[0] == i:
                print(b)
                break
        else:
            print("Book Not Found")

    elif ch == "5":
        for b in books:
            print(b)

    elif ch == "6":
        break
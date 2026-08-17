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
        found = False
    
        for b in books:
            if b[0] == i:
                found = True
    
                if b[3] > 0:
                    b[3] -= 1
                    print("Book Issued")
                else:
                    print("Book Not Available")
                break
    
        if not found:
            print("Book Not Found")

    elif ch == "3":
        i = input("Book ID: ")
        found = False
    
        for b in books:
            if b[0] == i:
                b[3] += 1
                found = True
                print("Book Returned")
                break
    
        if not found:
            print("Book Not Found")
            
    elif ch == "4":
        i = input("Book ID: ")
        found = False
    
        for b in books:
            if b[0] == i:
                print("Book ID:", b[0])
                print("Title:", b[1])
                print("Author:", b[2])
                print("Quantity:", b[3])
                found = True
                break
    
        if not found:
            print("Book Not Found")
    elif ch == "5":
        for b in books:
            print(b)

    elif ch == "6":
        break
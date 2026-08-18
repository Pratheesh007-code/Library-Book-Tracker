books = {}

while True:
    print("\n1.Add 2.View 3.Exit")
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
        break
books = {}

while True:
    print("\n1.Add  2.View  3.Save  4.Exit")
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
        with open("books.txt", "w") as f:
            for i, b in books.items():
                f.write(f"{i}|{b[0]}|{b[1]}|{b[2]}\n")
        print("Books Saved")

    elif ch == "4":
        break
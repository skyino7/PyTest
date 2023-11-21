
def main():

    booksList = []

    # infile = open("BooksList.txt", "r")
    # line = infile.readline()
    # while line:
    #     booksList.append(line.rstrip("\n").split(","))
    #     line = infile.readline()
    # infile.close()

    choice = 0
    while choice != 4:
        print("*** Books Manager ***")
        print("1) Add a book")
        print("2) Lookup a book")
        print("3) Display books")
        print("4) Quit")
        choice = int(input("Enter Your Choice (1-4) "))

        if choice == 1:
            print("Adding a book...")
            nBook = input("Enter the name of the book >>> ")
            nAuthor = input("Enter the name of the Author >>> ")
            nPages = int(input("Enter the number of pages >>> "))
            booksList.append([nBook, nAuthor, nPages])
        elif choice == 2:
            print("Searching for a book...")
            keyword = input("Enter Search Term: ")
            for book in booksList:
                if keyword in book:
                    print(book)
        elif choice == 3:
            print("Displaying all books....")
            for book in range(len(booksList)):
                print(booksList[book])
        elif choice == 4:
            print("Quitting Program..................")

        else:
            print("Wrong Selection")


if __name__ == "__main__":
    main()

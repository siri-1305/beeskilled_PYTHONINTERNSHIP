#LIBRARY MANAGEMENT SYSTEM
class Library:
    def __init__(self):
        self.books = ['a','b','c','d']

    def retur(self, book):
        self.books.append(book)
        print("BOOK RETURNED SUCCESSFULLY")

    def issue(self, book):
        if book in self.books:
            self.books.remove(book)
            print("BOOK ISSUED SUCCESSFULLY")
        else:
            print("BOOK NOT FOUND")


library = Library()

while True:
    print("""borrow or return
1 - borrow
2 - return
3 - exit""")

    opt = int(input(">>> "))

    if opt == 1:
        book = input("Enter the book name you need to borrow: ")
        library.issue(book)

    elif opt == 2:
        book = input("Enter the book name to return: ")
        library.retur(book)

    elif opt == 3:
        break

    else:
        print("Invalid input")


class Book():
    def __init__(self,book_id,title,author):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.is_avilable=True


class Library():
    def __init__(self,):
        self.books={}

    def add_book(self,book):
        if(book.book_id in self.books):
            print("Book Id already exist")
        else:
            self.books[book.book_id]=book
            print(f"Book Added: {book.title}")
    
    def remove_book(self,book_id):
        if(book_id in self.books):
            removed=self.books.pop(book_id)
            print(f"Book Removed: {removed.title}")
        else:
            print("Book not found!")
    
    def issue_book(self,book_id):
        if(book_id in self.books):
            book=self.books[book_id]
            if book.is_avilable:
                book.is_avilable=False
                print(f"Book Issued: {book.title}")
            else:
                print("Book already issued!")
        else:
             print("Book not found!")
    
    def return_book(self,book_id):
        if(book_id in self.books):
            book=self.books[book_id]
            if not book.is_avilable:
                book.is_avilable=True
                print(f"Book Issued: {book.title}")
            else:
                print("Book was not issued!")
        else:
            print("Book not found!")
    
    def display(self):
        if not self.books:
             print("Library is empty")
        else:
            for book in self.books:
                print(book)
    
library = Library()

while True:
    print("\n1. Add Book")
    print("2. Remove Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        book_id = input("Enter Book ID: ")
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        book = Book(book_id, title, author)
        library.add_book(book)

    elif choice == "2":
        book_id = input("Enter Book ID to remove: ")
        library.remove_book(book_id)

    elif choice == "3":
        book_id = input("Enter Book ID to issue: ")
        library.issue_book(book_id)

    elif choice == "4":
        book_id = input("Enter Book ID to return: ")
        library.return_book(book_id)

    elif choice == "5":
        library.display()

    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")


        


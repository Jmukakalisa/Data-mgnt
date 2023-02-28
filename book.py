# Books Library management system

class Book:        # a class of books with their properties
    def __init__(self, title, author, publication_year, isbn, available=True):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.isbn = isbn
        self.available = available

class Library:          # Initializing a library
    def __init__(self):
        self.books = []
        self.total_books = 0
    
    # A function to add books to the library
    def add_book(self, title, author, publication_year, isbn):
        book = Book(title, author, publication_year, isbn)
        self.books.append(book)
        self.total_books += 1

    # A function to remove a book from library
    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                self.total_books -= 1
                return True
        return False

    # A function to search a book in library
    def search_book(self, search_type, keyword):
        found_books = []
        for book in self.books:
            if search_type == 'title':
                if keyword.lower() in book.title.lower():
                    found_books.append(book)
            elif search_type == 'author':
                if keyword.lower() in book.author.lower():
                    found_books.append(book)
            elif search_type == 'publication_year':
                if keyword == book.publication_year:
                    found_books.append(book)
            elif search_type == 'isbn':
                if keyword == book.isbn:
                    found_books.append(book)
        return found_books

    # A function to display the availability of book in the library
    def display_books(self):
        for book in self.books:
            print(f"{book.title} by {book.author} ({book.publication_year}) - ISBN: {book.isbn} - {'Available' if book.available else 'Not available'}")

    # A function to check out a book from library
    def checkout_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and book.available:
                book.available = False
                return True
        return False

    # A function to return a book in a library
    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and not book.available:
                book.available = True
                return True
        return False

    # A function to get available books in the library
    def get_available_books_count(self):
        count = 0
        for book in self.books:
            if book.available:
                count += 1
        return count



# Snippet codes of how to use the library
library = Library()
# Add books
library.add_book("Life's Work A moral Argument For Choice", "DR. Willie J. Parker", 2017, "978-1-5011-5113-2")
library.add_book("Learning Python", "Mark Lutz", 2013, "978-1449355739")
library.add_book("To Kill a Mockingbird", "Harper Lee", 1960, "0446310786")
library.add_book("Fluent Python", "Luciano Ramalho", 2015, "978-1491946008")
library.add_book("Carving of A Firebrand", "Irene Kendi", 2022, "978-1-5607-3262-6")
library.add_book("Python for Data Analysis", "Wes McKinney", 2017, "978-1491957660")

# Display all books
print("The list of books in the library: ")
library.display_books()

# Search for books by title
found_books = library.search_book('title', 'to')
for book in found_books:
    print("Found the book " + book.title + " in the library")

# Checkout a book
isbn = "978-1-5607-3262-6"
if library.checkout_book(isbn):
    print(f"The book with ISBN {isbn} has been checked out.")
else:
    print(f"The book with ISBN {isbn} is not available for checkout.")

# Return a book
isbn = "978-1-5607-3262-6"
if library.return_book(isbn):
    print(f"The book with ISBN {isbn} has been returned.")
else:
    print(f"The book with ISBN {isbn} is yet to be returned.")

# Display the number of available books
print(f"There are {library.get_available_books_count()} available books in the library.")
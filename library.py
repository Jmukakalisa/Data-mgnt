# Library management system
class LibraryBook:
    def __init__(self, title, author, publication_year, isbn, available=True):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.isbn = isbn
        self.available = available

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year}) - ISBN: {self.isbn} - {'Available' if self.available else 'Not available'}"
    
    def checkout(self):
        if self.available:
            self.available = False
            return True
        else:
            return False

    def checkin(self):
        self.available = True


# Snippet codes:

# Import the Library and LibraryBook classes from the previous example
from typing import List

class Library:
    def __init__(self):
        self.books = []
        self.total_books = 0

    def add_book(self, title, author, publication_year, isbn):
        book = LibraryBook(title, author, publication_year, isbn)
        self.books.append(book)
        self.total_books += 1

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                self.total_books -= 1
                return True
        return False

    def search_book(self, search_term) -> List[LibraryBook]:
        found_books = []
        for book in self.books:
            if search_term.lower() in book.title.lower() or search_term.lower() in book.author.lower() or search_term.lower() in book.isbn.lower():
                found_books.append(book)
        return found_books

    def display_books(self):
        for book in self.books:
            print(book)

    def checkout_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and book.checkout():
                return True
        return False

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                book.checkin()
                return True
        return False

    def get_available_books_count(self):
        count = 0
        for book in self.books:
            if book.available:
                count += 1
        return count

# Create a new library object
library = Library()

# Add three new books to the library
library.add_book("Learning Python", "Mark Lutz", 2013, "978-1449355739")
library.add_book("Carving of A Firebrand", "Irene Kendi", 2022, "978-1-5607-3262-6")
library.add_book("Python for Data Analysis", "Wes McKinney", 2017, "978-1491957660")
library.add_book("Life's Work A moral Argument For Choice", "DR. Willie J. Parker", 2017, "978-1-5011-5113-2")
library.add_book("To Kill a Mockingbird", "Harper Lee", 1960, "0446310786")
library.add_book("Fluent Python", "Luciano Ramalho", 2015, "978-1491946008")

# Search for books with the search term "Python" and print the results
search_results = library.search_book("Python")
if search_results:
    print("Search results:")
    for book in search_results:
        print(book)
else:
    print("No results found for search term 'Python'.")

# Check out one of the books
isbn_to_checkout = "978-1449355739"
if library.checkout_book(isbn_to_checkout):
    print(f"The book with ISBN {isbn_to_checkout} has been checked out.")
else:
    print(f"The book with ISBN {isbn_to_checkout} is not available for checkout.")

# List all of the books in the library
print("All books in the library:")
library.display_books()

# Check in the book that was checked out
isbn_to_return = "978-1449355739"
if library.return_book(isbn_to_return):
    print(f"The book with ISBN {isbn_to_return} has been returned.")
else:
    print(f"The book with ISBN {isbn_to_return} is not in the library or has not been checked out.")


print("All books in the library after returning a book:")
library.display_books()


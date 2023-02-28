The codes in book.py file implements a simple book library management system. The system consists of two classes: Book and Library.

// The Book class has the following properties:

title: The title of the book
author: The author of the book
publication_year: The publication year of the book
isbn: The ISBN of the book
available: A flag to indicate if the book is available for checkout or not. The default value is True.
The Library class has the following methods:

init(): Initializes a new instance of the Library class. It initializes an empty list to store the books and sets the total_books count to 0.
add_book(): Adds a new book to the library by creating a new instance of the Book class and appending it to the books list. It also increments the total_books count.
remove_book(): Removes a book from the library based on its ISBN. It searches for the book with the given ISBN in the books list, removes it from the list, and decrements the total_books count. If the book is not found, it returns False.
search_book(): Searches for books in the library based on the search type and keyword. The search type can be title, author, publication_year, or ISBN. It returns a list of books that match the search criteria.
display_books(): Displays all the books in the library along with their title, author, publication year, ISBN, and availability status.
checkout_book(): Checks out a book from the library based on its ISBN. It searches for the book with the given ISBN in the books list, sets its available flag to False, and returns True if successful. If the book is not found or already checked out, it returns False.
return_book(): Returns a book to the library based on its ISBN. It searches for the book with the given ISBN in the books list, sets its available flag to True, and returns True if successful. If the book is not found or already returned, it returns False.
get_available_books_count(): Returns the number of books that are currently available in the library.

The code also provides an example of how to use the Library class. It creates a new instance of the Library class, adds some books to it, displays all the books, searches for books by title, checks out a book, returns a book, and displays the number of available books in the library.



// While the code in library.py file defines a Library class and a LibraryBook class for managing a library's books.

The LibraryBook class has the following attributes:

title: the title of the book
author: the author of the book
publication_year: the year the book was published
isbn: the ISBN number of the book
available: a boolean value indicating whether the book is available for checkout
The LibraryBook class also has the following methods:

str(self): a method that returns a string representation of the book
checkout(self): a method that checks out the book if it is available
checkin(self): a method that checks in the book, making it available again
The Library class has the following attributes:

books: a list of all the books in the library
total_books: the total number of books in the library
The Library class also has the following methods:

add_book(self, title, author, publication_year, isbn): adds a new book to the library
remove_book(self, isbn): removes a book from the library given its ISBN number
search_book(self, search_term): searches for books in the library based on a search term (case-insensitive)
display_books(self): displays all the books in the library
checkout_book(self, isbn): checks out a book from the library given its ISBN number
return_book(self, isbn): returns a book to the library given its ISBN number
get_available_books_count(self): returns the number of books available for checkout in the library
The code creates a new Library object and adds six books to it. It then searches for books with the search term "Python" and prints the results. It checks out one of the books and then lists all the books in the library. It returns the book that was checked out and lists all the books in the library again.



Both file contain codes that implement a library management system. You can either use one or the other.

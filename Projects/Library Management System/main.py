""" 
Library Management System

"""

class Library:
    def __init__(self):
        # Initialize the library with no books
        self.no_of_books = 0
        self.books = []

    def add_book(self, book_name):
        """Add a new book to the library."""
        self.books.append(book_name)
        self.no_of_books += 1
        print(f'Book "{book_name}" added to the library.')

    def print_all_books(self):
        """Print all books in the library."""
        if self.no_of_books == 0:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for idx, book in enumerate(self.books, start=1):
                print(f"{idx}. {book}")

    def get_no_of_books(self):
        """Return the number of books in the library."""
        return self.no_of_books


# Demonstrate the Library class functionality
if __name__ == "__main__":
    library = Library()  # Create a library instance

    # Adding books to the library
    library.add_book("The Great Gatsby")
    library.add_book("To Kill a Mockingbird")
    library.add_book("1984")

    # Print all books
    library.print_all_books()

    # Get the number of books
    print(f"Number of books in the library: {library.get_no_of_books()}")

    # Exit the program to demonstrate that books are not persisted
    print("\nExiting the program. Restart the program to see the state reset.")

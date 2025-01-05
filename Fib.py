class Book:
    def __init__(self, title, author, availability=True):
        """Initialize the book with title, author, and availability status."""
        self.title = title
        self.author = author
        self.availability = availability

    def display_info(self):
        """Display the information about the book."""
        availability_status = "Available" if self.availability else "Checked Out"
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {availability_status}")
    
    def check_out(self):
        """Check out the book (change its status to checked out)."""
        if self.availability:
            self.availability = False
            print(f"The book '{self.title}' has been checked out.")
        else:
            print(f"Sorry, the book '{self.title}' is already checked out.")
    
    def return_book(self):
        """Return the book (change its status back to available)."""
        if not self.availability:
            self.availability = True
            print(f"The book '{self.title}' has been returned and is now available.")
        else:
            print(f"The book '{self.title}' is already available.")


class LibraryCatalogue:
    def __init__(self):
        """Initialize the library catalogue (a list to store books)."""
        self.books = []

    def add_book(self, title, author):
        """Add a new book to the catalogue."""
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Book '{title}' by {author} added to the catalogue.")
    
    def display_all_books(self):
        """Display all books in the catalogue."""
        if self.books:
            print("\nLibrary Catalogue:")
            for book in self.books:
                book.display_info()
                print("-" * 30)
        else:
            print("The catalogue is empty.")
    
    def find_book(self, title):
        """Find a book by its title in the catalogue."""
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None


# Simple scenario of using the system

def main():
    # Create the library catalogue system
    catalogue = LibraryCatalogue()
    
    # Add some books to the catalogue
    catalogue.add_book("To Kill a Mockingbird", "Harper Lee")
    catalogue.add_book("1984", "George Orwell")
    catalogue.add_book("The Great Gatsby", "F. Scott Fitzgerald")
    
    # Display all books in the catalogue
    catalogue.display_all_books()
    
    # Check out a book
    book_to_check_out = catalogue.find_book("1984")
    if book_to_check_out:
        book_to_check_out.check_out()
    else:
        print("Book not found in the catalogue.")
    
    # Try to check out the same book again
    if book_to_check_out:
        book_to_check_out.check_out()

    # Return the book
    if book_to_check_out:
        book_to_check_out.return_book()

    # Display all books after returning a book
    catalogue.display_all_books()

if __name__ == "__main__":
    main()

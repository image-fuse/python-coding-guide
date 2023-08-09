class Book:
    def __init__(self, title: str, author: str, isbn: str, genre: str, availability: bool = True):
        """
        Initialize a Book object.

        Parameters:
        title (str): The title of the book.
        author (str): The author of the book.
        isbn (str): The ISBN of the book.
        genre (str): The genre of the book.
        availability (bool, optional): The availability status of the book. Defaults to True.

        Returns:
        None
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.availability = availability

    def __str__(self) -> str:
        """
        Return a string representation of the Book.

        Returns:
        str: The formatted string representing the book.
        """
        status = "Available" if self.availability else "Borrowed"
        return f"{self.title} by {self.author} ({status})"


class LibraryCatalog:
    def __init__(self):
        self.books = []

    def add_book(self, title: str, author: str, isbn: str, genre: str) -> None:
        """
        Add a book to the library catalog.

        Parameters:
        title (str): The title of the book.
        author (str): The author of the book.
        isbn (str): The ISBN of the book.
        genre (str): The genre of the book.

        Returns:
        None
        """
        book = Book(title, author, isbn, genre)
        self.books.append(book)

    def get_book_details(self, isbn: str) -> str:
        """
        Get the details of a book based on its ISBN.

        Parameters:
        isbn (str): The ISBN of the book.

        Returns:
        str: The details of the book as a formatted string.
        """
        for book in self.books:
            if book.isbn == isbn:
                return f"Title: {book.title}\nAuthor: {book.author}\nGenre: {book.genre}\nAvailability: {'Available' if book.availability else 'Borrowed'}"
        return "Book not found in the catalog."

    def get_all_books(self) -> list:
        """
        Get a list of string representations of all books in the catalog.

        Returns:
        list: List of string representations of books.
        """
        return [str(book) for book in self.books]

    def borrow_book(self, isbn: str) -> str:
        """
        Borrow a book from the catalog.

        Parameters:
        isbn (str): The ISBN of the book to borrow.

        Returns:
        str: A message indicating the success or failure of borrowing.
        """
        for book in self.books:
            if book.isbn == isbn:
                if book.availability:
                    book.availability = False
                    return f"You have borrowed '{book.title}'."
                else:
                    return f"'{book.title}' is already borrowed."
        return "Book not found in the catalog."

    def return_book(self, isbn: str) -> str:
        """
        Return a borrowed book to the catalog.

        Parameters:
        isbn (str): The ISBN of the book to return.

        Returns:
        str: A message indicating the success or failure of returning.
        """
        for book in self.books:
            if book.isbn == isbn:
                if not book.availability:
                    book.availability = True
                    return f"You have returned '{book.title}'."
                else:
                    return f"'{book.title}' is already available."
        return "Book not found in the catalog."

# Example usage
catalog = LibraryCatalog()

catalog.add_book("Muna Madan", "Laxmi Prasad Devkota", "978-0618260300", "Fantasy")
catalog.add_book("To Kill a Mockingbird", "Harper Lee", "978-0061120084", "Fiction")

print(catalog.get_all_books())

print(catalog.borrow_book("978-0618260300"))
print(catalog.borrow_book("978-0061120084"))

print(catalog.get_all_books())

print(catalog.return_book("978-0618260300"))

print(catalog.get_all_books())

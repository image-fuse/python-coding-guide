# A module should be responsible to one, and only one, actor.

class Book:
    def __init__(self, title, author, isbn, genre, availability=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.availability = availability

    def __str__(self):
        status = "Available" if self.availability else "Borrowed"
        return f"{self.title} by {self.author} ({status})"


class LibraryCatalog:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, isbn, genre):
        book = Book(title, author, isbn, genre)
        self.books.append(book)

    def get_book_details(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return f"Title: {book.title}\nAuthor: {book.author}\nGenre: {book.genre}\nAvailability: {'Available' if book.availability else 'Borrowed'}"
        return "Book not found in the catalog."

    def get_all_books(self):
        return [str(book) for book in self.books]

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.availability:
                    book.availability = False
                    return f"You have borrowed '{book.title}'."
                else:
                    return f"'{book.title}' is already borrowed."
        return "Book not found in the catalog."

    def return_book(self, isbn):
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

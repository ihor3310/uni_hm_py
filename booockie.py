class Book:
    def __init__(self, title, author, isbn, year_published):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year_published = year_published

    def get_info(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Published: {self.year_published}"

class FictionBook(Book):
    def __init__(self, title, author, isbn, year_published, genre):
        super().__init__(title, author, isbn, year_published)
        self.genre = genre

    def get_info(self):
        return f"{super().get_info()}, Genre: {self.genre}"

class NonFictionBook(Book):
    def __init__(self, title, author, isbn, year_published, topic):
        super().__init__(title, author, isbn, year_published)
        self.topic = topic

    def get_info(self):
        return f"{super().get_info()}, Topic: {self.topic}"

class ReferenceBook(Book):
    def __init__(self, title, author, isbn, year_published, description):
        super().__init__(title, author, isbn, year_published)
        self.description = description

    def get_info(self):
        return f"{super().get_info()}, Description: {self.description}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]

    def get_books(self):
        return [book.get_info() for book in self.books]

    def get_books_by_category(self, category):
        if category == "fiction":
            return [book.get_info() for book in self.books if isinstance(book, FictionBook)]
        elif category == "nonfiction":
            return [book.get_info() for book in self.books if isinstance(book, NonFictionBook)]
        elif category == "reference":
            return [book.get_info() for book in self.books if isinstance(book, ReferenceBook)]
        else:
            return []

    def get_books_by_author(self, author):
        return [book.get_info() for book in self.books if book.author.lower() == author.lower()]

    def get_books_by_year(self, year):
        return [book.get_info() for book in self.books if book.year_published == year]

library = Library()

book1 = FictionBook("Втеча з міста", "Andrey Ptach", "346780", 1995, "Novel")
book2 = NonFictionBook("Далеко за містом", "Horobetz Yuriy", "974320", 2007, "Poem")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

print("All books in the library:")
print("\n".join(library.get_books()))

print("\nFiction books:")
print("\n".join(library.get_books_by_category("fiction")))

print("\nNon-Fiction books:")
print("\n".join(library.get_books_by_category("nonfiction")))

print("\nReference books:")
print("\n".join(library.get_books_by_category("reference")))

print("\nBooks by Horobetz Yuriy:")
print("\n".join(library.get_books_by_author("Horobetz Yuriy")))

print("\nBooks published in 1995:")
print("\n".join(library.get_books_by_year(1995)))

library.remove_book("346780")
print("\n".join(library.get_books()))

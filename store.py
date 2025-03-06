import json
import os

from book import Book


class Store:
    def __init__(self, file="books.json"):
        self.file = file
        self.books = []
        self.load_book()
        self.view_books()

    def load_book(self):
        if not os.path.exists(self.file) or os.stat(self.file).st_size == 0:
            print(f"Warning: {self.file} is missing or empty. No books loaded.")
            return

        try:
            with open(self.file, "r") as fl:
                data = json.load(fl)
            if not isinstance(data, dict):
                print(f"Error: {self.file} does not contain a valid JSON structure")

            self.books.clear()
            for bk in data.get("books", []): # with null checked
                book = Book(
                    bk['title'],
                    bk['author'],
                    bk['isbn'],
                    bk['genre'],
                    bk['price'],
                    bk['quantity'],
                    bk['publisher'],
                    bk['year']
                )
                self.books.append(book)

        except FileNotFoundError:
            print(f"Warning: {self.file} not found. No books loaded.")

        except json.JSONDecodeError:
            print(f"Error: {self.file} contains invalid JSON and could not be read.")

    def save_book(self):
        data = {'books': [book.__dict__ for book in self.books]}
        with open(self.file, 'w') as file:
            json.dump(data, file, indent=4)

    def add_book(self, book):
        add = True
        for bk in self.books:
            if bk.isbn == book.isbn:
                print(f"A book with ISBN {book.isbn} already exists in the library.")
                add = False
        if add:
            self.books.append(book)
            self.save_book()
        print(book)

    def view_books(self):
        for book in self.books:
            print(book)

    def search_books(self, term):
        books = []
        for book in self.books:
            if term.lower() in book.title.lower() or term.lower() in book.isbn.lower():
                books.append(book)
        return books

    def remove_book(self, isbn):
        match_book = None
        for book in self.books:
            if book.isbn == isbn:
                match_book = book
                break
        self.books.remove(match_book)
        self.save_book()

        if match_book:
            return True
        else:
            return False

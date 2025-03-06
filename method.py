import re
from book import Book

def get_valid_text(title_text):
    while True:
        title = input(f"Enter the {title_text}: ").strip()
        if title and not title.isdigit():  # Ensure it's not empty or a number
            return title
        else:
            print(f"Error: {title_text} must be a valid string.")

def get_float_number(title):
    while True:
        try:
            price = float(input(f"Enter the {title}: ").strip())
            if price > 0:
                return price  # Return valid price
            else:
                print(f"Error: {title} must be a positive value.")
        except ValueError:
            print("Error: Please enter a valid number.")

def get_int_number(title):
    while True:
        try:
            quantity = int(input(f"Enter the {title}: ").strip())
            if quantity > 0:
                return quantity  # Return valid quantity
            else:
                print(f"Error: {title} must be a positive number.")
        except ValueError:
            print("Error: Please enter a valid integer.")

def get_valid_year():
    while True:
        try:
            year = int(input("Enter the year: ").strip())
            if 1000 <= year <= 9999:
                return year
            else:
                print("Error: Year must be a four-digit number (e.g., 2023).")
        except ValueError:
            print("Error: Please enter a valid year (four-digit number).")

def get_valid_isbn():
    while True:
        isbn = input("Enter the book ISBN: ").strip().replace("-", "")  # Remove hyphens
        if re.fullmatch(r"\d{10}|\d{13}", isbn):
            return isbn
        print("Error: ISBN must be a 10 or 13-digit number (ignoring hyphens).")


def add_book(store):
    print("Enter Information to Add A Book: ")
    title = get_valid_text("Title")
    author = get_valid_text("Author")
    isbn = get_valid_isbn()
    genre = input("genre: ")
    price = get_float_number("Book Price")
    quantity = get_int_number("Book Quantity")
    publisher = get_valid_text("Publisher")
    year = get_valid_year()
    book = Book(title, author, isbn,genre, price, quantity, publisher, year)
    store.add_book(book)


def search_books(store):
    term = input("Enter Title or ISBN: ")
    books = store.search_books(term)
    print("Search Result: ")
    for book in books:
        print(book)

def remove_book(store):
    isbn = get_valid_isbn()
    is_remove = store.remove_book(isbn)
    if is_remove:
        print("Book removed successfully.")
    else:
        print("Book not found!")


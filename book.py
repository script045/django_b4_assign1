class Book:
    def __init__(self, title, author, isbn, genre, price, quantity, publisher=None, year=None):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.price = price
        self.quantity = quantity
        self.publisher = publisher
        self.year = year

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Genre: {self.genre}, Price: {self.price}, Quantity: {self.quantity}, Publisher: {self.publisher}, Year: {self.year}"

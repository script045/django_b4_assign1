from method import add_book, search_books, remove_book
from store import Store


def menu():
    print( """
    Book Store Management
    1. Add Book
    2. View Books
    3. Search Books(Title or ISBN only)
    4. Remove Book
    0: Exit
    """)


def main():
    store = Store()
    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_book(store)
        elif choice == "2":
            store.view_books()
        elif choice == "3":
            search_books(store)
        elif choice == "4":
            remove_book(store)
        elif choice == "0":
            store.save_book()
            print("Thank You for Using!")
            break
        else:
            print("Invalid choice. Please Input Correct Choice")


if __name__ == "__main__":
    main()
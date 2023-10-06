# Определяем класс Book
class Book:
    def __init__(self, title, author):
        self.title = title  # Атрибут: название книги
        self.author = author  # Атрибут: автор книги
        self.checked_out = False  # Атрибут: флаг, указывающий, взята ли книга

    def checkout(self):

        if not self.checked_out:
            self.checked_out = True
            print(f"The book '{self.title}' has been checked out.")
        else:
            print(f"The book '{self.title}' is already checked out.")

    def return_book(self):

        if self.checked_out:
            self.checked_out = False
            print(f"The book '{self.title}' has been returned.")
        else:
            print(f"The book '{self.title}' is not checked out.")

# Определяем класс Library
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(f"'{book.title}' by {book.title}")

    def checkout_book(self, title):
        for book in self.books:
            if book.title == title:
                book.checkout()
                return

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.return_book()
                return

# Создаём экземпляр класса Library
library = Library()

# Добавляем книги в библиотеку
library.add_book("The Catcher in the Rye", "J.D. Salinger")
library.add_book("To Kill a Mockingbird", "Harper Lee")

# Выводим список книг в библиотеке
library.list_books()

# Берём книгу из библиотеки и возвращаем её через библиотеку
library.checkout_book("The Catcher in the Rye")
library.return_book("The Catcher in the Rye")

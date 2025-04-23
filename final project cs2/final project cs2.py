from abc import ABC, abstractmethod
from typing import List

# Abstract base class
class Person(ABC):
    def __init__(self, name: str, email: str):
        self._name = name
        self._email = email

    @abstractmethod
    def get_role(self) -> str:
        pass

class Author(Person):
    def __init__(self, name: str, email: str, biography: str):
        super().__init__(name, email)
        self._biography = biography

    def get_role(self) -> str:
        return "Author"

class Member(Person):
    def __init__(self, name: str, email: str, member_id: int):
        super().__init__(name, email)
        self._member_id = member_id
        self._borrowed_books: List['Book'] = []

    def borrow_book(self, book: 'Book'):
        self._borrowed_books.append(book)

    def get_borrowed_books(self) -> List['Book']:
        return self._borrowed_books

    def get_role(self) -> str:
        return "Member"

class Librarian(Person):
    def __init__(self, name: str, email: str, employee_id: int):
        super().__init__(name, email)
        self._employee_id = employee_id

    def get_role(self) -> str:
        return "Librarian"


class Book:
    def __init__(self, title: str, isbn: str, author: Author):
        self._title = title
        self._isbn = isbn
        self._author = author

class EBook(Book):
    def __init__(self, title: str, isbn: str, author: Author, file_format: str):
        super().__init__(title, isbn, author)
        self._file_format = file_format

class PrintedBook(Book):
    def __init__(self, title: str, isbn: str, author: Author, pages: int):
        super().__init__(title, isbn, author)
        self._pages = pages


class Library:
    def __init__(self, name: str):
        self._name = name
        self._books: List[Book] = []
        self._members: List[Member] = []
        self._librarians: List[Librarian] = []

    def add_book(self, book: Book):
        self._books.append(book)

    def add_member(self, member: Member):
        self._members.append(member)

    def add_librarian(self, librarian: Librarian):
        self._librarians.append(librarian)

    def get_books(self) -> List[Book]:
        return self._books

class LibraryCard:
    def __init__(self, card_number: int, member: Member):
        self._card_number = card_number
        self._member = member
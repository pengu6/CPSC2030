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
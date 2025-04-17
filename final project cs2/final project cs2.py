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

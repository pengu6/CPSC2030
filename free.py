'''from abc import ABC, abstractmethod

class SpaceStation(ABC):
    @abstractmethod
    def dock_ship(self, name, cargo):
        pass
    
    def get_station_status(self):
        pass
    
class Battery:
    def __init__(self):
        self.charge = 100

class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()

    def charge(self):
        self.battery = Battery()

    

c = Car()
c.charge()'


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Course:
    def __init__(self, name, students):
        self.name = name
        self.students = students

students = {
    Student("Alice", 18),
    Student("Bob", 19),
    Student("Tommy", 20),
}

course = Course("OOP", students)'
'''

class Book:
    def __init__(self, title):
        self.title = title

class Library:
    def __init__(self, books = []):
        self.books = books
        self.book_count = len(books)

    def chekcout(self, book):
        self.books.remove(book)

    def return_book(self, book):
        self.books.append(book)

        
b = Book("Lord of The Rings")
l = Library([b])
assert len(l.books) == 1
l.chekcout(b)   
assert len(l.books) == 0 
l.return_book(b)
assert l.books[0] ==b
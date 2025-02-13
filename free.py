'''class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi my name is {self.name} and I am {self.age} years old!")

connor = Person("Connor", 18)
noah = Person("Noah", 18)

connor.introduce()
noah.introduce()

class Rectangle:

    def __init__(self, width, height):
        self._width = width
        self._height = height

    def area(self):
        return self._width * self._height
    
    def perimiter(self):
        return self._width *2 + self._height *2
        

r = Rectangle(6, 9)
print(r.area())


class Person:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
       return self._name
    
    @name.deleter
    def name(self):
        del self._name

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return str((self.x , self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def mag(self):
        return (self.x**2 + self.y**2)**.5
    
    def __lt__(self, other):
        return self.mag() < other.mag()

v1 = Vector(2,4)
v2 = Vector(3,6)
'''

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def drive(self):
        return f"Driving {self.brand} car."

class Bike(Vehicle):
    def drive(self):
        return f"Pedaling{self.brand} bike."

class ElectricCar(Car):
    def drive(self):
        return f"Silently driving {self.brand} car."

class SportsCar(Car):
    pass

class Electric:
    def charge(self):
        return "Charging..."
    

class Zoo:
    def __init__(self):
        self.employees = []
        self.animals = []
        self.guests = []

class Person:
    def __init__(self, name):
        self. _name = name
    
    def __repr__(self):
        return self._name
    
class Employee(Person):
    def __init__(self, name):
        super().__init__(name)
        self.food = 20

    def feed(self,animal):
        animal.hunger -=1
        self.food -=1

class Animal:
    def __init__(self, species):
        self.species = species
        self._hunger = 10
    
    def feed(self, amount):
        self._hunger -= amount

class Carnivore(Animal):
    pass

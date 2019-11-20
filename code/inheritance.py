"""Inheritance in Python"""


# Single Inhertance
class Animal:
    def __init__(self):
        self.is_animal = True


class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.barks = True


a = Animal()
d = Dog()
print(d.is_animal)
print(d.barks)


# Multiple Inheritance


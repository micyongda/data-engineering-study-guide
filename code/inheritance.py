"""Inheritance in Python"""


"""
Single Inheritance -
    A derived class acquires the members of a single super class.
"""
class Animal:
    def __init__(self):
        self.is_animal = True


class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.barks = True


a = Animal()
d = Dog()
assert a.is_animal 
assert d.barks 


"""
Multiple Inheritance - 
    A derived class is inherited from more than one base class.
"""
class Cat:
    pass 

class Dog:
    pass 

class Animal(Cat, Dog):
    pass

a = Animal()
print(dir(a))


"""
MultiLevel Inheritance - 
    A derived class inherits from a base class who interits from another base class. 
"""
class Animal:
    pass

class Dog(Animal):
    pass 

class Chihuahua(Dog):
    pass 

"""
Hierarchical Inheritance - 
    From one base class you can inherit any number of child classes
"""

class Car:
    def __init__(self):
        self.drives = True

class SUV(Car):
    def __init__(self):
        super().__init__()
        self.weight = random.randrange(4000,5000)

class Sedan(Car):
    def __init__(self):
        super().__init__()
        self.weight = random.randrange(2000,4000)

class Truck(Car):
    def __init__(self):
        super().__init__()
        self.weight = random.randrange(4500,5500)
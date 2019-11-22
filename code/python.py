"""4 Key Features of Python"""

# 1. Python is an interpreted language. 
# That means that it does not need to be compiled before it's run. 
python3 run.py
javac run.java; java run

# 2. Python is dynamically typed. 
# You don't have to state the types of variables when declaring them
x = "I'm a string"
x = 12
# Happens without error 

# 3. Python is well suited for object oriented programming. 
# It allows the definition of classes and along with composition and inheritance
# Does not have access specifiers like C++'s public and private members

# 4. Functions are first-class objects. 
def num():
    return 23
# This means that they can be assigned to variables, 
x = num() 
# passed into other functions, 
y = range(1, num())
# and returned from other functions. 
def call_num():
    return num()
z = call_num()
# Classes are also first class objects. 


"""Indentation"""

for i in range(0, 15):
    # indentation required 

def hello():
    # indentation required 

class Person:
    # indentation required
    # 4 spaces

def fails():
 print("This will throw an error because of faulty indentation")


"""Arrays vs Lists"""

from array import array 

arr = array('i', [1, 2, 3, 4])
lst = ["Hello", 1, 2.0]


"""Functions"""

def newfunc():
    # code . . .
    print("Hi")

# only gets executed when it is called
newfunc()

"""init"""
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age 
        self.salary = salary

E1 = Employee("XYZ", 23, 20000)
# E1 is the instance of class Employee 
# __init__ allocates memory for E1

"""Self"""
class Person:
    def __init__(self):
        self.gender = "Male"
        self.miles_walked = 0

    def walked(self, miles_walked):
        self.miles_walked += miles_walked
        return self.miles_walked


"""PYTHONPATH"""

# When module is imported, the interpreter searches for a built-in module with the same name 
# Then it checks sys.path for that module.
# sys.path is initialized from 
# 1) current working directory 
# 2) the directories defined in PYTHONPATH,
# 3) the installation-dependent default
# ex: sys.path = ['', '/Library/../python3.zip, '/Desktop/goodbye']

# PYTHONPATH is an environment variable that is used when a module is imported.
# PYTHONPATH is also looked up to check the presence of imported modules in various directories. 
# PYTHONPATH is just a list of directory names (colon separated just like PATH)
# The interpreter uses it to determine which module to load.
'SET PYTHONPATH' -> adds path to module to sys.path [] -> import mod_a -> check sys.path -> success!
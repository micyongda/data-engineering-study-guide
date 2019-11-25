## Questions from data engineering cookbook and other website
73. What Is The Output Of The Following Python Code Fragment? Justify Your Answer.
```
def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

print "list1 = %s" % list1
print "list2 = %s" % list2
print "list3 = %s" % list3
```
The result of the above Python code snippet is: 
```
list1 = [10, 'a']
list2 = [123]
list3 = [10, 'a']
```
You may erroneously expect list1 to be equal to [10] and list3 to match with [‘a’], thinking that the list argument will initialize to its default value of [] every time there is a call to the extendList.

However, the flow is like that a new list gets created once after the function is defined. And the same get used whenever someone calls the extendList method without a list argument. It works like this because the calculation of expressions (in default arguments) occurs at the time of function definition, not during its invocation.

The list1 and list3 are hence operating on the same default list, whereas list2 is running on a separate object that it has created on its own (by passing an empty list as the value of the list parameter).

The definition of the extendList function can get changed in the following manner.

```
def extendList(val, list=None):
  if list is None:
    list = []
  list.append(val)
  return list
```
With this revised implementation, the output would be:
```
list1 = [10]
list2 = [123]
list3 = ['a']
```

74. What are decorators in python and when is it Uused?

Python decorator is a relative change that you do in Python syntax to adjust the functions quickly.

Python decorator gives us the ability to add new behavior to the given objects dynamically. In the example below, we’ve written a simple example to display a message pre and post the execution of a function.

```
def decorator_sample(func):
    def decorator_hook(*args, **kwargs):
        print("Before the function call")
        result = func(*args, **kwargs)
        print("After the function call")
        return result
    return decorator_hook

@decorator_sample
def product(x, y):
    "Function to multiply two numbers."
    return x * y

print(product(3, 3))
```

The output is: 
```
Before the function call
After the function call
9
```

75. How Do You Handle Exceptions With Try/Except/Finally In Python?

Python lay down Try, Except, Finally constructs to handle errors as well as Exceptions. We enclose the unsafe code indented under the try block. And we can keep our fall-back code inside the except block. Any instructions intended for execution last should come under the finally block.

76. What Is Slicing In Python?

Slicing is a string operation for extracting a part of the string, or some part of a list. In Python, a string (say text) begins at index 0, and the nth character stores at position text[n-1]. Python can also perform reverse indexing, i.e., in the backward direction, with the help of negative numbers. In Python, the slice() is also a constructor function which generates a slice object. The result is a set of indices mentioned by range(start, stop, step). The slice() method allows three parameters. 1. start – starting number for the slicing to begin. 2. stop – the number which indicates the end of slicing. 3. step – the value to increment after each index (default = 1).

77. Is A String Immutable Or Mutable In Python?

Python strings are indeed immutable.

Let’s take an example. We have an “str” variable holding a string value. We can’t mutate the container, i.e., the string, but can modify what it contains that means the value of the variable.

78. How are arguments passed by value or by reference?

In call-by-value, the argument whether an expression or a value gets bound to the respective variable in the function.

Python will treat that variable as local in the function-level scope. Any changes made to that variable will remain local and will not reflect outside the function.

We use both “call-by-reference” and “pass-by-reference” interchangeably. When we pass an argument by reference, then it is available as an implicit reference to the function, rather than a simple copy. In such a case, any modification to the argument will also be visible to the caller.

This scheme also has the advantage of bringing more time and space efficiency because it leaves the need for creating local copies.

On the contrary, the disadvantage could be that a variable can get changed accidentally during a function call. Hence, the programmers need to handle in the code to avoid such uncertainty.

79. What Does The Join Method Do In Python?

Python provides the join() method which works on strings, lists, and tuples. It combines them and returns a united value.

80. What Is Composition In Python?

The composition is also a type of inheritance in Python. It intends to inherit from the base class but a little differently, i.e., by using an instance variable of the base class acting as a member of the derived class.

81. What Are The Optional Statements Possible Inside A Try-Except Block In Python?

There are two optional clauses you can use in the try-except block.

The “else” clause
It is useful if you want to run a piece of code when the try block doesn’t create an exception.
The “finally” clause
It is useful when you want to execute some steps which run, irrespective of whether there occurs an exception or not.

82. What is the difference between an object and a class?

Objects are an encapsulation of variables and functions into a single entity. Objects get their variables and functions from classes. Classes are essentially a template to create your objects.

83. How can you share global variables across modules?

The canonical way to share information across modules within a single program is to create a special configuration module (often called config or cfg). Just import the configuration module in all modules of your application; the module then becomes available as a global name. Because there is only one instance of each module, any changes made to the module object get reflected everywhere.
```
#config.py
x = 0   # Default value of the 'x' configuration setting

#mod.py
import config
config.x = 1

#main.py
import config
import mod
print config.x
```

Module variables are also often used to implement the Singleton design pattern, for the same reason.

84. What Is The Set Object In Python?

Sets are unordered collection objects in Python. They store unique and immutable objects. Python has its implementation derived from mathematics.

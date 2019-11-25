# 100 Python Interview Questions

### Basic Python Questions 

1. What is the difference between list and tuples in Python?

2. What are the key features of Python?

3. What type of language is python? Programming or Scripting? 

4. How is Python an interpreted language?

5. What is pep 8?

6. How is memory managed in Python?

7. What is name space in Python?

8. What is PYTHON PATH?

9. What are python modules? Name some commonly used built-in modules in python?

10. What are local variables and global variables in Python?

11. Is python case sensitive?

12. What is type conversion in Python?

13. How to install Python on Windows and set path variable?

14. Is indentation required in python?

15. What is the difference between Python Arrays and lists?

16. What are functions in Python?

17. What is __init__?

18. What is a lambda function?

19. What is self in Python?

20. How does break, continue and pass work?

21. What does [::-1] do?

22. How can you randomize the items of a list in place in Python?

23. What are python iterators?

24. How can you generate random numbers in Python?

25. What is the difference between range & xrange?

26. How do you write comments in python?

27. What is pickling and unpickling?

28. What are the generators in python?

29. How will you capitalize the first letter of string?

30. How will you convert a string to all lowercase?

31. How to comment multiple lines in python?

32. What are docstrings in Python?

33. What is the purpose of is, not and in operators?

34. What is the usage of help() and dir() function in Python?

35. Whenever Python exits, why isn’t all the memory de-allocated?

36. What is a dictionary in Python?

37. How can the ternary operators be used in python?

38. What does this mean: *args, **kwargs? And why would we use it?

39. What does len() do?

40. Explain split(), sub(), subn() methods of “re” module in Python.

41. What are negative indexes and why are they used?

42. What are Python packages?

43. How can files be deleted in Python?

44. What are the built-in types of python?

45. What advantages do NumPy arrays offer over (nested) Python lists?

46. How to add values to a python array?

47. How to remove values to a python array?

48. Does Python have OOps concepts?

49. What is the difference between deep and shallow copy?

50. How is Multithreading achieved in Python?

51. What is the process of compilation and linking in python?

52. What are Python libraries? Name a few of them.

53. What is split used for?

54. How to import modules in python?

### Object Oriented Questions
55. Explain Inheritance in Python with an example.

56. How are classes created in Python? 

57. What is monkey patching in Python?

58. Does python support multiple inheritance?

59. What is Polymorphism in Python?

60. Define encapsulation in Python?

61. How do you do data abstraction in Python?

62. Does python make use of access specifiers?

63. How to create an empty class in Python? 

64. What does an object() do?

### Basic Python Programs 
65. Write a function in Python to execute the Bubble sort algorithm.

66. Write a function in Python to produce Star triangle.

67. Write a function to produce Fibonacci series in Python.

68. Write a function in Python to check if a number is prime.

69. Write a function in Python to check if a sequence is a Palindrome.

70. Write a one-liner that will count the number of capital letters in a file. Your code should work even if the file is too big to fit in memory.

71. Write a sorting algorithm for a numerical dataset in Python.

72. Looking at the below code, write down the final values of A0, A1, …An.
```
A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]
print(A0,A1,A2,A3,A4,A5,A6)
```

73 - 84 
### Questions from data engineering cookbook and other website
73. What is the difference between an object and a class

74. Explian Immutability 

75. What is the difference between args and kwargs? 

76. How to reverse a linked list? 

77. What's the difference between a library, framework, and package? 

78. What's the difference between OOP and functional programming? 

79. What are Python decorators?

80. How are arguments passed by value or by reference?

81. How can you share global variables across modules?

82. Why lambda forms in python does not have statements?

83. What is unittest in Python?

84. What are generators in Python?

### Data Analysis Python Interview Questions
85. What is map function in Python?

86. Is python numpy better than lists?

87. How to get indices of N maximum values in a NumPy array?

88. How do you calculate percentiles with Python/ NumPy?

89. What is the difference between NumPy and SciPy?

90. How do you make 3D plots/visualizations using NumPy/SciPy?

### Multiple Choice 

91. Which of the following statements create a dictionary? (Multiple Correct Answers Possible)
```
a) d = {}
b) d = {“john”:40, “peter”:45}
c) d = {40:”john”, 45:”peter”}
d) d = (40:”john”, 45:”50”)
```
92. Which one of these is floor division?
```
a) /
b) //
c) %
d) None of the mentioned
```
93. What is the maximum possible length of an identifier?
```
a) 31 characters
b) 63 characters
c) 79 characters
d) None of the above
```
94. Why are local variable names beginning with an underscore discouraged?
```
a) they are used to indicate a private variables of a class
b) they confuse the interpreter
c) they are used to indicate global variables
d) they slow down execution
```
95. Which of the following is an invalid statement?
```
a) abc = 1,000,000
b) a b c = 1000 2000 3000
c) a,b,c = 1000, 2000, 3000
d) a_b_c = 1,000,000
```
96. What is the output of the following?
```
try:
    if '1' != 1:
        raise "someError"
    else:
        print("someError has not occured")
except "someError":
    print ("someError has occured")

a) someError has occured
b) someError has not occured
c) invalid code
d) none of the above
```
97. Suppose list1 is [2, 33, 222, 14, 25], What is list1[-1] ?

```
a) Error
b) None
c) 25
d) 2
```
98. To open a file c:scores.txt for writing, we use
```
a) outfile = open(“c:scores.txt”, “r”)
b) outfile = open(“c:scores.txt”, “w”)
c) outfile = open(file = “c:scores.txt”, “r”)
d) outfile = open(file = “c:scores.txt”, “o”)
```
99. What is the output of the following?
```
f = None
 
for i in range (5):
    with open("data.txt", "w") as f:
        if i > 2:
            break
 
print f.closed

a) True
b) False
c) None
d) Error
```
100. When will the else part of try-except-else be executed?
```
a) always
b) when an exception occurs
c) when no exception occurs
d) when an exception occurs into except block
```

# Links to Answers
* Questions 1-72 85-100: (https://www.edureka.co/blog/interview-questions/python-interview-questions/)
* Questions 73-78: (https://www.youtube.com/watch?v=WbqRH2r3N40&feature=youtu.be)
* 79-84: (https://www.guru99.com/python-interview-questions-answers.html)

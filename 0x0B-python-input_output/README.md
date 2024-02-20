Write a function that writes a string to a text file (UTF8) and returns the number of characters written:

Prototype: def write_file(filename="", text=""):
You must use the with statement
You don’t need to manage file permission exceptions.
Your function should create the file if doesn’t exist.
Your function should overwrite the content of the file if it already exists.
You are not allowed to import any module


Write a function that reads a text file (UTF8) and prints it to stdout:

Prototype: def read_file(filename=""):
You must use the with statement
You don’t need to manage file permission or file doesn't exist exceptions.
You are not allowed to import any module

Write a function that returns the JSON representation of an object (string):
● Prototype: def to_json_string(my_obj):
● You don’t need to manage exceptions if the object can’t be serialized.

Write a function that returns an object (Python data structure) represented by a JSON string:
● Prototype: def from_json_string(my_str):
● You don’t need to manage exceptions if the JSON string doesn’t represent an object.

Write a function that writes an Object to a text file, using a JSON representation:
● Prototype: def save_to_json_file(my_obj, filename)
● You must use the with statement
● You don’t need to manage exceptions if the object can’t be serialized.
● You don’t need to manage file permission exceptions.

Write a function that creates an Object from a “JSON file”:
● Prototype: def load_from_json_file(filename):
● You must use the with statement
● You don’t need to manage exceptions if the JSON string doesn’t represent an object.
● You don’t need to manage file permissions / exceptions.

Write a function that returns the dictionary description with simple data structure (list,
dictionary, string, integer and boolean) for JSON serialization of an object:
● Prototype: def class_to_json(obj):
● obj is an instance of a Class
● All attributes of the obj Class are serializable: list, dictionary, string, integer and
boolean
● You are not allowed to import any module

Write a class Student that defines a student by:
● Public instance attributes:
○ first_name
○ last_name
○ age
● Instantiation with first_name, last_name and age: def __init__(self,
first_name, last_name, age):
● Public method def to_json(self): that retrieves a dictionary representation of a
Student instance (same as 8-class_to_json.py)
● You are not allowed to import any module

Write a class Student that defines a student by:
Public instance attributes:
first_name
last_name
age
Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py):
If attrs is a list of strings, only attribute names contained in this list must be retrieved.
Otherwise, all attributes must be retrieved


Write a class Student that defines a student by: (based on 10-student.py)

Public instance attributes:
first_name
last_name
age
Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py):
If attrs is a list of strings, only attributes name contain in this list must be retrieved.
Otherwise, all attributes must be retrieved
Public method def reload_from_json(self, json): that replaces all attributes of the Student instance:
You can assume json will always be a dictionary
A dictionary key will be the public attribute name
A dictionary value will be the value of the public attribute
You are not allowed to import any module



Write a class Student that defines a student by: (based on 10-student.py)

Public instance attributes:
first_name
last_name
age
Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py):
If attrs is a list of strings, only attributes name contain in this list must be retrieved.
Otherwise, all attributes must be retrieved
Public method def reload_from_json(self, json): that replaces all attributes of the Student instance:
You can assume json will always be a dictionary
A dictionary key will be the public attribute name
A dictionary value will be the value of the public attribute
You are not allowed to import any module



Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:

Prototype: def append_write(filename="", text=""):
If the file doesn’t exist, it should be created
You must use the with statement
You don’t need to manage file permission or file doesn't exist exceptions.
You are not allowed to import any module

Pascal's Triangle
Technical interview preparation:

You are not allowed to google anything
Whiteboard first
Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:
Returns an empty list if n <= 0
You can assume n will be always an integer
You are not allowed to import any module

EXPLANATION OF PASCALS TRIANGLE
--------------------------------
It is a fascinating mathematical pattern
It has applications in Probability Theory, Algebra, Combinatorics

A Pascal's triangle is a triangular array of numbers

Each number in the triangle represents a binomial coefficient, nCr
n is the row number starting from 0
r is the position within the row

Named after the French Mathematician Blaise Pascal
However it was known to other mathematicians centuries before him

How do we construct it:
------------------------
Topmost row is row 0
Contains a single non zero entity 1
[1]

Each subsequent row is constructed by adding adjacent numbers from the above row

The second row, row 1, has two entries, 1 and 1 [1, 1] ie 0 + 1

The 3rd row, row 2. will have [1, 2, 1]

The entry in the ith row and jth column of a Pascals triangle is denoted as C(i,j)

This represents the value of nCr
	n is the row number 
	r is the position within the row
Formulae for binomial coeffaicients: C(i, j) = n! / (r! * (i - r)!)

Helps calculate combinations, probabilities, permutations

Used in algebraic expansions such as the binomail theorem

It has fascinating patterns related to number theory



Write a function that inserts a line of text to a file, after each line containing a specific string (see example):
Prototype: def append_after(filename="", search_string="", new_string=""):
You must use the with statement
You don’t need to manage file permission or file doesn't exist exceptions.
You are not allowed to import any module


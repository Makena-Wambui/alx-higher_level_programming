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

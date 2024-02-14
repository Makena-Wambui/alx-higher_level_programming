--------------------Learning Objectives---------------------------
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
Why Python programming is awesome
What is an object
What is the difference between a class and an object or instance
What is the difference between immutable object and mutable object
What is a reference
What is an assignment
What is an alias
How to know if two variables are identical
How to know if two variables are linked to the same object
How to display the variable identifier (which is the memory address in the CPython implementation)
What is mutable and immutable
What are the built-in mutable types
What are the built-in immutable types
How does Python pass variables to functions

WHAT IS AN OBJECT?
------------------
An object is something a variable can refer to.
Variables dont have an associated type or size,
since they are names or labels attched to objects in memory.
Do not think of variables as boxes, rather think of them as labels.
Variables point to a memory position where concrete objects live
A variable is a name that refers to or holds a reference to a concrete object.
Python objects are concrete pieces of information that live in specific memory locations 
on your computer.

In summary:
A variable holds a reference to an object
An object lives in a concrete memory position.

0. Who am I?
What function would you use to get the type of an object?

Write the name of the function in the file, without ()


1. Where are you?
How do you get the variable identifier (which is the memory address in the CPython implementation)?

Write the name of the function in the file, without ().

2. Right count
In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = 100


3. Right count =
In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = 89


4. Right count =
In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = a

5. Right count =+
In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = a + 1

6. Is equal
What do these 3 lines print?

>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)

7. Is the same
What do these 3 lines print?

>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)

8. Is really equal
What do these 3 lines print?

>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)

9. Is really the same
What do these 3 lines print?

>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)

10. And with a list, is it equal
What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)

11. And with a list, is it the same
What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)

12. And with a list, is it really equal

What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)


13. And with a list, is it really the same
What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)

14. List append
What does this script print?

l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)

14. List append
What does this script print?

l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)

EXPLANATION
------------
When you assign l1 to l2, l1 and l2 ow both have the same value.
And both names both refer to the same object in memory.
As in they are aliases for the same list object.
Any changes made to one alias will reflect in the other.
When you append to l1, you are modifying the existing list, ie the one pointed to by both l1 and l2.


15. List add
What does this script print?

l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)

EXPLANATION
------------
By doing this: l1 = l1 + [4]
we are creating a new list by concatenating an existing list, l1
with [4]
the newly created list is stored in the variable l1
l2 stil points to the original [1, 2, 3]
It remains unaffected.
while l1 now points to anew list.
So + operator creates a new list

Mutating methods like append() modify the existing list,
affecting all aliases.
Reassignment like l1 = l1 + [4] creates a new list,
leaving other aliases unchanged.

21. Tuple or not?
a = (1, 2)
Is a a tuple? Answer with Yes or No.

22. Tuple or not?
a = (1)
Is a a tuple? Answer with Yes or No.

23. Tuple or not?

a = (1, )
Is a a tuple? Answer with Yes or No.

24. Who I am?

What does this script print?

a = (1)
b = (1)
a is b

25. Tuple or not

What does this script print?

a = (1, 2)
b = (1, 2)
a is b

26. Empty is not empty
What does this script print?

a = ()
b = ()
a is b

27. Still the same?
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
Will the last line of this script print 139926795932424? Answer with Yes or No.

28. Same or not?

>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
Will the last line of this script print 139926795932424? Answer with Yes or No.



16. Integer incrementation

What does this script print?

def increment(n):
    n += 1

a = 1
increment(a)
print(a)

QUESTION
---------
julien@twix:/tmp/so$ cat int.py 
print("I")
print("Love")
print("Python")
julien@ubuntu:/tmp/so$ 
Assuming we are using a CPython implementation of Python3 with default options/configuration:

Before the execution of line 2 (print("Love")), how many int objects have been created and are still in memory? (105-line1.txt)
Why? (optional blog post :))


QUESTION
---------
julien@ubuntu:/python3$ cat int.py 
a = 1024
b = 1024
del a
del b
c = 1024
julien@ubuntu:/python3$ 
Assuming we are using a CPython implementation of Python3 with default options/configuration:

How many int objects are created by the execution of the first line of the script? (104-line1.txt)
How many int objects are created by the execution of the second line of the script (104-line2.txt)
After the execution of line 3, is the int object pointed by a deleted? Answer with Yes or No (104-line3.txt)
After the execution of line 4, is the int object pointed by b deleted? Answer with Yes or No (104-line4.txt)
How many int objects are created by the execution of the last line of the script (104-line5.txt)



QUESTION
----------
julien@ubuntu:/python3$ cat int.py 
a = 1
b = 1
julien@ubuntu:/python3$ 
Assuming we are using a CPython implementation of Python3 with default options/configuration:

How many int objects are created by the execution of the first line of the script? (103-line1.txt)
How many int objects are created by the execution of the second line of the script (103-line2.txt)

QUESTION
----------
Write a class LockedClass with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called first_name.

You are not allowed to import any module


QUESTION
------------
Write a function magic_string() that returns a string “BestSchool” n times the number of the iteration (see code):


Your file should be maximum 4-line long (no documentation needed)
You are not allowed to import any module

------EXPLAINED------
Create an attribute count on the function magic string.
Then use the getattr function to retrieve the value of magic_string.count
if it doesnt exist, it defaults to 0.
if it exists,
1 is added to increment the count.
Then we create a list ['BestSchool'] multiplied by count attribute
join returns a string.
Specify separator as ", "



What does this script print?
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)



What does this script print?
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)


19. Copy a list object
Write a function def copy_list(l): that returns a copy of a list.
The input list can contain any type of objects
Your file should be maximum 3-line long (no documentation needed)
You are not allowed to import any module

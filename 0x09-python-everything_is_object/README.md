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

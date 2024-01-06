#!/usr/bin/python3
class A:
    a = "I am a class attribute."


x = A()
y = A()
# print(x.a)
# print(y.a)
# print(A.a)

# let us create a new instance attribute for x
x.a = "This is a new instance attribute for x."
# print(y.a)
# print(A.a)

# let us change the class attribute a
A.a = "This is how you change the class attribute."
print(y.a)
print(A.a)

print(x.a)

print(x.__dict__)
print(y.__dict__)
print(A.__dict__)
print(x.__class__.__dict__)

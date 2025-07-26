Python - Everything is Object
This repository contains the answers to questions regarding Python's handling of objects, including mutable and immutable types, as well as how objects are passed to functions and the distinction between variables and memory addresses.

Task 0: Who am I?
Question: What function would you use to print the type of an object?
Answer: type

Task 1: Where are you?
Question: How do you get the variable identifier (which is the memory address in the CPython implementation)?
Answer: id

Task 2: Right count
Question: In the following code, do a and b point to the same object?

python
Copy
>>> a = 89
>>> b = 100
Answer: No

Task 3: Right count =
Question: In the following code, do a and b point to the same object?

python
Copy
>>> a = 89
>>> b = 89
Answer: Yes

Task 4: Right count =
Question: In the following code, do a and b point to the same object?

python
Copy
>>> a = 89
>>> b = a
Answer: Yes

Task 5: Right count =+
Question: In the following code, do a and b point to the same object?

python
Copy
>>> a = 89
>>> b = a + 1
Answer: No

Task 6: Is equal
Question: What do these 3 lines print?

python
Copy
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
Answer: True

Task 7: Is the same
Question: What do these 3 lines print?

python
Copy
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
Answer: True

Task 8: Is really equal
Question: What do these 3 lines print?

python
Copy
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)
Answer: True

Task 9: Is really the same
Question: What do these 3 lines print?

python
Copy
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)
Answer: True

Task 10: And with a list, is it equal
Question: What do these 3 lines print?

python
Copy
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
Answer: True

Task 11: And with a list, is it the same
Question: What do these 3 lines print?

python
Copy
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
Answer: No

Task 12: And with a list, is it really equal
Question: What do these 3 lines print?

python
Copy
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
Answer: True

Task 13: And with a list, is it really the same
Question: What do these 3 lines print?

python
Copy
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
Answer: True

Task 14: List append
Question: What does this script print?

python
Copy
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
Answer: [1, 2, 3, 4]

Task 15: List add
Question: What does this script print?

python
Copy
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
Answer: [1, 2, 3]

Task 16: Integer incrementation
Question: What does this script print?

python
Copy
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
Answer: 1

Task 17: List incrementation
Question: What does this script print?

python
Copy
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
Answer: [1, 2, 3, 4]

Task 18: List assignation
Question: What does this script print?

python
Copy
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
Answer: [1, 2, 3]

Task 19: Copy a list object
Question: Write a function copy_list(a_list) that returns a copy of a list.
Answer:

python
Copy
def copy_list(a_list):
    return a_list[:]
Task 20: Tuple or not?
Question: Is a = () a tuple?
Answer: Yes

Task 21: Tuple or not?
Question: Is a = (1, 2) a tuple?
Answer: Yes

Task 22: Tuple or not?
Question: Is a = (1) a tuple?
Answer: No

Task 23: Tuple or not?
Question: Is a = (1,) a tuple?
Answer: Yes

Task 24: Who I am?
Question: What does this script print?

python
Copy
a = (1)
b = (1)
a is b
Answer: False

Task 25: Tuple or not
Question: What does this script print?

python
Copy
a = (1, 2)
b = (1, 2)
a is b
Answer: False

Task 26: Empty is not empty
Question: What does this script print?

python
Copy
a = ()
b = ()
a is b
Answer: True

Task 27: Still the same?
Question: Will the last line of this script print 139926795932424?

python
Copy
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
Answer: No

Task 28: Same or not?
Question: Will the last line of this script print 139926795932424?

python
Copy
>>> a
[1, 2, 3]
>>> id(a)
139926795932424
>>> a += [4]
>>> id(a)
Answer: Yes

Task 29: Python3: Mutable, Immutable... everything is object!
Write a blog post about everything you just learned.


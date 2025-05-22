📐 0x06. Python - Classes and Objects
This project is part of the Holberton School Higher Level Programming curriculum. It introduces the concept of classes and objects in Python, with a focus on encapsulation, validation, properties, and basic methods like printing and computing the area of a square.

📁 Project Structure
markdown
Copy code
holbertonschool-higher_level_programming/
└── python-classes/
    ├── 0-square.py
    ├── 1-square.py
    ├── 2-square.py
    ├── 3-square.py
    ├── 4-square.py
    ├── 5-square.py
    ├── 6-square.py
    └── ...
📚 Learning Objectives
By the end of this project, you will be able to:

Understand the concept of object-oriented programming in Python

Create and use classes and objects

Understand the difference between class and instance attributes

Use __init__ and define methods

Understand and implement getters/setters using @property

Handle input validation and raise exceptions

Customize how objects are printed using my_print

🧠 Tasks Overview
🔹 0. My First Square
Create an empty class Square.

python
Copy code
class Square:
    pass
🔹 1. Square with Size
Add a private attribute __size.

Instantiate with size, no validation yet.

python
Copy code
def __init__(self, size):
    self.__size = size
🔹 2. Size Validation
Validate that size:

Must be an int → raise TypeError

Must be >= 0 → raise ValueError

python
Copy code
if not isinstance(size, int):
    raise TypeError("size must be an integer")
if size < 0:
    raise ValueError("size must be >= 0")
🔹 3. Area of a Square
Add area() method to return size * size.

python
Copy code
def area(self):
    return self.__size ** 2
🔹 4. Access and Update Private Attribute
Use property decorators to access and modify size.

python
Copy code
@property
def size(self):
    return self.__size

@size.setter
def size(self, value):
    # validate value before setting
🔹 5. Printing a Square
Add my_print() method to display the square using #.

python
Copy code
def my_print(self):
    if self.__size == 0:
        print("")
    else:
        for _ in range(self.__size):
            print("#" * self.__size)
🔹 6. Coordinates of a Square
Add position as a private attribute (a tuple of 2 positive integers).

Modify my_print() to respect position when printing.

python
Copy code
def my_print(self):
    if self.__size == 0:
        print()
        return
    print("\n" * self.__position[1], end="")
    for _ in range(self.__size):
        print(" " * self.__position[0] + "#" * self.__size)

🚫 Constraints
No imports allowed

Code must follow PEP8

Validations and exceptions must follow the exact specifications

🏁 Author
Ahmed Dawwari

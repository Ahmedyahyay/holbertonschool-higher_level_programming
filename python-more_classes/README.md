Rectangle Class in Python
This repository contains a set of Python class definitions for a Rectangle, developed as part of the Holberton School's "Python - More Classes" curriculum. Each task incrementally builds on the previous one, adding features and functionality to the Rectangle class.

📁 Directory Structure
Copy code
holbertonschool-higher_level_programming/
└── python-more_classes/
    ├── 0-rectangle.py
    ├── 1-rectangle.py
    ├── 2-rectangle.py
    ├── 3-rectangle.py
    ├── 4-rectangle.py
    ├── 5-rectangle.py
    ├── 6-rectangle.py
    ├── 7-rectangle.py
    └── README.md
🧠 Tasks Overview
0. Simple Rectangle
File: 0-rectangle.py

Description: Defines an empty Rectangle class.

No attributes or methods.

1. Real Definition of a Rectangle
File: 1-rectangle.py

Adds:

Private instance attributes: __width, __height

Property getters and setters for both

Validates that:

Width and height are integers ≥ 0

2. Area and Perimeter
File: 2-rectangle.py

Adds:

area() method: returns width * height

perimeter() method: returns 2 * (width + height) or 0 if either is 0

3. String Representation
File: 3-rectangle.py

Adds:

__str__() method: returns rectangle as a string of # characters

Returns empty string if width or height is 0

4. Eval is Magic
File: 4-rectangle.py

Adds:

__repr__() method: returns a string that can recreate the instance via eval()

5. Detect Instance Deletion
File: 5-rectangle.py

Adds:

__del__() method: prints Bye rectangle... when an instance is deleted

6. How Many Instances
File: 6-rectangle.py

Adds:

Class attribute number_of_instances

Tracks how many Rectangle objects exist

Increments/decrements on creation/deletion

7. Change Representation
File: 7-rectangle.py

Adds:

Class attribute print_symbol: used for string representation

Can be changed per instance or globally

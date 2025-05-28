📘 Python Inheritance Project
This project covers the concept of inheritance in Python, along with type checking and class validation. It’s part of the Holberton School Higher Level Programming track.

No external modules are used — only built-in Python features.

🧠 Learning Objectives
What is a subclass

How to list all attributes/methods of a class or instance

How to use isinstance() vs type()

How to build a class hierarchy with proper validation

How to override built-in methods like __str__

📂 Project Structure
0-lookup.py
🔍 Function: lookup(obj)

Returns a list of all available attributes and methods of an object.

python
Copy
Edit
def lookup(obj):
    return dir(obj)
1-my_list.py
📃 Class: MyList (inherits from list)

Adds a method print_sorted() to print the list in ascending order (without changing the original list).

2-is_same_class.py
✅ Function: is_same_class(obj, a_class)

Returns True if obj is exactly an instance of a_class (not a subclass).

3-is_kind_of_class.py
🧬 Function: is_kind_of_class(obj, a_class)

Returns True if obj is an instance of a_class or a subclass of a_class.

4-inherits_from.py
🧪 Function: inherits_from(obj, a_class)

Returns True if obj is an instance of a class that inherited (directly or indirectly) from a_class, but not if it's an instance of a_class itself.

5-base_geometry.py
📐 Class: BaseGeometry

An empty base class for geometry-related shapes.

6-base_geometry.py
🚧 Class: BaseGeometry (Improved)

Adds area() method that raises Exception: area() is not implemented.

7-base_geometry.py
📏 Class: BaseGeometry (Further Improved)

Adds integer_validator(name, value) method:

Raises TypeError if value is not an int.

Raises ValueError if value <= 0.

8-rectangle.py
🧱 Class: Rectangle (inherits from BaseGeometry)

Constructor takes width and height, which are:

Private

Validated using integer_validator

9-rectangle.py
📦 Class: Rectangle (extends 8)

Implements area()

Implements __str__ to return [Rectangle] <width>/<height>

10-square.py
🔳 Class: Square (inherits from Rectangle)

Constructor takes size, validated via integer_validator

Square is a rectangle with equal width and height

Implements area()

11-square.py
🔲 Class: Square (extends 10)

Overrides __str__ to return [Square] <width>/<height>

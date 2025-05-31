# 📘 Python ABCs, Duck Typing, and Object-Oriented Concepts

## 🔍 Overview

This project explores **object-oriented programming** concepts in Python using:

- **Abstract Base Classes (ABCs)**
- **Duck Typing**
- **Inheritance & Multiple Inheritance**
- **Mixins**
- **Built-in class extension**


---

## ✅ Task 0: Abstract Animal Class and its Subclasses

### 🔸 Objective
- Create an abstract class `Animal` using the `abc` module.
- Add an abstract method `sound()`.
- Create two subclasses:
  - `Dog`: returns `"Bark"`
  - `Cat`: returns `"Meow"`

### 💡 Key Concepts
- Abstract classes cannot be instantiated.
- Subclasses must implement all abstract methods.

### 🧪 Example

```bash
$ ./main_00_abc.py
Bark
Meow
TypeError: Can't instantiate abstract class Animal with abstract method sound
✅ Task 1: Shapes, Interfaces, and Duck Typing
🔸 Objective
Create abstract class Shape with methods area() and perimeter().

Implement:

Circle(radius)

Rectangle(width, height)

Define shape_info(shape) using duck typing to print area and perimeter.

💡 Key Concepts
Duck typing: If it quacks like a duck, treat it like one.

🧪 Example
bash
Copy code
$ ./main_01_duck_typing.py
Area: 78.53981633974483
Perimeter: 31.41592653589793
Area: 28
Perimeter: 22
✅ Task 2: Extending the Python List with Notifications
🔸 Objective
Create VerboseList that inherits from Python's built-in list.

Override:

append()

extend()

remove()

pop()

Each method prints a notification message.

💡 Key Concepts
Inherit from built-in classes.

Use super() to call original methods.

🧪 Example
bash
Copy code
$ ./main_02_verboselist.py
Added [4] to the list.
Extended the list with [2] items.
Removed [2] from the list.
Popped [6] from the list.
Popped [1] from the list.
✅ Task 3: CountedIterator - Keeping Track of Iteration
🔸 Objective
Create CountedIterator class.

Tracks how many items were accessed using __next__.

Method: get_count()

💡 Key Concepts
Custom iterators.

Overriding __next__().

🧪 Example
bash
Copy code
$ ./main_03_countediterator.py
Got 1, total 1 items iterated.
Got 2, total 2 items iterated.
Got 3, total 3 items iterated.
Got 4, total 4 items iterated.
No more items.
✅ Task 4: The Enigmatic FlyingFish - Multiple Inheritance
🔸 Objective
Create:

Fish: swim(), habitat()

Bird: fly(), habitat()

FlyingFish inherits from both and overrides all methods.

💡 Key Concepts
Multiple inheritance.

Method Resolution Order (MRO).

🧪 Example
bash
Copy code
$ ./main_04_flyingfish.py
The flying fish is swimming!
The flying fish is soaring!
The flying fish lives both in water and the sky!
✅ Task 5: The Mystical Dragon - Mastering Mixins
🔸 Objective
Create mixins:

SwimMixin: swim()

FlyMixin: fly()

Create Dragon that inherits both and adds roar().

💡 Key Concepts
Mixins = modular reusable behaviors.

Combine multiple behaviors without deep inheritance trees.

🧪 Example
bash
Copy code
$ ./main_05_dragon.py
The creature swims!
The creature flies!
The dragon roars!

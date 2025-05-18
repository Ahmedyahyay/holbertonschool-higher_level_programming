# Python Test-Driven Development Projects

This repository contains a series of Python exercises focused on writing functions and their tests using test-driven development (TDD). Each task implements a specific function with detailed requirements and is accompanied by test files.

---

## Tasks Overview

### 0. Integers Addition

- **Function:** `add_integer(a, b=98)`
- **Description:** Adds two integers or floats (floats are cast to int).
- **Requirements:**
  - `a` and `b` must be integers or floats; else raise `TypeError`.
  - Return the integer sum of `a` and `b`.
- **Example:**
  ```python
  add_integer(1, 2)  # Returns 3
  add_integer(100, -2)  # Returns 98
  add_integer(2)  # Returns 100 (2 + 98 default)
1. Divide a Matrix
Function: matrix_divided(matrix, div)

Description: Divides all elements of a matrix by div, rounding to 2 decimals.

Requirements:

matrix must be a list of lists of integers/floats.

Each row must be the same size.

div must be a number and not zero.

Returns: New matrix with divided values.

2. Say My Name
Function: say_my_name(first_name, last_name="")

Description: Prints My name is <first_name> <last_name>.

Requirements:

Both first_name and last_name must be strings.

Raise TypeError if not.

3. Print Square
Function: print_square(size)

Description: Prints a square using the character #.

Requirements:

size must be an integer >= 0.

Raise appropriate exceptions otherwise.

4. Text Indentation
Function: text_indentation(text)

Description: Prints text with two new lines after ., ?, and :.

Requirements:

text must be a string.

No leading/trailing spaces on printed lines.

5. Max Integer - Unittest
Function: max_integer(list=[])

Description: Returns the max integer in a list.

Includes: Unit tests using the unittest module.

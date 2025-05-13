# README - Python Data Structures

## Overview

This repository contains solutions to a series of Python exercises designed to help users learn and practice essential data structures like lists, tuples, and strings. These exercises provide a hands-on approach to understanding and manipulating different types of data structures.

## Directory Structure

```
python-data_structures/
├── 0-print_list_integer.py        # Print a list of integers
├── 1-element_at.py                # Secure access to an element in a list
├── 2-replace_in_list.py           # Replace element in a list
├── 3-print_reversed_list_integer.py # Print a list of integers in reverse order
├── 4-new_in_list.py               # Replace an element in a list without modifying the original list
├── 5-no_c.py                      # Remove characters 'c' and 'C' from a string
├── 6-print_matrix_integer.py      # Print a matrix of integers
├── 7-add_tuple.py                 # Add 2 tuples
├── 8-multiple_returns.py          # Return the length of a string and its first character
├── 9-max_integer.py               # Find the maximum integer in a list
├── 10-divisible_by_2.py           # Find all multiples of 2 in a list
├── 11-delete_at.py                # Delete an item at a specific position in a list
└── 12-switch.py                   # Switch the values of two variables
```

## File Descriptions

### 0-print\_list\_integer.py

* **Function:** `print_list_integer(my_list=[])`
* **Description:** Prints all integers in a list, each on a new line.
* **Requirements:** The list only contains integers. The function uses `str.format()` for printing.

### 1-element\_at.py

* **Function:** `element_at(my_list, idx)`
* **Description:** Retrieves an element from a list at a specific index. Returns `None` if the index is negative or out of range.

### 2-replace\_in\_list.py

* **Function:** `replace_in_list(my_list, idx, element)`
* **Description:** Replaces an element at a specific position in a list. If the index is invalid, the list is not modified.

### 3-print\_reversed\_list\_integer.py

* **Function:** `print_reversed_list_integer(my_list=[])`
* **Description:** Prints all integers in a list in reverse order, each on a new line.
* **Requirements:** Uses `str.format()` for printing.

### 4-new\_in\_list.py

* **Function:** `new_in_list(my_list, idx, element)`
* **Description:** Replaces an element at a specific position in a copy of the list, leaving the original list unchanged.

### 5-no\_c.py

* **Function:** `no_c(my_string)`
* **Description:** Removes all characters 'c' and 'C' from the input string and returns the new string.
* **Requirements:** Does not use `str.replace()`.

### 6-print\_matrix\_integer.py

* **Function:** `print_matrix_integer(matrix=[[]])`
* **Description:** Prints a matrix (list of lists) of integers.
* **Requirements:** The matrix only contains integers. Each integer is printed using `str.format()`.

### 7-add\_tuple.py

* **Function:** `add_tuple(tuple_a=(), tuple_b=())`
* **Description:** Adds two tuples element by element and returns a tuple with the sum. If a tuple is smaller than 2, uses 0 for missing integers.

### 8-multiple\_returns.py

* **Function:** `multiple_returns(sentence)`
* **Description:** Returns a tuple with the length of a string and its first character. If the string is empty, the first character is `None`.

### 9-max\_integer.py

* **Function:** `max_integer(my_list=[])`
* **Description:** Finds the largest integer in a list. Returns `None` if the list is empty.

### 10-divisible\_by\_2.py

* **Function:** `divisible_by_2(my_list=[])`
* **Description:** Returns a new list indicating whether each integer in the input list is divisible by 2 (`True` or `False`).

### 11-delete\_at.py

* **Function:** `delete_at(my_list=[], idx=0)`
* **Description:** Deletes an item at a specific position in the list. If the index is negative or out of range, the list is not modified.

### 12-switch.py

* **Function:** Swap the values of two variables `a` and `b`.
* **Description:** This script switches the values of two variables using a simple Python assignment.

## Usage

Each file contains a specific Python function, which you can run independently. To execute a function, simply call the respective Python script with the provided input.

For example, to test the function that prints a list of integers, you can run the following command:

```bash
python3 0-print_list_integer.py
```

### Example Output for `0-print_list_integer.py`

```bash
1
2
3
4
5
```

### Example Output for `1-element_at.py`

```bash
Element at index 3 is 4
```

## Requirements

* Python 3.x
* No external modules or libraries required
* All functions are written in standard Python (no additional dependencies)

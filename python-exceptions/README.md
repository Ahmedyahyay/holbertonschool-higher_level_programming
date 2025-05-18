📂 Project: Python - Exceptions
This directory contains Python functions that demonstrate the use of exceptions in various situations. Each function handles potential runtime errors gracefully using try, except, and finally blocks.

0-safe_print_list.py – ✅ Safe List Printing
Function: safe_print_list(my_list=[], x=0)
Prints x elements from my_list using try / except.

All elements are printed on the same line.

Returns the actual number of elements printed.

Does not use len() or import any modules.

1-safe_print_integer.py – ✅ Safe Integer Print
Function: safe_print_integer(value)
Safely prints value as an integer using "{}{:d}".format().

Returns True if printed successfully, else False.

Uses try / except only.

Does not use type() or import any modules.

2-safe_print_list_integers.py – ✅ Print and Count Integers
Function: safe_print_list_integers(my_list=[], x=0)
Prints only integers from the first x elements of my_list.

Skips non-integer types silently.

Returns number of integers printed.

Raises IndexError if x > list length.

Uses "{:d}".format() and try / except.

3-safe_print_division.py – ✅ Division with Debug
Function: safe_print_division(a, b)
Divides a by b with safe error handling.

Prints result in finally block as: Inside result: <value>

Returns result if valid, otherwise None.

4-list_division.py – ✅ Divide a List
Function: list_division(my_list_1, my_list_2, list_length)
Element-wise division of two lists.

Handles mismatched lengths and invalid types.

Prints errors:

"wrong type" for non-number types

"division by 0" for division errors

"out of range" if index out of bounds

Returns new list of results.

5-raise_exception.py – ✅ Raise Type Exception
Function: raise_exception()

Raises a TypeError intentionally.

No external modules used.

6-raise_exception_msg.py – ✅ Raise NameError with Message
Function: raise_exception_msg(message="")

Raises a NameError with a custom message.

No external modules used.

Python Import Modules
This repository contains several Python programs that focus on the concept of importing modules, defining functions, and handling arguments. The exercises cover various aspects of Python, including the use of the import statement, argument handling, and interacting with functions across multiple files.

Task Breakdown
0. Import a Simple Function from a Simple File
Objective:
Write a program that imports the add(a, b) function from the file add_0.py and prints the result of the addition 1 + 2 = 3.

Requirements:

Use print with string format to display the integers.

Define the variables a = 1 and b = 2 on separate lines.

The program should print:
1 + 2 = 3

1. My First Toolbox!
Objective:
Write a program that imports functions from the file calculator_1.py, performs mathematical operations, and prints the results.

Functions to Import:

add(a, b)

sub(a, b)

mul(a, b)

div(a, b)

Requirements:

Define a = 10 and b = 5 on separate lines.

Call each of the imported functions using a and b as arguments.

Print results in the following format:

Copy
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2
2. How to Make a Script Dynamic!
Objective:
Write a program that prints the number of arguments and the list of arguments passed to it.

Output Example:

If no arguments are passed:

javascript
Copy
0 arguments.
If one argument is passed:

yaml
Copy
1 argument:
1: Hello
If multiple arguments are passed:

yaml
Copy
6 arguments:
1: Hello
2: Welcome
3: To
4: The
5: Best
6: School
3. Infinite Addition
Objective:
Write a program that prints the result of adding all arguments passed to it.

Requirements:

Convert arguments to integers using int().

Print the sum of all arguments passed.

4. Who Are You?
Objective:
Write a program that prints all the names defined by the compiled module hidden_4.pyc.

Requirements:

Only print names that do not start with __.

Print one name per line in alphabetical order.

5. Everything Can Be Imported
Objective:
Write a program that imports the variable a from the file variable_load_5.py and prints its value.

Requirements:

Do not use * for importing or __import__.

Print the value of a in the program.

File Descriptions
add_0.py: Contains the function add(a, b) that returns the sum of a and b.

calculator_1.py: Defines four mathematical functions: add(a, b), sub(a, b), mul(a, b), and div(a, b).

hidden_4.pyc: A compiled Python file containing various function names.

variable_load_5.py: Defines a simple variable a with the value 98.

Usage
To run any of the programs, simply execute the respective Python file. For example:

./0-add.py

./1-calculation.py

./2-args.py

Ensure that the necessary files are available in the working directory and the programs are executable.

Repository Information
GitHub Repository: holbertonschool-higher_level_programming

Directory: python-import_modules

File: 0-add.py, 1-calculation.py, 2-args.py, 3-infinite_add.py, 4-hidden_discovery.py, 5-variable_load.py

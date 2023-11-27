# 0x00. Python - Hello, World
## Learning Objectives
At the end of the project, I learnt the following:
- Why Python programming is awesome
- Who created Python
- Who is Guido van Rossum
- Where does the name ‘Python’ come from
- What is the Zen of Python
- How to use the Python interpreter
- How to print text and variables using print
- How to use strings
- What are indexing and slicing in Python
- What is the official Python coding style and how to check your code with pycodestyle
## Tasks
### [0. Write a Shell script that runs a Python script.](0-run)
The Python file name will be saved in the environment variable $PYFILE
### [1. Write a Shell script that runs Python code.](1-run_inline)
The Python code will be saved in the environment variable $PYCODE
### [2. Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.](2-print.py)
- Use the function print
### [3. Complete this source code in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.](3-print_number.py)
- You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/3-print_number.py)
- The output of the script should be:
	- the number, followed by Battery street,
	- followed by a new line
- You are not allowed to cast the variable number into a string
- Your code must be 3 lines long
- You have to use f-strings tips
### [4. Complete the source code in order to print the float stored in the variable number with a precision of 2 digits.](4-print_float.py)
- You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/5-print_string.py)
- The output of the program should be:
	- Float:, followed by the float with only 2 digits
	- followed by a new line
- You are not allowed to cast number to string
- You have to use f-strings
### [5. Complete this source code in order to print 3 times a string stored in the variable str, followed by its first 9 characters.](5-print_string.py)
- You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/5-print_string.py)
- The output of the program should be:
	- 3 times the value of str
	- followed by a new line
	- followed by the 9 first characters of str
	- followed by a new line
- You are not allowed to use any loops or conditional statement
- Your program should be maximum 5 lines long
### [6. Complete this source code to print "Welcome to Holberton School!"](6-concat.py)
- You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/6-concat.py)
- You are not allowed to use any loops or conditional statements.
- You have to use the variables str1 and str2 in your new line of code
- Your program should be exactly 5 lines long
### [7. Complete this source code](7-edges.py)
- You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/7-edges.py)
- You are not allowed to use any loops or conditional statements
- Your program should be exactly 8 lines long
- word_first_3 should contain the first 3 letters of the variable word
- word_last_2 should contain the last 2 letters of the variable word
- middle_word should contain the value of the variable word without the first and last letters
### [8. Complete this source code to print "object-oriented programming with Python", followed by a new line.](8-concat_edges.py)
- You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/8-concat_edges.py)
- You are not allowed to use any loops or conditional statements
- Your program should be exactly 5 lines long
- You are not allowed to create new variables
- You are not allowed to use string literals
### [9. Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.](9-easter_egg.py)
- Your script should be maximum 98 characters long (please check with wc -m 9-easter_egg.py)
### [10. Write a function in C that checks if a singly linked list has a cycle in it.](10-check_cycle.c)
- Prototype: int check_cycle(listint_t *list);
- Return: 0 if there is no cycle, 1 if there is a cycle
Requirements:
- Only these functions are allowed: write, printf, putchar, puts, malloc, free
### [11. Write a Python script that prints exactly "and that piece of art is useful - Dora Korpar, 2015-10-19", followed by a new line.](100-write.py)
- Use the function write from the sys module
- You are not allowed to use print
- Your script should print to stderr
- Your script should exit with the status code 1
### [12. Write a script that compiles a Python script file.](101-compile)
The Python file name will be stored in the environment variable $PYFILE
The output filename has to be $PYFILEc (ex: export PYFILE=my_main.py => output filename: my_main.pyc)
### [13. Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:](102-magic_calculation.py)
```
3             0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE
```

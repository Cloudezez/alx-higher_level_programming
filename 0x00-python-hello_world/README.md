# Python Hello World

## Overview

This repository contains solutions to various introductory Python tasks. The tasks include basic file operations, string manipulations, and bytecode understanding. The purpose of these tasks is to get familiar with Python scripting, basic operations, and understanding Python bytecode.

## Task List

### 0. Run Python file
- **File:** `0-run`
- **Description:** Runs a Python script whose filename is stored in the environment variable `$PYFILE`.

### 1. Run inline
- **File:** `1-run_inline`
- **Description:** Runs Python code stored in the environment variable `$PYCODE`.

### 2. Hello, print
- **File:** `2-print.py`
- **Description:** Prints exactly "Programming is like building a multilingual puzzle", followed by a new line.

### 3. Print integer
- **File:** `3-print_number.py`
- **Description:** Prints the integer stored in the variable `number`, followed by "Battery street", and a new line.

### 4. Print float
- **File:** `4-print_float.py`
- **Description:** Prints the float stored in the variable `number` with a precision of 2 digits.

### 5. Print string
- **File:** `5-print_string.py`
- **Description:** Prints the string stored in the variable `str` three times, followed by its first 9 characters.

### 6. Play with strings
- **File:** `6-concat.py`
- **Description:** Prints "Welcome to Holberton School!" using the variables `str1` and `str2` in exactly 5 lines of code.

### 7. Copy - Cut - Paste
- **File:** `7-edges.py`
- **Description:** Extracts and prints specific parts of the string `word`: first 3 letters, last 2 letters, and the middle part.

### 8. Create a new sentence
- **File:** `8-concat_edges.py`
- **Description:** Prints "object-oriented programming with Python" using string slicing and concatenation, without creating new variables.

### 9. Easter Egg
- **File:** `9-easter_egg.py`
- **Description:** Prints "The Zen of Python" by Tim Peters, followed by a new line. The script must be no longer than 98 characters.

### 10. Linked list cycle
- **File:** `10-check_cycle.c` and `lists.h`
- **Description:** Checks if a singly linked list has a cycle. Includes the implementation of the function `check_cycle()`.

### 11. Hello, write
- **File:** `100-write.py`
- **Description:** Prints "and that piece of art is useful - Dora Korpar, 2015-10-19" to stderr using the `write` function from the `sys` module, and exits with status code 1.

### 12. Compile
- **File:** `101-compile`
- **Description:** Compiles a Python script file specified in the environment variable `$PYFILE`. The output filename will be `$PYFILEc`.

### 13. ByteCode -> Python #1
- **File:** `102-magic_calculation.py`
- **Description:** Defines the function `magic_calculation(a, b)` that replicates specific Python bytecode behavior.

## Requirements

- **Python Version:** 3.x
- **Allowed Editors:** vi, vim, emacs
- **Scripts should:**
  - End with a new line.
  - Be executable.
  - Follow provided guidelines for script length and code style.

## Installation

Clone the repository and navigate to the appropriate directory:

```bash
git clone https://github.com/Cloudezez/alx-higher_level_programming.git
cd alx-higher_level_programming/0x00-python-hello_world
python3 <script_name.py>
export PYFILE=<script_name.py>
./101-compile

https://github.com/Cloudezez/alx-higher_level_programming.git

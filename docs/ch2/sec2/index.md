# Chapter 2: Introduction to Python

## Section 2: Variables and Data Types

Variables are fundamental components of any programming language. They allow you to store and manipulate data in your programs. In this section, we'll explore variables and different data types in Python.

### Variables in Python

In Python, variables are dynamically typed, which means you don't need to declare their types explicitly. You can simply assign a value to a variable, and Python will infer its type based on the assigned value.

Here's an example that demonstrates variable assignment:

```python
# Variable assignment
message = "Hello, World!"
count = 10
pi = 3.14159
is_true = True
```

In the above example, we assigned different values to variables of different types, including strings, integers, floating-point numbers, and boolean values.

### Naming Conventions for Variables

When choosing variable names in Python, it's important to follow naming conventions to write clean and readable code. Here are some guidelines for naming variables:

- Variables should have descriptive names that reflect their purpose.
- Variable names can consist of letters, numbers, and underscores (_), but they cannot start with a number.
- Variable names are case-sensitive, so `message` and `Message` are considered different variables.
- Avoid using reserved keywords as variable names.

### Data Types in Python

Python provides several built-in data types to work with different kinds of data. Some commonly used data types include:

- **Numeric Types**: Integers (`int`), floating-point numbers (`float`), and complex numbers (`complex`).
- **String Type**: Represents a sequence of characters and is denoted by the `str` type.
- **Boolean Type**: Represents either `True` or `False` and is denoted by the `bool` type.
- **List Type**: An ordered collection of elements, denoted by square brackets (`[]`).
- **Tuple Type**: An ordered, immutable collection of elements, denoted by parentheses (`()`).
- **Dictionary Type**: A collection of key-value pairs, denoted by curly braces (`{}`).
- **Set Type**: An unordered collection of unique elements, denoted by curly braces (`{}`).

Here's an example that demonstrates the usage of different data types:

```python
# Numeric types
num1 = 10
num2 = 3.14159
result = num1 + num2

# String type
name = "John Doe"

# Boolean type
is_valid = True

# List type
fruits = ["apple", "banana", "orange"]

# Tuple type
point = (5, 10)

# Dictionary type
student = {"name": "John", "age": 20}

# Set type
numbers = {1, 2, 3, 4, 5}
```

### Type Conversion

Python provides functions to convert variables from one type to another. These functions include `int()`, `float()`, `str()`, and more. You can use these functions to convert variables when needed.

Here's an example that demonstrates type conversion:

```python
# Type conversion
num = 10
num_str = str(num)
num_float = float(num)

print(num_str)
print(num_float)
```

In the above example, we convert the integer variable `num` to a string and a floating-point number using the `str()` and `float()` functions, respectively.

Understanding variables and data types is essential for working with data in Python. In the upcoming sections, we'll delve deeper into Python's data types and explore more advanced concepts.

[Back](../sec1/index.md) |
[Next](../sec3/index.md)

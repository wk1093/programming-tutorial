# Chapter 2: Introduction to Python

## Section 3: Operators and Expressions

Operators in Python allow you to perform various operations on data, such as arithmetic calculations, logical evaluations, and comparisons. In this section, we'll explore different operators and expressions in Python.

This section might feel a bit fast, but you should already understand the basics from C.

### Arithmetic Operators

Arithmetic operators are used to perform mathematical calculations in Python. The commonly used arithmetic operators include:

- **Addition (`+`)**: Adds two operands.
- **Subtraction (`-`)**: Subtracts the second operand from the first.
- **Multiplication (`*`)**: Multiplies two operands.
- **Division (`/`)**: Divides the first operand by the second.
- **Floor Division (`//`)**: Divides the first operand by the second and rounds down to the nearest whole number.
- **Modulus (`%`)**: Returns the remainder of the division.
- **Exponentiation (`**`)**: Raises the first operand to the power of the second.

Here's an example that demonstrates the usage of arithmetic operators:

```python
# Arithmetic operators
num1 = 10
num2 = 3

sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2
division_result = num1 / num2
floor_division_result = num1 // num2
modulus_result = num1 % num2
exponentiation_result = num1 ** num2

print(sum_result)
print(difference_result)
print(product_result)
print(division_result)
print(floor_division_result)
print(modulus_result)
print(exponentiation_result)
```

### Comparison Operators

Comparison operators are used to compare values and evaluate conditions. The result of a comparison operation is a boolean value (`True` or `False`). Some commonly used comparison operators include:

- **Equal to (`==`)**: Checks if two operands are equal.
- **Not equal to (`!=`)**: Checks if two operands are not equal.
- **Greater than (`>`)**: Checks if the left operand is greater than the right.
- **Less than (`<`)**: Checks if the left operand is less than the right.
- **Greater than or equal to (`>=`)**: Checks if the left operand is greater than or equal to the right.
- **Less than or equal to (`<=`)**: Checks if the left operand is less than or equal to the right.

Here's an example that demonstrates the usage of comparison operators:

```python
# Comparison operators
num1 = 10
num2 = 3

is_equal = num1 == num2
is_not_equal = num1 != num2
is_greater = num1 > num2
is_less = num1 < num2
is_greater_or_equal = num1 >= num2
is_less_or_equal = num1 <= num2

print(is_equal)
print(is_not_equal)
print(is_greater)
print(is_less)
print(is_greater_or_equal)
print(is_less_or_equal)
```

### Logical Operators

Logical operators allow you to perform logical operations on boolean values. The commonly used logical operators include:

- **Logical AND (`and`)**: Returns `True` if both operands are `True`.
- **Logical OR (`or`)**: Returns `True` if either of the operands is `True`.
- **Logical NOT (`not`)**: Returns the opposite boolean value of the operand.

Here's an example that demonstrates the usage of logical operators:

```python
# Logical operators
is_sunny = True
is_warm = False

is_good_weather = is_sunny and is_warm
is_bad_weather = is_sunny or is_warm
is_not_sunny = not is_sunny

print(is_good_weather)
print(is_bad_weather)
print(is_not_sunny)
```

Understanding operators and expressions is crucial for performing various computations and making logical evaluations in your Python programs. In the upcoming sections, we'll explore more advanced topics in Python programming.


[Back](../sec2/index.md) |
[Next](../sec4/index.md)
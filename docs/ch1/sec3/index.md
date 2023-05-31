# Chapter 1: Introduction to C

## Section 3: Operators and Expressions

In C, operators are used to perform various operations on variables and constants. Expressions, on the other hand, are combinations of operators, variables, and constants that produce a result.

### Arithmetic Operators

C provides several arithmetic operators to perform basic mathematical operations:

- **Addition (`+`):** Adds two operands.
- **Subtraction (`-`):** Subtracts the second operand from the first.
- **Multiplication (`*`):** Multiplies two operands.
- **Division (`/`):** Divides the first operand by the second.
- **Modulus (`%`):** Returns the remainder of the division operation.
- **Increment (`++`) and Decrement (`--`):** Increase or decrease the value of a variable by 1.

Here's an example that demonstrates the usage of arithmetic operators:

```c
int x = 10;
int y = 5;

int sum = x + y;  // Addition
int difference = x - y;  // Subtraction
int product = x * y;  // Multiplication
int quotient = x / y;  // Division
int remainder = x % y;  // Modulus

x++;  // Increment x by 1
y--;  // Decrement y by 1
```

### Relational Operators

Relational operators compare two values and return a result of either true (non-zero) or false (0):

- **Equal to (`==`):** Checks if two values are equal.
- **Not equal to (`!=`):** Checks if two values are not equal.
- **Greater than (`>`):** Checks if the left operand is greater than the right operand.
- **Less than (`<`):** Checks if the left operand is less than the right operand.
- **Greater than or equal to (`>=`):** Checks if the left operand is greater than or equal to the right operand.
- **Less than or equal to (`<=`):** Checks if the left operand is less than or equal to the right operand.

Here's an example that demonstrates the usage of relational operators:

```c
int x = 10;
int y = 5;

int isEqual = (x == y);  // Checks if x is equal to y
int isNotEqual = (x != y);  // Checks if x is not equal to y
int isGreater = (x > y);  // Checks if x is greater than y
int isLess = (x < y);  // Checks if x is less than y
int isGreaterOrEqual = (x >= y);  // Checks if x is greater than or equal to y
int isLessOrEqual = (x <= y);  // Checks if x is less than or equal to y
```

### Logical Operators

Logical operators are used to combine multiple conditions and produce a logical result:

- **Logical AND (`&&`):** Returns true if both conditions are true.
- **Logical OR (`||`):** Returns true if at least one of the conditions is true.
- **Logical NOT (`!`):** Reverses the logical state of a condition.

Here's an example that demonstrates the usage of logical operators:

```c
int x = 10;
int y = 5;

int result1 = (x > 0) && (y < 10);  // Checks if x is greater than 0 and y is less than 10
int result2 = (x > 0) || (y > 10);  // Checks if x is greater than 0 or y is greater than 10
int result3 = !(x > y);  // Checks if x is not greater than y
```

### Assignment Operators

Assignment operators are used to assign values to variables:

- **=:** Assigns the value on the right to the variable on the left.
- **+=, -=, *=, /=, %=:** Perform the corresponding arithmetic operation and then assign the result to the variable.

Here's an example that demonstrates the usage of assignment operators:

```c
int x = 10;
int y = 5;

x += y;  // Equivalent to x = x + y
y -= 3;  // Equivalent to y = y - 3
```

Understanding operators and expressions is essential for performing computations and making logical decisions in C programs. In the upcoming sections, we'll explore more about operators, expressions, and how they are used in C.

Let's continue our journey into the world of C programming and explore these concepts further!

[Back](../sec2/index.md) |
[Next](../sec4/index.md)
# Chapter 1: Introduction to C

## Section 4: Control Flow: Conditional Statements and Loops

Control flow statements are used in C to control the execution of the program based on certain conditions. This allows for making decisions and repeating actions as needed. In this section, we'll explore conditional statements and loops.

### Conditional Statements: if, else if, and else

Conditional statements are used to perform different actions based on different conditions. In C, the `if` statement is used to perform a certain action if a condition is true. The `else if` statement allows for checking multiple conditions, and the `else` statement provides a default action if none of the conditions are true.

Here's an example that demonstrates the usage of conditional statements:

```c
int num = 10;

if (num > 0) {
    printf("The number is positive.");
} else if (num < 0) {
    printf("The number is negative.");
} else {
    printf("The number is zero.");
}
```

### Loops: while, for, and do-while

Loops are used to repeat a block of code multiple times. There are different types of loops in C:

- The `while` loop repeats a block of code as long as a condition is true.
- The `for` loop repeats a block of code for a specific number of times.
- The `do-while` loop repeats a block of code at least once, and then continues as long as a condition is true.

Here's an example that demonstrates the usage of loops:

```c
int i = 1;

while (i <= 5) {
    printf("%d\n", i);
    i++;
}

for (int j = 1; j <= 5; j++) {
    printf("%d\n", j);
}

int k = 1;
do {
    printf("%d\n", k);
    k++;
} while (k <= 5);
```

### Control Flow: break and continue

The `break` statement is used to exit a loop prematurely, while the `continue` statement is used to skip the rest of the current iteration and continue to the next iteration.

Here's an example that demonstrates the usage of `break` and `continue`:

```c
for (int i = 1; i <= 10; i++) {
    if (i == 5) {
        break;  // Exit the loop when i is equal to 5
    }
    if (i % 2 == 0) {
        continue;  // Skip the even numbers and continue to the next iteration
    }
    printf("%d\n", i);
}
```

Understanding control flow statements is crucial for implementing conditional behavior and repetitive tasks in C programs. In the upcoming sections, we'll dive deeper into control flow and explore more advanced concepts.

[Back](../sec3/index.md) |
[Next](../sec5/index.md)
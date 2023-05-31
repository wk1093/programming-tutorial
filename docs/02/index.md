# Part 2: C

## Hello World

In C, the hello world program is a bit more complicated than in Python. Here is the code:

```c
#include <stdio.h>

int main() {
    printf("Hello World!\n");
    return 0;
}
```

Let's break it down:

```c
#include <stdio.h>
```

This line tells the compiler to include the standard input/output library. This library contains the `printf` function, which we use to print the string "Hello World!" to the console.

```c
int main() {
```

This line declares the main function. The main function is the entry point of the program. Every C program must have a main function.
The main function returns an int (the exit code) so we declare with the int keyword. Unlike python there isn't a special keyword to declare a function
we just use a type, in this case int. The main function takes no arguments so we leave the parentheses empty.

```c
    printf("Hello World!\n");
```

This calls the printf function with the string "Hello World!\n" as an argument. The `\n` is an escape sequence that tells the console to print a newline.

```c
    return 0;
```

This line returns 0 from the main function. This is the exit code of the program. A return code of 0 means the program exited successfully.

```c
}
```

This line ends the main function. 

## Variables

In C, variables must be declared before they can be used. Here is an example:

```c
int main() {
    int x = 5;
    printf("%d\n", x);
    return 0;
}
```

This program declares a variable named `x` and assigns it the value 5. The `%d` in the printf function is a format specifier. It tells the printf function to print an integer. The `x` after the format specifier is the variable to print.

## Functions

Functions in C are declared like this:

```c
int add(int x, int y) {
    return x + y;
}
```

This function takes two integers as arguments and returns their sum. The `int` before the function name is the return type. The `int` before each argument is the type of the argument. The `return` keyword returns a value from the function.

## Pointers

Pointers are a very important concept in C. A pointer is a variable that stores the address of another variable. Here is an example:

```c
int main() {
    int x = 5;
    int *y = &x;
    printf("%d\n", *y);
    return 0;
}
```

Let's break it down:

```c
int x = 5;
```

This line declares a variable named `x` and assigns it the value 5.

```c
int *y = &x;
```

This line declares a variable named `y` and assigns it the address (position in memory) of `x`. The `*` before the variable name tells the compiler that `y` is 
a pointer. The `&` before the variable name tells the compiler to get the address of the variable.

If you have trouble understanding pointers, I recommend reading [this](https://www.tutorialspoint.com/cprogramming/c_pointers.htm) tutorial.

```c
printf("%d\n", *y);
```

This line prints the value of `y`. The `*` before the variable name tells the compiler to get the value at the address stored in `y`.

## Arrays

In C, arrays are declared like this:

```c
int main() {
    int x[5] = {1, 2, 3, 4, 5};
    printf("%d\n", x[0]); // first element: 0
    return 0;
}
```

In most programming langauges, arrays start at 0, not 1. So to get the first element in an array, you use `array[0]`. for the second element, you use `array[1]`, and so on.

This program declares an array named `x` with 5 elements. The first element is 1, the second is 2, and so on. The `x[0]` in the printf function gets the first element of the array.

An array is actually just a pointer to the first element of the array. So the following code is equivalent to the previous example:

```c
int main() {
    int x[5] = {1, 2, 3, 4, 5};
    printf("%d\n", *x); // first element: 0
    return 0;
}
```

```c
int main() {
    int x[5] = {1, 2, 3, 4, 5};
    printf("%d\n", x[1]); // second element: 1
    printf("%d\n", *(x + 1)); // same as above
    return 0;
}
```

The above example shows how x is just a number that points to the first element of the array. The `x[1]` in the printf function gets the second element of the array. 
`*(x + 1)` can be explained as `get value at (x + 1)`. since x is just a position in memory, and the array is stored in the same memory, we can just add 1 to x to get the second element of the array.

Since a pointer is just a number, we can also use it to access other memory locations. Here is an example:

```c
int main() {
    int *y = (int *) 0; // point to memory location 0
    printf("%d\n", *y); // will cause a segmentation fault (tried to access memory that doesn't belong to the program)
    return 0;
}
```

The `(int*) 0` is a cast, which tells the compiler to treat the number 0 as a pointer to an integer. I'll explain casts in more detail later.

Pointers are very powerful, but they can also be very dangerous. If you try to access memory that doesn't belong to your program, you will get a segmentation fault. This is a very common error in C programs.

If you have trouble understanding pointers, I recommend reading [this](https://www.tutorialspoint.com/cprogramming/c_pointers.htm) tutorial.

## Casting

Casting is a way to tell the compiler to treat a variable as a different type. Here is an example:

```c
int main() {
    int x = 5;
    printf("%f\n", (float) x);
    return 0;
}
```

This program declares a variable named `x` and assigns it the value 5. The `(float)` before the variable name tells the compiler to treat `x` as a float. The `%f` in the printf function is a format specifier. It tells the printf function to print a float. The `x` after the format specifier is the variable to print.

You can also cast a variable multiple times. Here is an example:

```c
int main() {
    int x = 5;
    printf("%d\n", x);
    printf("%d\n", (int) (float) x);
    return 0;
}
```

This program declares a variable named `x` and assigns it the value 5. The `(float)` before the variable name tells the compiler to treat `x` as a float. The `(int)` before the variable name tells the compiler to treat `x` as an int. The `%d` in the printf function is a format specifier. It tells the printf function to print an int. The `x` after the format specifier is the variable to print.

## Control Flow

Control flow is a way to control the order in which statements are executed. Here is an example:

```c
int main() {
    int x = 5;
    if (x == 5) {
        printf("x is 5\n");
    } else {
        printf("x is not 5\n");
    }
    return 0;
}
```

This program declares a variable named `x` and assigns it the value 5. The `if` statement checks if `x` is equal to 5. If it is, it prints "x is 5". If it isn't, it prints "x is not 5".

## Loops

Loops are a way to repeat a block of code multiple times. Here is an example:

```c
int main() {
    int x = 0;
    while (x < 5) {
        printf("%d\n", x);
        x++;
    }
    return 0;
}
```

This program declares a variable named `x` and assigns it the value 0. The `while` loop repeats the block of code until `x` is equal to 5. The `printf` function prints the value of `x`. The `x++` statement increments `x` by 1.

### For Loops

For loops are a way to repeat a block of code a specific number of times. Here is an example:

```c
int main() {
    for (int x = 0; x < 5; x++) {
        printf("%d\n", x);
    }
    return 0;
}
```

This program declares a variable named `x` and assigns it the value 0. The `for` loop repeats the block of code until `x` is equal to 5. The `printf` function prints the value of `x`. The `x++` statement increments `x` by 1. A for loop is in the following format: 
`for (initialization; condition; increment) { code }`. The initialization is executed before the loop starts. The condition is checked before each iteration of the loop. The increment is executed after each iteration of the loop.

## User Input

Unlike python, user input in C does not need to be casted. Here is an example of string and integer input:

```c
#include <stdio.h>

int main() {
    char name[100]; // buffer
    int age;
    printf("Enter your name: ");
    scanf("%s", name);
    printf("Enter your age: ");
    scanf("%d", &age);
    printf("Hello %s, you are %d years old\n", name, age);
    return 0;
}
```

Wow, that's a lot of new stuff. Let's go over it line by line.

```c
char name[100]; // buffer
```

This is a list of characters, that represents the input from the user. The 100 is the maximum number of characters that can be stored in the buffer. If the user enters more than 100 characters, the program will crash.

```c
int age;
```

This is an integer, that represents the input from the user. The `int` before the variable name tells the compiler to treat `age` as an integer.

```c
scanf("%s", name);
```

This reads a string from the console and stores it in the buffer `name`. The `%s` in the scanf function is a format specifier. It tells the scanf function to read a string. The `name` after the format specifier is the buffer to store the string in.

```c
scanf("%d", &age);
```

This reads an integer from the console and stores it in the variable `age`. The `%d` in the scanf function is a format specifier. It tells the scanf function to read an integer. The `&age` after the format specifier is the variable to store the integer in. This is because scanf requires a pointer to the variable, not the variable itself. I'll explain pointer arguments in more detail later.

```c
printf("Hello %s, you are %d years old\n", name, age);
```

This prints the name and age of the user. The `%s` in the printf function is a format specifier. It tells the printf function to print a string. The `name` after the format specifier is the buffer to print. The `%d` in the printf function is a format specifier. It tells the printf function to print an integer. The `age` after the format specifier is the variable to print.

## Pointer Arguments

Pointer arguments are a way to pass a variable by reference. Here is an example:

```c
void set_to_5(int *x) {
    *x = 5;
}

int main() {
    int x = 2;
    printf("%d\n", x);
    set_to_5(&x);
    printf("%d\n", x);
    return 0;
}
```

This program declares a variable named `x` and assigns it the value 2. The `printf` function prints the value of `x`. The `set_to_5` function takes a pointer to an integer as an argument. The `*x = 5` statement sets the value of the integer pointed to by `x` to 5. The `set_to_5(&x)` statement calls the `set_to_5` function with a pointer to `x` as an argument. The `printf` function prints the value of `x`.

## Examples / Exercises

Now with all our new knowledge, we can make some programs.
Here is a few examples with a challenge:

### Guessing Game

```c
#include <stdio.h>
#include <stdlib.h> // for rand() and srand()
#include <time.h> // for time()

// the user can keep guessing until they guess the correct number
// try to modify/rewrite this program to only allow 3 guesses

int main() {
    srand(time(NULL)); // seed the random number generator
    int number = rand() % 10 + 1; // generate a random number between 1 and 10
    int guess;
    while (1) {
        printf("Enter a number: ");
        scanf("%d", &guess);
        if (guess == number) {
            printf("You guessed the correct number!\n");
            break;
        } else if (guess < number) {
            printf("Too low\n");
        } else {
            printf("Too high\n");
        }
    }
    return 0;
}
```
[Solution](guess.md)

Like in Python, if you have trouble reading the code, try going line by line and writing pseudocode for it.
Try changing different parts of the code and see what happens.

## Note
 > From now on, most of the tutorial will have Python and/or C code examples. So make sure you have a basic understanding of both languages before continuing.
 
If you need help with Python, check out [this](https://www.w3schools.com/python) tutorial.
If you need help with C, check out [this](https://www.w3schools.com/c/) tutorial.

[Back](../01/) |
[Next](../03/)
# Programming Concepts

Programming is really just converting a thought into a basic form called an algorithm. Then writing that algorithm in what is called
a programming language. The compiler then takes that programming language and converts it into machine code that the computer can
understand.

## Algorithms

An algorithm is a set of instructions that are followed to solve a problem. For example, if you wanted to make a peanut butter and jelly sandwich, you would follow these steps:
```
1. Get two slices of bread
2. Get peanut butter and jelly
3. Spread peanut butter on one slice of bread
4. Spread jelly on the other slice of bread
5. Put the two slices of bread together
```
This is an algorithm. It is a set of instructions that are followed to solve a problem. In this case, the problem is making a peanut butter and jelly sandwich.

## Programming Languages

A programming language is similar to a normal langauge, but instead of using it to communicate, we use it to write an algorithm.
Here is a basic algorithm to write "Hello World" using a programming language called Python:
```py
print("Hello World")
```
This is a very simple algorithm. It is just one line of code. The `print` function is a built-in function in Python that prints whatever you give it.
In this case, we gave it the string `"Hello World"`. A string is a sequence of characters. In this case, the string is `"Hello World"`.
The string is surrounded by double quotes. This tells Python that the characters inside the double quotes are a string.

### String

A string is a sequence of characters. A character is a single letter, number, or symbol. A string is surrounded by double quotes. For example, `"Hello World"` is a string.

### Function

A function is a set of instructions that can be reused, and sometimes given different inputs. For example, the `print` function is a function that prints whatever you give it. In this case, we gave it the string `"Hello World"`. A function is called by using its name, followed by parentheses. Inside the parentheses, you can put the inputs to the function. In this case, we gave the `print` function the string `"Hello World"` as an input.

### Structure

Different programming langauges have different ways of writing the same thing, some programming langauges are more verbose (use more words) than others. For example, here is the same algorithm in C:
```c
#include <stdio.h> // this lets us use the printf function

int main() { // tells the program that the code inside here is meant to be run first
    printf("Hello World\n"); // prints "Hello World" the \n means new line (Python automatically adds this)
    return 0; // tells the program that it is done and had no errors (errors can be signaled by returning a number other than 0)
} // code inside of curly braces is called a block
```

### Variables

A variable is a way to store data. For example, if you wanted to store the number 5, you could do this in Python:
```py
x = 5
```
This creates a variable called `x` and sets it to the number 5. You can then use the variable `x` to get the number 5. For example:
```py
x = 5
print(x) # prints 5
```

Here is the same thing in C:
```c
#include <stdio.h>

int main() {
    int x = 5; // creates a variable called x and sets it to 5, 'int' means integer (a whole number)
    printf("%d\n", x); // prints 5 (printf is print formatted) %d means print an integer
    return 0;
}
```

printf is a function that prints formatted text. The first input is a string that tells printf what to print. You can add special characters to the string to tell printf to print a variable. For example, `%d` tells printf to print an integer. The second input is the variable to print. In this case, we gave it the variable `x`.
if you wanted to print 2 integers, you could do this:
```c
printf("%d, %d\n", x, y); // prints 2 integers separated by a comma
```

### Comments

You probably have realized this by now, but code after the `//` is greyed out, and does not count towards any part of the algorithm. This is called a comment,
They are used for many different reasons, but mostly to explain the code to other people. For example, if you wanted to explain what a variable does, you could do this:
```c
int x = 5; // This variable stores the number of apples
```

### Types

You may have noticed that in C, you have to specify a type before the name of a variable, this is because C is a statically typed language. This means that you have to specify the type of a variable before you use it. Python is a dynamically typed language, which means that you do not have to specify the type of a variable before you use it. For example, in Python, you can do this:
```py
x = 5
x = "Hello World"
```
This is not possible in C, because you have to specify the type of a variable before you use it. For example, this is not possible in C:
```c
int x = 5;
x = "Hello World"; // this is not possible because x is an integer, not a string
```

The basic types in C are:
- `int` - an integer (a whole number, 1, 2, 3 ... 100, not 1.5, 1.2...)
- `float` - a floating point number (a number with a decimal point, 1.5, 1.2, 3.14...)
- `char` - a character (a single letter, number, or symbol, 'a', 'b', 'c', '1', '2', '3', '!', '@', '#', '$'...)

there is other types that are different sizes, but they are all similar to these types.

### Operators

Operators are used to do math. For example, if you wanted to add 2 numbers, you could do this:
```c
int x = 5;
int y = 10;
int z = x + y; // z is now 15
```
(Remember, C code has to be inside of a function, so this code would be inside of the `main` function)

here is a few of the most common operators:
- `+` - addition
- `-` - subtraction
- `*` - multiplication
- `/` - division
- `%` - modulus (remainder)

### Control Flow

Sometimes in an algorithm, you want to do something different based on a condition. Or repeat something multiple times. This is called control flow. There are 3 main types of control flow:
- `if` - if a condition is true, do something
- `for` - repeat something a certain number of times, or iterate (go through each element) over a list
- `while` - repeat something until a condition is false (or true, using the not operator)

#### If

If statements are used to do something if a condition is true. For example, if you wanted to print "Hello World" if a variable called `x` is equal to 5, you could do this:

C
```c
if (x == 5) { // if x is equal to 5
    printf("Hello World\n"); // print "Hello World"
}
```

Python
```py
if x == 5: # if x is equal to 5
    print("Hello World") # print "Hello World"
```

you can use the `else` keyword to do something if the condition is false. For example, if you wanted to print "Hello World" if a variable called `x` is equal to 5, and print "Goodbye World" if it is not, you could do this:

C
```c
if (x == 5) { // if x is equal to 5
    printf("Hello World\n"); // print "Hello World"
} else { // if x is not equal to 5
    printf("Goodbye World\n"); // print "Goodbye World"
}
```

Python
```py
if x == 5: # if x is equal to 5
    print("Hello World") # print "Hello World"
else: # if x is not equal to 5
    print("Goodbye World") # print "Goodbye World"
```

You can also use `else if` (or `elif` in python) to do something if the first condition is false, and another condition is true. For example, if you wanted to print "Hello World" if a variable called `x` is equal to 5, print "Goodbye World" if it is not, and print "Hello Goodbye World" if it is equal to 10, you could do this:

C
```c
if (x == 5) { // if x is equal to 5
    printf("Hello World\n"); // print "Hello World"
} else if (x == 10) { // if x is equal to 10
    printf("Hello Goodbye World\n"); // print "Hello Goodbye World"
} else { // if x is not equal to 5 or 10
    printf("Goodbye World\n"); // print "Goodbye World"
}
```

Python
```py
if x == 5: # if x is equal to 5
    print("Hello World") # print "Hello World"
elif x == 10: # if x is equal to 10
    print("Hello Goodbye World") # print "Hello Goodbye World"
else: # if x is not equal to 5 or 10
    print("Goodbye World") # print "Goodbye World"
```

#### For

For loops are used to repeat something a certain number of times, or iterate (go through each element) over a list. For example, if you wanted to print "Hello World" 5 times, you could do this:

C
```c
for (int i = 0; i < 5; i++) { // repeat 5 times
    printf("Hello World\n"); // print "Hello World"
}
```
(Again, remember that C code has to be inside of a function, so this code would be inside of the `main` function)

Python
```py
for i in range(5): # repeat 5 times
    print("Hello World") # print "Hello World"
```

Some of this code (especially the C part) looks a bit confusing, but in the Python and C sections of this tutorial, I will explain what each part of the code does.

#### While

While loops are used to repeat something until a condition is false. For example, if you wanted to print "Hello World" until a variable called `x` is equal to 5, you could do this:

C
```c
while (x != 5) { // repeat until x is equal to 5
    printf("Hello World\n"); // print "Hello World" 
}
```

Python
```py
while x != 5: # repeat until x is equal to 5
    print("Hello World") # print "Hello World"
```

If x is never equal to 5, this will repeat forever.
[Back: Main](../)
[Next: Python](../c/)

# Part 1: Python

Python is an interpreted langauge, meaning that instead of compiling our code into 1s and 0s (machine code), someone else's program will
interpret (hence the name *interpreted*) our code, and do what we tell it to do. This is different from a compiled language, like C, where
we have to compile our code into machine code before we can run it.

## Hello World

```py
print("Hello World")
```

In python the "builtin library" (built in functions that we can use) does not need to be imported, so we can just use the `print` function.
In python the print function automatically adds a newline at the end of whatever you print, so we don't need to add a newline character (`\n`).

## Variables

```py
x = 5
print(x)
```

In python, variables do not need to have a type, it is inferred from the value that you assign to it. In this case, we assigned the number 5 to
the variable `x`, so the type of `x` is an integer (whole number).

Just because python does not require you to specify the type of a variable, does not mean that you can't. You can specify the type of a variable
by adding a colon (`:`) after the variable name, and then the type. For example:

```py
x: int = 5
```

This is useful if you want to make sure that a variable is a certain type, or you want to be explicit about what type a variable is.

## Comments

```py
# This is a comment
```

In python, comments use `#` instead of `//`. Comments are used to explain what your code does, or to disable a line of code.

## Types

The basic types in python are:
- `int` - an integer (a whole number, 1, 2, 3 ... 100, not 1.5, 1.2...)
- `float` - a floating point number (a number with a decimal point, 1.5, 1.2, 3.14, 2.71828...)
- `str` - a string (a sequence of characters, "Hello World", "This is a string", "123", "1.5", "True", "False")
- `bool` - a boolean (a value that is either `True` or `False`)
- `None` - a special type that represents nothing
- `list` - a list of values (a sequence of values, [1, 2, 3], ["Hello", "World"], [1, 2, 3, "Hello", "World"])
- `dict` - a dictionary (a mapping of keys to values, {"key": "value", "name": "John", "age": 20})

there is other types, but these are the basic ones.

## Operators

### Arithmetic Operators

```py
x = 5
y = 2
print(x + y) # prints 7
print(x - y) # prints 3
print(x * y) # prints 10
print(x / y) # prints 2.5
```

## Functions

```py
def print_hello():
    print("Hello")
```

We can declare a function using the `def` keyword, followed by the name of the function, and then parentheses `()`. If the function takes
arguments, we can put the names of the arguments inside the parentheses, separated by commas. After the parentheses, we put a colon (`:`),
and then the body of the function. The body of the function is indented, and all of the code that is indented is part of the function.

```py
def hello(name: str): # the name argument is a string, we can't add a number to a string, so we need to make sure that the name argument is a string
    return "Hello " + name + "!"
```

To use a function, we just call it by name, and pass in the arguments. If the function returns a value, we can store it in a variable.

```py
print(hello("John")) # prints "Hello John!"
```

## Control Flow

### If Statements

```py
def is_even(x: int) -> bool: # this function takes an integer, and returns a boolean
    if x % 2 == 0: # if x is divisible by 2 with no remainder
        return True
    else:
        return False
```

In python, if statements are written using the `if` keyword, followed by a condition, and then a colon (`:`). The body of the if statement
is indented, and all of the code that is indented is part of the if statement. If the condition is true, then the code in the body of the
if statement will be executed. If the condition is false, then the code in the body of the if statement will not be executed.

### For Loops

```py
for i in range(10): # range(10) returns a list of numbers from 0 to 9
    print(i) # prints 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
```

In python for loops are written using the `for` keyword, followed by a variable name, the `in` keyword, and then a list. The body of the
for loop is indented, and all of the code that is indented is part of the for loop. The variable that we declared in the for loop will
be assigned to each value in the list, and the body of the for loop will be executed for each value in the list.

### While Loops

```py
x = 0
while x < 10:
    print(x)
    x += 1 # add 1 to x
```

In python while loops are written using the `while` keyword, followed by a condition, and then a colon (`:`). The body of the while loop
is indented, and all of the code that is indented is part of the while loop. The condition is checked before the body of the while loop
is executed, and if the condition is true, then the body of the while loop will be executed. After the body of the while loop is executed,
the condition is checked again, and if the condition is true, then the body of the while loop will be executed again. This will continue
until the condition is false.

## User Input

```py
name = input("What is your name? ")
print("Hello " + name)
```

In python, using the `input` function, we can get input from the user. The `input` function takes a string as an argument, and then prints
that string to the console (without newline), and then waits for the user to type something, and press enter. Whatever the user types will
be returned from the `input` function, and we can store it in a variable.

### Input Types

```py
x = input("Enter a number: ")
print(x + 5) # this will not work, because x is a string
```

The `input` function always returns a string, so if we want to get a number from the user, we need to convert the string to a number.

```py
x = int(input("Enter a number: "))
print(x + 5) # this will work, because x is an integer
```

We can convert a string to an integer using the `int` function, or we can convert a string to a float using the `float` function.
If the user enters something that is not a number, then we will get an error.

## Exceptions

```py
try:
    x = int(input("Enter a number: "))
    print(x + 5)
except ValueError:
    print("You did not enter a number")
```

In python, error handling is really easy, we can use the `try` and `except` keywords to handle errors. The code in the `try` block will
be executed, and if an error occurs, then the code in the `try` will stop executing, and the code in the `except` block will be executed.
If no error occurs, then the code in the `except` block will not be executed.

<!-- Classes will be in another section about object oriented programming -->

## Importing

In python there is a standard library that comes with python, and there is also a lot of third party libraries that we can install and use.
To use a library, we need to import it.

```py
import random # import the random library (part of python)

print(random.randint(1, 10)) # prints a random number between 1 and 10
```

We can also import specific functions from a library.

```py
from random import randint # import the randint function from the random library

print(randint(1, 10)) # prints a random number between 1 and 10
```

We can import another python file that we made as a "module".

mytestfile.py:
```py
avariable = 5
```

main.py:
```py
import mytestfile # import the mytestfile module

print(mytestfile.avariable) # prints 5
```

<!-- File I/O will be in another section -->

## Examples / Exercises

Now with all our new knowledge, we can make some programs.
Here is a few examples:

### Guessing Game

```py
import random

number = random.randint(1, 10)
guess = -1

# the user can keep guessing until they guess the correct number
# try to modify this program to only allow 3 guesses

while guess != number: # repeat until correct guess
    try:
        guess = int(input("Guess a number between 1 and 10: "))
    except ValueError:
        print("You did not enter a number")
        continue # go to next iteration of loop
    
    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")
    else:
        print("Correct!")
    
    if guess == -1: # if guess is -1, then the user wants to quit
        print("The number was " + str(number))
        break # exit loop

```

### Rock Paper Scissors

```py

import random

# rock paper scissors game
# try to modify this program to keep track of wins and losses

while True: # repeat forever
    user = input("Rock, Paper, or Scissors? ").lower() # get user input and convert to lowercase
    if user not in ["rock", "paper", "scissors"]: # check if user input is valid
        print("Invalid input")
        continue # go to next iteration of loop
    computer = random.choice(["rock", "paper", "scissors"]) # choose a random option
    
    if user == computer:
        print("Tie!")
    elif user == "rock":
        if computer == "paper":
            print("You lose!")
        else:
            print("You win!")
    elif user == "paper":
        if computer == "scissors":
            print("You lose!")
        else:
            print("You win!")
    elif user == "scissors":
        if computer == "rock":
            print("You lose!")
        else:
            print("You win!")
    else:
        print("Invalid input")
    
    if input("Play again? (y/n) ").lower() != "y": # ask user if they want to play again
        break # exit loop

```

If you find it hard to read either of the above examples, try going through line by line, and writing down what each line is doing. Keep indentation
in mind, and remember that all of the code that is indented is part of the loop. This is called "pseudocode", and it is a good way to understand
what a program is doing.

Sometimes when you have an idea, but are having trouble writing the code, it can help to write pseudocode first, and then write the code based on
the pseudocode.

[Back](../00/) |
[Next](../02/)

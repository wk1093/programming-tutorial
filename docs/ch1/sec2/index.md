# Chapter 1: Introduction to C

## Section 2: Variables and Data Types

In C, variables are used to store and manipulate data. Before using a variable, you need to declare it with a specific data type. C provides various built-in data types, each serving a specific purpose. Let's explore some commonly used data types:

### Integer Types

- **int:** Used to store whole numbers. It typically occupies 4 bytes of memory.
- **short:** Used to store smaller whole numbers. It usually occupies 2 bytes of memory.
- **long:** Used to store larger whole numbers. It typically occupies 4 or 8 bytes of memory, depending on the system.
- **unsigned int, unsigned short, unsigned long:** Similar to their signed counterparts, but they only store positive numbers.

### Floating-Point Types

- **float:** Used to store decimal numbers with single-precision. It typically occupies 4 bytes of memory.
- **double:** Used to store decimal numbers with double-precision. It usually occupies 8 bytes of memory.
- **long double:** Used to store decimal numbers with extended precision. It can occupy 8 or 16 bytes of memory, depending on the system.

### Character Types

- **char:** Used to store individual characters. It typically occupies 1 byte of memory.
- **signed char, unsigned char:** Similar to `char`, but explicitly specifying the signedness.

### Other Data Types

- **_Bool:** Used to represent boolean values. It can have two states: `0` (false) or non-zero (true).
- **void:** Represents the absence of a value. It is commonly used as a return type or for declaring generic pointers.

### Declaring Variables

To declare a variable, you need to specify its data type and provide a name. Here's the general syntax:

```c
data_type variable_name;
```

For example, to declare an integer variable named `age`, you would write:

```c
int age;
```

### Initializing Variables

Variables can be initialized with an initial value at the time of declaration. Here's an example:

```c
int score = 100;
```

### Variable Naming Rules

When naming variables, follow these rules:

- Variable names can contain letters, digits, and underscores.
- The first character must be a letter or an underscore.
- Variable names are case-sensitive.
- Avoid using reserved keywords as variable names.

### Variable Assignment

To assign a value to a variable, use the assignment operator (`=`). Here's an example:

```c
int x;
x = 10;
```

You can also assign a value directly during declaration:

```c
int y = 20;
```

### Type Modifiers

C provides type modifiers to further specify the range or size of a data type. Some common modifiers include `short`, `long`, and `unsigned`. For example:

```c
short int count;
unsigned long int distance;
```

Understanding variables and data types is crucial for writing effective C programs. They allow you to store, manipulate, and represent different types of data. In the upcoming sections, we'll explore more about variables, data types, and how to work with them in C.

Let's continue our journey into the world of C programming and dive deeper into these concepts!
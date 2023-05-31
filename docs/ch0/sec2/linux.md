# Setting Up Your Development Environment on Linux

If you're using Linux, here's a detailed guide on setting up your development environment for coding in C and Python using the `sudo apt` package manager:

1. Ensure that the `sudo` command is available on your system:
   - Open a terminal and run the command `sudo apt update`.
   - If prompted, enter your user password to execute the command.
   - If the command runs successfully, you have `sudo` access. Otherwise, consult your system administrator for assistance.

2. Install a text editor or integrated development environment (IDE):
   - Visual Studio Code (VS Code) is a popular choice. Install it using the following commands:
     ```
     sudo apt update
     sudo apt install code
     ```
   - To install PyCharm, you can follow the JetBrains Toolbox installation instructions. Alternatively, you can use VS Code for Python development as well.

3. Install the necessary compilers and tools:
   - For C programming, install the GCC compiler and related build tools using the following command:
     ```
     sudo apt update
     sudo apt install build-essential
     ```
   - For Python, most Linux distributions come with Python pre-installed. To ensure you have the latest version, use the following command:
     ```
     sudo apt update
     sudo apt install python3
     ```

4. Test your setup:
   - Open a terminal and try compiling and running a C program by navigating to the directory containing your C file and using the `gcc` command to compile it. For example:
     ```
     cd /path/to/your/c/program
     gcc -o program program.c
     ./program
     ```
   - To run a Python program, navigate to the directory containing your Python file and execute it using the `python3` command. For example:
     ```
     cd /path/to/your/python/program
     python3 program.py
     ```

These steps should help you set up your development environment for C and Python programming on Linux using the `sudo apt` package manager. Remember to keep your system and development tools updated to benefit from the latest features and security patches. Happy coding!

[Back](index.md)
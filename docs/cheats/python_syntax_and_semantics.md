# Python Syntax and Semantics: Understanding the Basics

## Understanding Python Programming Language

| Title                       | Concept                                                          | Description                                                |
|-----------------------------|------------------------------------------------------------------|------------------------------------------------------------|
| Overview of Python          | Python is a versatile, high-level programming language.         | Widely used for various applications like web development and data analysis. |
| Importance of Python in the Programming World | Known for its simplicity, readability, and vast ecosystem of libraries. | Facilitates rapid development and fosters a strong community of developers. |

## Key Differentiators of Python Syntax

| Title                       | Concept                                                          | Description                                                |
|-----------------------------|------------------------------------------------------------------|------------------------------------------------------------|
| Indentation                 | Indicates code blocks with spaces or tabs consistently.         | Mandatory for code structure and improves readability.     |
| Simplicity and Readability  | Emphasizes clear and simple syntax for developers.              | Enhances code maintenance, debugging, and collaboration.   |

# Basic Python Syntax: Fundamentals for Code Structure

## Statements and Comments

| Title                       | Concept                                                          | Code                                                       |
|-----------------------------|------------------------------------------------------------------|------------------------------------------------------------|
| Python Statement Syntax     | Statements end with a newline character in Python.              | `x = 5` <br> `if x > 0:` <br> &nbsp; &nbsp; `print("Positive")` |
| Importance of Comments      | Comments start with `#` and provide documentation or clarity.   | `# This is a comment` <br> `print("Hello, World!")`          |

## Variables and Data Types

| Title                       | Concept                                                          | Code                                                       |
|-----------------------------|------------------------------------------------------------------|------------------------------------------------------------|
| Variable Naming Convention  | Descriptive names with lowercase and underscores for readability. | `my_variable = 10`                                        |
| Data Types in Python        | Includes int, float, str, list, tuple, and dict among others.   | `a = 10` <br> `b = 3.14` <br> `c = "Python"`              |

## Operators

| Title                       | Concept                                                          | Code                                                       |
|-----------------------------|------------------------------------------------------------------|------------------------------------------------------------|
| Arithmetic Operators        | Perform basic mathematical operations in Python.                | `x = 10` <br> `y = 3` <br> `result = x + y`                |
| Comparison Operators        | Compare values and return boolean results for conditions.       | `a = 5` <br> `b = 10` <br> `is_greater = a > b`            |
| Logical Operators           | Combine conditions using logical operators in Python.           | `x = 5` <br> `if x > 0 and x % 2 == 0:` <br> &nbsp; &nbsp; `print("Positive and even")` |

## Control Flow Structures

| Title                       | Concept                                                          | Code                                                       |
|-----------------------------|------------------------------------------------------------------|------------------------------------------------------------|
| Conditional Statements      | Execute code based on specified conditions.                     | `x = 10` <br> `if x > 0:` <br> &nbsp; &nbsp; `print("Positive")` |
| Loops                       | Repeat code block until a specific condition is met.            | `for i in range(5):` <br> &nbsp; &nbsp; `print(i)`           |
| Break and Continue Statements | Change loop flow by exiting or skipping iterations.             | `for i in range(10):` <br> &nbsp; &nbsp; `if i == 5:` <br> &nbsp; &nbsp; &nbsp; &nbsp; `break` |

# Functions and Modules in Python: Building Blocks of Reusability

## Defining Functions

| Title                       | Concept                                                          | Code                                                       |
|-----------------------------|------------------------------------------------------------------|------------------------------------------------------------|
| Function Declaration Syntax | Define reusable code blocks with the `def` keyword in Python.   | `def greet(name):` <br> &nbsp; &nbsp; `return f"Hello, {name}!"` |
| Parameters and Return Values | Pass inputs and get outputs from functions in Python.            | `def add(a, b):` <br> &nbsp; &nbsp; `return a + b` <br> `result = add(3, 5)` |

## Built-in Functions

| Title                       | Concept                                                          | Code                                                       |
|-----------------------------|------------------------------------------------------------------|------------------------------------------------------------|
| Common Built-in Functions   | Python offers diverse functions for numerous operations.       | `print(len([1, 2, 3]))` <br> `print(type("Hello"))`        |
| Example of Built-in Functions | Examples include `print()`, `len()`, `type()`, `range()`, `sum()`, and more. | -                                                      |

## Importing and Using Modules

| Title                       | Concept                                                          | Code                                                       |
|-----------------------------|------------------------------------------------------------------|------------------------------------------------------------|
| Importing Modules           | Include external libraries or modules into Python programs.     | `import math` <br> `print(math.pi)`                         |
| Module Aliasing             | Assign aliases to modules for easier access and usage.          | `import numpy as np` <br> `print(np.array([1, 2, 3]))`       |

## Creating Custom Modules

| Title                       | Concept                                                          | Code                                                       |
|-----------------------------|------------------------------------------------------------------|------------------------------------------------------------|
| Modularizing Code           | Organize code into modules for better structure and reuse.      | `# module.py` <br> `def square(x):` <br> &nbsp; &nbsp; `return x ** 2` |
| Using Custom Module Functions | Access and utilize functions from custom modules.               | `import module` <br> `result = module.square(5)` <br> `print(result)` |

# Object-Oriented Programming (OOP) in Python: Structuring Code with Classes and Objects

## Classes and Objects

| Title                       | Concept                                                          | Code                                                       |
|-----------------------------|------------------------------------------------------------------|------------------------------------------------------------|
| Defining Classes            | Outline object blueprints with attributes and methods in Python. | `class Car:` <br> &nbsp; &nbsp; `def __init__(self, brand):` <br> &nbsp; &nbsp; &nbsp; &nbsp; `self.brand = brand` |
| Creating Objects            | Instantiate objects based on defined classes.                    | `car1 = Car("Toyota")` <br> `print(car1.brand)`             |

## Inheritance

| Title                       | Concept                                                          | Code                                                       |
|-----------------------------|------------------------------------------------------------------|------------------------------------------------------------|
| Inheritance Definition      | Create new classes derived from existing ones for reuse and extension. | `class ElectricCar(Car):` <br> &nbsp; &nbsp; `def __init__(self, brand, battery):` <br> &nbsp; &nbsp; &nbsp; &nbsp; `super().__init__(brand)`  |
| Types of Inheritance        | Includes single, multiple, multilevel, and hierarchical inheritance. | `class A:` <br> `class B(A):`                               |

## Polymorphism

| Title                       | Concept                                                          | Code                                                       |
|-----------------------------|------------------------------------------------------------------|------------------------------------------------------------|
| Understanding Polymorphism  | Treat objects from different classes as a common superclass.    | `class Shape:` <br> &nbsp; &nbsp; `def area(self):`           |
| Method Overriding           | Customize inherited methods in subclasses for specific behavior. | `class Rectangle(Shape):` <br> &nbsp; &nbsp; `def area(self):` |

## Encapsulation

| Title                       | Concept                                                          | Code                                                       |
|-----------------------------|------------------------------------------------------------------|------------------------------------------------------------|
| Encapsulation in Python     | Control access to attributes and methods within a class.        | `class BankAccount:` <br> &nbsp; &nbsp; `def __init__(self, balance):` <br> &nbsp; &nbsp; &nbsp; &nbsp; `self.__balance = balance` |
| Access Modifiers            | Use double underscores to denote private variables for data protection. | `class MyClass:` <br> &nbsp; &nbsp; `def __init__(self):` <br> &nbsp; &nbsp; &nbsp; &nbsp; `self.__private_var = 10` |

By mastering these fundamental Python concepts, you can efficiently structure code, enable reusability, and develop robust applications.
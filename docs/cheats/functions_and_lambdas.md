
# Functions and Lambdas in Python

## Introduction to Functions

| Title                       | Concept                                                            | Codes                                    |
|-----------------------------|--------------------------------------------------------------------|------------------------------------------|
| What are Functions?         | Blocks of reusable code that perform a specific task.              | Encapsulate logic, promote code reuse, and enhance code modularity. |
| Function Syntax in Python   | Define functions, arguments, and return values in Python.         | Functions are defined using the `def` keyword with optional parameters and return statements. |
| Purpose of Functions        | Modularity, Reusability, and Improved Code Organization.          | Functions break down complex systems into manageable components and streamline code maintenance. |

### 1. Defining Functions

1. Function Syntax:
   ```python
   def my_function(param1, param2):
       # Function code here
       return result
   ```

2. Function Arguments:
   - Positional Arguments
   - Keyword Arguments
   - Default Arguments
   - Variable-Length Arguments

3. Function Returns:
   - Optional return statement
   - Can return single or multiple values

## Working with Functions

### Function Parameters

| Title                       | Concept                                                            | Codes                                    |
|-----------------------------|--------------------------------------------------------------------|------------------------------------------|
| Positional Parameters       | Arguments passed based on order.                                   |`def greet(name, message):`<br>&nbsp;&nbsp;&nbsp;&nbsp;`print(f"Hello, {name}! {message}")` |
| Keyword Parameters          | Arguments passed based on names provided.                         |`greet(message="How are you?", name="Alice")` |
| Default Parameters          | Predefined values for function arguments.                         |`def greet(name, message="Good day!"):`<br>&nbsp;&nbsp;&nbsp;&nbsp;`print(f"Hello, {name}! {message}")` |
| Variable-Length Arguments   | Handle arbitrary number of arguments.                             |`def sum_values(*args):`<br>&nbsp;&nbsp;&nbsp;&nbsp;`return sum(args)` |

### Function Scope

| Title                       | Concept                                                            | Codes                                    |
|-----------------------------|--------------------------------------------------------------------|------------------------------------------|
| Global vs. Local Scope       | Differentiating variable accessibility within functions.           |Global variables accessible throughout, local variables limited to function scope. |
| Accessing Variables in Different Scopes | Utilizing variables with specific scopes.                        |`global_var = 10`<br>`def my_func():`<br>&nbsp;&nbsp;&nbsp;&nbsp;`local_var = 5` |
| The 'global' Keyword         | Modifying global variables within function scope.                 |`def change_global_value():`<br>&nbsp;&nbsp;&nbsp;&nbsp;`global global_var`<br>&nbsp;&nbsp;&nbsp;&nbsp;`global_var = 20` |

### Lambda Functions

| Title                       | Concept                                                            | Codes                                    |
|-----------------------------|--------------------------------------------------------------------|------------------------------------------|
| Definition and Syntax       | Anonymous functions defined in a single line.                     |`lambda x, y: x + y` |
| Advantages of Lambda Functions | Concise, no need for `def` keyword, used for short functions.     |`lambda x: x**2 if x > 0 else 0` |
| Use Cases for Lambda Functions | Functional programming, data transformations, quick functions.    |`list(map(lambda x: x+2, [1, 2, 3]))` |

## Built-in Functions in Python

### Common Built-in Functions

1. print() Function
2. len() Function
3. range() Function

### map() Function

1. Using map() with Functions
   ```python
   numbers = [1, 2, 3]
   squared = list(map(lambda x: x**2, numbers))
   ```

2. Lambda Functions with map()
   ```python
   names = ['Alice', 'Bob', 'Charlie']
   lengths = list(map(lambda x: len(x), names))
   ```

### filter() Function

1. Using filter() with Functions
   ```python
   numbers = [1, 2, 3, 4, 5]
   even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
   ```

2. Lambda Functions with filter()
   ```python
   names = ['Alice', 'Bob', 'Charlie']
   long_names = list(filter(lambda x: len(x) > 5, names))
   ```

## Recursion in Python

### Understanding Recursion

1. Definition and Concepts
   - A function calling itself
   - Breaks a problem into smaller, similar subproblems

2. Recursive Functions
   - Must have a base case to terminate
   - Examples: Factorial, Fibonacci

### Advantages and Limitations

1. Pros of Recursion
   - Elegant solutions for some problems
   - Improves readability for certain algorithms

2. Common Pitfalls and Limitations
   - Stack overflow with excessive recursion
   - Harder to debug compared to iterative solutions

### Recursive Examples

1. Writing Recursive Functions
   ```python
   def factorial(n):
       if n == 1:
           return 1
       else:
           return n * factorial(n - 1)
   ```

2. Recursion vs. Iteration
   - Recursion: Compact and elegant
   - Iteration: Better for performance in some cases

## Functional Programming Concepts

### Pure Functions

1. Definition and Characteristics
   - Output solely determined by input
   - No side effects

2. Benefits of Pure Functions
   - Easier to test and debug
   - Enables parallel and concurrent execution

### Higher-Order Functions

1. Definition and Examples
   - Functions that take other functions as arguments
   - Examples: `map()`, `filter()`

2. Using Functions as Parameters
   - Enhances code reusability and flexibility
   - Example: `sorted()`

### Immutability and Higher-Order Functions

1. Understanding Immutability
   - Data that cannot be changed after creation
   - Promotes functional programming principles

2. Applying Higher-Order Functions with Immutable Data
   - Avoids unintended data changes
   - Supports functional programming paradigms
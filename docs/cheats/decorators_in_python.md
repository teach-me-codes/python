# Decorators in Python

## Introduction to Decorators

| Title                       | Concept                                                            | Codes                                           |
|-----------------------------|--------------------------------------------------------------------|------------------------------------------------|
| **What are Decorators?**    | Functions that modify or extend the behavior of functions or methods. | Decorators are used to alter the functionality of other functions without changing their code. |
|                             | Definition and Purpose                                          | Allow for adding functionality to existing functions dynamically. |
|                             | Role in Python Programming                                      | Provide a clean and efficient way to modify functions at runtime. |
| **Advantages of Using Decorators** | Enhances code structure and readability.                       | Promotes code reusability and simplifies maintenance. |
|                             | Code Reusability                                                | Define a decorator once and apply it to multiple functions. |
|                             | Separation of Concerns                                          | Keep different aspects of a program separate and modular. |

## Creating and Using Decorators

| Title                       | Concept                                                            | Codes                                           |
|-----------------------------|--------------------------------------------------------------------|------------------------------------------------|
| **Defining a Decorator Function** | Building functions that modify the behavior of other functions. |<pre lang="python">def my_decorator(func):<br>    def wrapper():<br>        # Add extra functionality<br>        return func()<br>    return wrapper<br>@my_decorator<br>def greet():<br>    return "Hello!"</pre>|
|                             | Syntax and Structure                                            | Define a function that takes another function as an argument. |
|                             | Implementing Decorators                                         | Inside the decorator, wrap the original function and add extra logic. |
| **Applying Decorators to Functions** | Enhancing the functionality of existing functions.               | Use the `@decorator_name` syntax before the function definition. |
|                             | Using the @symbol                                               | An easy way to apply a decorator to a function. |
|                             | Multiple Decorators on a Single Function                        | Apply multiple decorators in a chained manner. |
| **Common Use Cases for Decorators** | Improving code readability and maintenance.                       | Implement functionalities like logging, timing, and access control. |
|                             | Logging and Timing Functions                                    | Track function execution time and log important information. |
|                             | Authorization and Access Control                                | Restrict access to specific functions based on user privileges. |

## Built-in Decorators in Python

| Title                       | Concept                                                            | Codes                                           |
|-----------------------------|--------------------------------------------------------------------|------------------------------------------------|
| **Introduction to Built-in Decorators** | Predefined decorators in Python for common tasks.                | Includes @property, @staticmethod, and @classmethod. |
|                             | Overview of @property, @staticmethod, @classmethod                | Each decorator serves a specific purpose in Python classes. |
|                             | Understanding their Applications                                 | Apply built-in decorators to improve class functionality. |
| **@property Decorator**     | Property-based access control for class attributes.              |<pre lang="python">class MyClass:<br>    def __init__(self):<br>        self._my_attr = None<br>    @property<br>    def my_attr(self):<br>        return self._my_attr</pre>|
|                             | Definition and Usage                                            | Creates a property for accessing and modifying class attributes. |
|                             | Getter, Setter, Deleter Methods                                 | Implement methods for retrieving, setting, and deleting property values. |
| **@staticmethod Decorator**  | Declaring static methods that belong to a class.                |<pre lang="python">class MyClass:<br>    @staticmethod<br>    def my_static_method():<br>        return "Static Method"</pre>|
|                             | Definition and Usage                                            | Use static methods without access to instance variables. |
|                             | Static Methods vs. Instance Methods                             | Functionality not dependent on instance state or attributes. |
| **@classmethod Decorator**   | Creating methods that operate on the class itself, not instances. |<pre lang="python">class MyClass:<br>    class_variable = 0<br>    @classmethod<br>    def update_class_variable(cls, value):<br>        cls.class_variable += value</pre>|
|                             | Definition and Usage                                            | Modify class state across all instances. |
|                             | Class Methods and Instance Methods                              | Differentiate between actions related to class and instance objects. |

## Custom Decorators

| Title                       | Concept                                                            | Codes                                           |
|-----------------------------|--------------------------------------------------------------------|------------------------------------------------|
| **Implementing Custom Decorators** | Developing decorators tailored to specific needs.               |<pre lang="python">def my_custom_decorator(func):<br>    def wrapper(*args, **kwargs):<br>        # Custom logic here<br>        return func(*args, **kwargs)<br>    return wrapper</pre>|
|                             | Writing Custom Decorator Functions                               | Customize decorators for specific functionalities. |
|                             | Decorators with Arguments                                       | Allow decorators to accept arguments for dynamic behavior. |
| **Chaining Decorators**      | Applying multiple decorators sequentially.                      |<pre lang="python">@decorator1<br>@decorator2<br>def my_function():<br>    pass</pre>|
|                             | Using Multiple Custom Decorators                                | Combine multiple decorators for complex functionality. |
|                             | Order of Execution in Decorator Chaining                         | Apply decorators from top to bottom in sequential order. |
| **Practical Examples of Custom Decorators** | Enhancing function behavior in real-world scenarios.          | Implement decorators for error handling and performance optimization. |
|                             | Error Handling Decorators                                       | Capture and handle exceptions in functions elegantly. |
|                             | Performance Optimization Decorators                              | Implement decorators to optimize function execution speed. |

## Decorators with Parameters

| Title                       | Concept                                                            | Codes                                           |
|-----------------------------|--------------------------------------------------------------------|------------------------------------------------|
| **Passing Parameters to Decorators** | Customizing decorator behavior with arguments.                   |<pre lang="python">def parametrized_decorator(param):<br>    def decorator(func):<br>        def wrapper(*args, **kwargs):<br>            # Use param here<br>            return func(*args, **kwargs)<br>        return wrapper<br>    return decorator</pre>|
|                             | Adding Arguments to Decorator Functions                          | Make decorators more flexible by accepting parameters. |
|                             | Using Parameters in Decorator Logic                              | Incorporate parameter values directly in the decorator logic. |
| **Decorators with Variable Number of Arguments** | Handling multiple arguments in decorator functions.            |<pre lang="python">def variable_args_decorator(func):<br>    def wrapper(*args, **kwargs):<br>        # Process variable args and kwargs<br>        return func(*args, **kwargs)<br>    return wrapper</pre>|
|                             | Handling *args and **kwargs                                     | Utilize the flexibility of Python's variable-length arguments. |
|                             | Dynamic Parameter Handling in Decorators                         | Adjust decorator behavior based on varying parameter inputs. |
| **Examples of Decorators with Parameters** | Practical use cases for parameterized decorators.               | Implement decorators like timers and conditional decorators. |
|                             | Parameterized Timer Decorator                                   | Time the execution of functions with adjustable parameters. |
|                             | Conditional Decorators based on Parameters                       | Apply decorators conditionally based on specified criteria. |

## Decorator Use Cases and Best Practices

| Title                       | Concept                                                            | Description                                    |
|-----------------------------|--------------------------------------------------------------------|------------------------------------------------|
| **Common Use Cases for Decorators** | Practical scenarios where decorators shine.                    | Implement functionalities like caching and validation. |
|                             | Caching Function Results                                        | Improve performance by caching results of expensive functions. |
|                             | Input Validation and Sanitization                               | Ensure data integrity and security through validation decorators. |
| **Best Practices when Using Decorators** | Guidelines for effective and maintainable decorator usage.     | Follow best practices to write clean and efficient decorator functions. |
|                             | Keeping Decorator Logic Simple                                  | Maintain readability by separating concerns and keeping decorators concise. |
|                             | Documenting Decorator Functions                                 | Provide clear documentation to aid understanding and usage. |
| **Performance Considerations with Decorators** | Impact of decorators on code execution and efficiency.          | Understand the performance implications of decorator usage. |
|                             | Impact on Code Execution Time                                   | Measure and optimize code execution when applying decorators. |
|                             | Avoiding Overuse of Decorators                                   | Balance functionality enhancements with code complexity and performance. |

By mastering these decorator concepts, you can enhance the flexibility, readability, and functionality of your Python code effectively.
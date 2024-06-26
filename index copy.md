
# Welcome to Python Learning Portal

<style>
.circular-nav {
    position: relative;
    width: 400px; /* Increase width to accommodate the fourth button */
    height: 100px;
    background-color: white;
    display: flex;
    justify-content: space-evenly;
    align-items: center;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    border-radius: 25px; /* Rounded corners */
}

.nav-button {
    width: 80px;
    height: 80px;
    border-radius: 50%;
    background-color: #0073e6;
    border: 2px solid #0073e6;
    font-size: 12px;
    color: #ffffff;
    cursor: pointer;
    display: flex;
    justify-content: center;
    align-items: center;
    transition: transform 0.2s, box-shadow 0.2s;
}

.nav-button:hover {
    transform: scale(1.1);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
}

.nav-button i {
    margin-right: 8px; /* Space between icon and text */
}
</style>

<div class="circular-nav">
    <button class="nav-button" id="theory"><i class="fas fa-book"></i> Theory</button>
    <button class="nav-button" id="projects"><i class="fas fa-laptop"></i> Projects</button>
    <button class="nav-button" id="questions"><i class="fas fa-lightbulb"></i> Q&A</button>
    <button class="nav-button" id="cheatsheets"><i class="fas fa-text"></i> Cheat Sheets</button>
</div>

<script>
document.getElementById('theory').onclick = function() {
    window.location.href = 'theory.html';
};
document.getElementById('projects').onclick = function() {
    window.location.href = 'projects.html';
};
document.getElementById('questions').onclick = function() {
    window.location.href = 'questions.html';
};
document.getElementById('cheatsheets').onclick = function() {
    window.location.href = 'cheatsheets.html';
};
</script>




| Book <br> Chapters | Selected <br> Projects | Questions  & <br> Answers | Cheat <br> Sheets | References |
|--------|----------|-----|--------------|------------|
|[Introduction to <br> Python](https://learning.teachme.codes/chapters/introduction_to_python)|[Introduction to <br> Projects](https://learning.teachme.codes/projects/introduction_to_projects)|[Introduction to <br> QnAs](https://learning.teachme.codes/qnas/introduction_to_python)|[Introduction to <br> Cheats](https://learning.teachme.codes/cheats/introduction_to_python)|[Introduction to <br> Python](https://learning.teachme.codes/python/introduction_to_python)|
|[Python Syntax and <br> Semantics](https://learning.teachme.codes/chapters/python_syntax_and_semantics)|[Python Syntax and <br> Projects](https://learning.teachme.codes/projects/python_syntax_and_semantics)|[Python Syntax and <br> QnAs](https://learning.teachme.codes/qnas/python_syntax_and_semantics)|[Python Syntax and <br> Cheats](https://learning.teachme.codes/cheats/python_syntax_and_semantics)|[Python Syntax and <br> Semantics](https://learning.teachme.codes/python/python_syntax_and_semantics)|
|[Variables and <br> Data Types](https://learning.teachme.codes/chapters/variables_and_data_types)|[Variables and <br> Projects](https://learning.teachme.codes/projects/variables_and_data_types)|[Variables and <br> QnAs](https://learning.teachme.codes/qnas/variables_and_data_types)|[Variables and <br> Cheats](https://learning.teachme.codes/cheats/variables_and_data_types)|[Variables and <br> Data Types](https://learning.teachme.codes/python/variables_and_data_types)|
|[Control Flow <br> Statements](https://learning.teachme.codes/chapters/control_flow_statements)|[Control Flow <br> Projects](https://learning.teachme.codes/projects/control_flow_statements)|[Control Flow <br> QnAs](https://learning.teachme.codes/qnas/control_flow_statements)|[Control Flow <br> Cheats](https://learning.teachme.codes/cheats/control_flow_statements)|[Control Flow <br> Statements](https://learning.teachme.codes/python/control_flow_statements)|
|[Functions and <br> Lambdas](https://learning.teachme.codes/chapters/functions_and_lambdas)|[Functions and <br> Projects](https://learning.teachme.codes/projects/functions_and_lambdas)|[Functions and <br> QnAs](https://learning.teachme.codes/qnas/functions_and_lambdas)|[Functions and <br> Cheats](https://learning.teachme.codes/cheats/functions_and_lambdas)|[Functions and <br> Lambdas](https://learning.teachme.codes/python/functions_and_lambdas)|
|[Exception <br> Handling](https://learning.teachme.codes/chapters/exception_handling)|[Exception <br> Projects](https://learning.teachme.codes/projects/exception_handling)|[Exception <br> QnAs](https://learning.teachme.codes/qnas/exception_handling)|[Exception <br> Cheats](https://learning.teachme.codes/cheats/exception_handling)|[Exception <br> Handling](https://learning.teachme.codes/python/exception_handling)|
|[File IO <br> Operations](https://learning.teachme.codes/chapters/file_io_operations)|[File IO <br> Projects](https://learning.teachme.codes/projects/file_io_operations)|[File IO <br> QnAs](https://learning.teachme.codes/qnas/file_io_operations)|[File IO <br> Cheats](https://learning.teachme.codes/cheats/file_io_operations)|[File IO <br> Operations](https://learning.teachme.codes/python/file_io_operations)|
|[List <br> Comprehensions](https://learning.teachme.codes/chapters/list_comprehensions)|[List <br> Projects](https://learning.teachme.codes/projects/list_comprehensions)|[List <br> QnAs](https://learning.teachme.codes/qnas/list_comprehensions)|[List <br> Cheats](https://learning.teachme.codes/cheats/list_comprehensions)|[List <br> Comprehensions](https://learning.teachme.codes/python/list_comprehensions)|
|[Generators and <br> Iterators](https://learning.teachme.codes/chapters/generators_and_iterators)|[Generators and <br> Projects](https://learning.teachme.codes/projects/generators_and_iterators)|[Generators and <br> QnAs](https://learning.teachme.codes/qnas/generators_and_iterators)|[Generators and <br> Cheats](https://learning.teachme.codes/cheats/generators_and_iterators)|[Generators and <br> Iterators](https://learning.teachme.codes/python/generators_and_iterators)|
|[Decorators in <br> Python](https://learning.teachme.codes/chapters/decorators_in_python)|[Decorators in <br> Projects](https://learning.teachme.codes/projects/decorators_in_python)|[Decorators in <br> QnAs](https://learning.teachme.codes/qnas/decorators_in_python)|[Decorators in <br> Cheats](https://learning.teachme.codes/cheats/decorators_in_python)|[Decorators in <br> Python](https://learning.teachme.codes/python/decorators_in_python)|
|[Context <br> Managers](https://learning.teachme.codes/chapters/context_managers)|[Context <br> Projects](https://learning.teachme.codes/projects/context_managers)|[Context <br> QnAs](https://learning.teachme.codes/qnas/context_managers)|[Context <br> Cheats](https://learning.teachme.codes/cheats/context_managers)|[Context <br> Managers](https://learning.teachme.codes/python/context_managers)|
|[Modules and <br> Packages](https://learning.teachme.codes/chapters/modules_and_packages)|[Modules and <br> Projects](https://learning.teachme.codes/projects/modules_and_packages)|[Modules and <br> QnAs](https://learning.teachme.codes/qnas/modules_and_packages)|[Modules and <br> Cheats](https://learning.teachme.codes/cheats/modules_and_packages)|[Modules and <br> Packages](https://learning.teachme.codes/python/modules_and_packages)|
|[Virtual <br> Environments](https://learning.teachme.codes/chapters/virtual_environments)|[Virtual <br> Projects](https://learning.teachme.codes/projects/virtual_environments)|[Virtual <br> QnAs](https://learning.teachme.codes/qnas/virtual_environments)|[Virtual <br> Cheats](https://learning.teachme.codes/cheats/virtual_environments)|[Virtual <br> Environments](https://learning.teachme.codes/python/virtual_environments)|
|[Python Standard <br> Library](https://learning.teachme.codes/chapters/python_standard_library)|[Python Standard <br> Projects](https://learning.teachme.codes/projects/python_standard_library)|[Python Standard <br> QnAs](https://learning.teachme.codes/qnas/python_standard_library)|[Python Standard <br> Cheats](https://learning.teachme.codes/cheats/python_standard_library)|[Python Standard <br> Library](https://learning.teachme.codes/python/python_standard_library)|
|[Regular <br> Expressions](https://learning.teachme.codes/chapters/regular_expressions)|[Regular <br> Projects](https://learning.teachme.codes/projects/regular_expressions)|[Regular <br> QnAs](https://learning.teachme.codes/qnas/regular_expressions)|[Regular <br> Cheats](https://learning.teachme.codes/cheats/regular_expressions)|[Regular <br> Expressions](https://learning.teachme.codes/python/regular_expressions)|
|[Using <br> map_filter_reduce](https://learning.teachme.codes/chapters/using_map_filter_reduce)|[Using <br> Projects](https://learning.teachme.codes/projects/using_map_filter_reduce)|[Using <br> QnAs](https://learning.teachme.codes/qnas/using_map_filter_reduce)|[Using <br> Cheats](https://learning.teachme.codes/cheats/using_map_filter_reduce)|[Using <br> map_filter_reduce](https://learning.teachme.codes/python/using_map_filter_reduce)|
|[String Manipulation <br> Functions](https://learning.teachme.codes/chapters/string_manipulation_functions)|[String Manipulation <br> Projects](https://learning.teachme.codes/projects/string_manipulation_functions)|[String Manipulation <br> QnAs](https://learning.teachme.codes/qnas/string_manipulation_functions)|[String Manipulation <br> Cheats](https://learning.teachme.codes/cheats/string_manipulation_functions)|[String Manipulation <br> Functions](https://learning.teachme.codes/python/string_manipulation_functions)|
|[Numeric and Math <br> Functions](https://learning.teachme.codes/chapters/numeric_and_math_functions)|[Numeric and Math <br> Projects](https://learning.teachme.codes/projects/numeric_and_math_functions)|[Numeric and Math <br> QnAs](https://learning.teachme.codes/qnas/numeric_and_math_functions)|[Numeric and Math <br> Cheats](https://learning.teachme.codes/cheats/numeric_and_math_functions)|[Numeric and Math <br> Functions](https://learning.teachme.codes/python/numeric_and_math_functions)|
|[Data Structure <br> Functions](https://learning.teachme.codes/chapters/data_structure_functions)|[Data Structure <br> Projects](https://learning.teachme.codes/projects/data_structure_functions)|[Data Structure <br> QnAs](https://learning.teachme.codes/qnas/data_structure_functions)|[Data Structure <br> Cheats](https://learning.teachme.codes/cheats/data_structure_functions)|[Data Structure <br> Functions](https://learning.teachme.codes/python/data_structure_functions)|
|[Date and Time <br> Functions](https://learning.teachme.codes/chapters/date_and_time_functions)|[Date and Time <br> Projects](https://learning.teachme.codes/projects/date_and_time_functions)|[Date and Time <br> QnAs](https://learning.teachme.codes/qnas/date_and_time_functions)|[Date and Time <br> Cheats](https://learning.teachme.codes/cheats/date_and_time_functions)|[Date and Time <br> Functions](https://learning.teachme.codes/python/date_and_time_functions)|
|[Input and Output <br> Functions](https://learning.teachme.codes/chapters/input_and_output_functions)|[Input and Output <br> Projects](https://learning.teachme.codes/projects/input_and_output_functions)|[Input and Output <br> QnAs](https://learning.teachme.codes/qnas/input_and_output_functions)|[Input and Output <br> Cheats](https://learning.teachme.codes/cheats/input_and_output_functions)|[Input and Output <br> Functions](https://learning.teachme.codes/python/input_and_output_functions)|
|[Built-in Sorting and <br> Searching](https://learning.teachme.codes/chapters/built_in_sorting_and_searching)|[Built-in Sorting and <br> Projects](https://learning.teachme.codes/projects/built_in_sorting_and_searching)|[Built-in Sorting and <br> QnAs](https://learning.teachme.codes/qnas/built_in_sorting_and_searching)|[Built-in Sorting and <br> Cheats](https://learning.teachme.codes/cheats/built_in_sorting_and_searching)|[Built-in Sorting and <br> Searching](https://learning.teachme.codes/python/built_in_sorting_and_searching)|
|[Type Conversion <br> Functions](https://learning.teachme.codes/chapters/type_conversion_functions)|[Type Conversion <br> Projects](https://learning.teachme.codes/projects/type_conversion_functions)|[Type Conversion <br> QnAs](https://learning.teachme.codes/qnas/type_conversion_functions)|[Type Conversion <br> Cheats](https://learning.teachme.codes/cheats/type_conversion_functions)|[Type Conversion <br> Functions](https://learning.teachme.codes/python/type_conversion_functions)|
|[Object-Oriented <br> Functions](https://learning.teachme.codes/chapters/object_oriented_functions)|[Object-Oriented <br> Projects](https://learning.teachme.codes/projects/object_oriented_functions)|[Object-Oriented <br> QnAs](https://learning.teachme.codes/qnas/object_oriented_functions)|[Object-Oriented <br> Cheats](https://learning.teachme.codes/cheats/object_oriented_functions)|[Object-Oriented <br> Functions](https://learning.teachme.codes/python/object_oriented_functions)|
|[Classes and <br> Objects](https://learning.teachme.codes/chapters/classes_and_objects)|[Classes and <br> Projects](https://learning.teachme.codes/projects/classes_and_objects)|[Classes and <br> QnAs](https://learning.teachme.codes/qnas/classes_and_objects)|[Classes and <br> Cheats](https://learning.teachme.codes/cheats/classes_and_objects)|[Classes and <br> Objects](https://learning.teachme.codes/python/classes_and_objects)|
|[Inheritance and <br> Polymorphism](https://learning.teachme.codes/chapters/inheritance_and_polymorphism)|[Inheritance and <br> Projects](https://learning.teachme.codes/projects/inheritance_and_polymorphism)|[Inheritance and <br> QnAs](https://learning.teachme.codes/qnas/inheritance_and_polymorphism)|[Inheritance and <br> Cheats](https://learning.teachme.codes/cheats/inheritance_and_polymorphism)|[Inheritance and <br> Polymorphism](https://learning.teachme.codes/python/inheritance_and_polymorphism)|
|[Encapsulation and <br> Abstraction](https://learning.teachme.codes/chapters/encapsulation_and_abstraction)|[Encapsulation and <br> Projects](https://learning.teachme.codes/projects/encapsulation_and_abstraction)|[Encapsulation and <br> QnAs](https://learning.teachme.codes/qnas/encapsulation_and_abstraction)|[Encapsulation and <br> Cheats](https://learning.teachme.codes/cheats/encapsulation_and_abstraction)|[Encapsulation and <br> Abstraction](https://learning.teachme.codes/python/encapsulation_and_abstraction)|
|[Magic Methods and <br> Operator Overloading](https://learning.teachme.codes/chapters/magic_methods_and_operator_overloading)|[Magic Methods and <br> Projects](https://learning.teachme.codes/projects/magic_methods_and_operator_overloading)|[Magic Methods and <br> QnAs](https://learning.teachme.codes/qnas/magic_methods_and_operator_overloading)|[Magic Methods and <br> Cheats](https://learning.teachme.codes/cheats/magic_methods_and_operator_overloading)|[Magic Methods and <br> Operator Overloading](https://learning.teachme.codes/python/magic_methods_and_operator_overloading)|
|[Composition and <br> Aggregation](https://learning.teachme.codes/chapters/composition_and_aggregation)|[Composition and <br> Projects](https://learning.teachme.codes/projects/composition_and_aggregation)|[Composition and <br> QnAs](https://learning.teachme.codes/qnas/composition_and_aggregation)|[Composition and <br> Cheats](https://learning.teachme.codes/cheats/composition_and_aggregation)|[Composition and <br> Aggregation](https://learning.teachme.codes/python/composition_and_aggregation)|



### [Introduction to Python](https://learning.teachme.codes/python/introduction_to_python): 

 Python is a high-level, interpreted programming language known for its simplicity and readability. It is widely used in web development, data analysis, artificial intelligence, and scientific computing.

### [Python Syntax and Semantics](https://learning.teachme.codes/python/python_syntax_and_semantics): 

 Python syntax refers to the rules that define the structure of the language, while semantics define the meaning of the language constructs. Understanding both is essential for writing correct and efficient code.

### [Variables and Data Types](https://learning.teachme.codes/python/variables_and_data_types): 

 Variables are used to store data in memory, while data types define the type of data that can be stored in a variable. Python supports various data types such as integers, floats, strings, lists, tuples, sets, and dictionaries.

### [Control Flow Statements](https://learning.teachme.codes/python/control_flow_statements): 

 Control flow statements allow you to control the execution of code based on conditions. 'if' and 'else' statements are used for conditional execution, while 'for' and 'while' loops are used for iteration.

### [Functions and Lambdas](https://learning.teachme.codes/python/functions_and_lambdas): 

 Functions are blocks of reusable code that perform a specific task. Lambdas are anonymous functions that can be defined in a single line. Both are essential for organizing and modularizing code.

### [Exception Handling](https://learning.teachme.codes/python/exception_handling): 

 Exception handling allows you to gracefully handle errors and exceptions that occur during program execution. It helps prevent crashes and provides a way to recover from unexpected situations.

### [File IO Operations](https://learning.teachme.codes/python/file_io_operations): 

 File IO operations allow you to read from and write to files on disk. Python provides built-in functions and methods for working with files, making it easy to manipulate file data.

### [List Comprehensions](https://learning.teachme.codes/python/list_comprehensions): 

 List comprehensions provide a concise way to create lists in Python. They allow you to generate lists using a single line of code, making code more readable and efficient.

### [Generators and Iterators](https://learning.teachme.codes/python/generators_and_iterators): 

 Generators and iterators are used to create iterable objects in Python. They allow you to iterate over sequences of data without loading the entire sequence into memory, making them memory-efficient.

### [Decorators in Python](https://learning.teachme.codes/python/decorators_in_python): 

 Decorators are a powerful feature in Python that allow you to modify or extend the behavior of functions or methods.

### [Context Managers](https://learning.teachme.codes/python/context_managers): 

 Context managers are used to manage resources in Python, such as files or database connections. They ensure that resources are properly cleaned up after use, even if an error occurs.

### [Modules and Packages](https://learning.teachme.codes/python/modules_and_packages): 

 Modules are files that contain Python code, while packages are directories that contain multiple modules. They help organize and reuse code, making it easier to manage large projects.

### [Virtual Environments](https://learning.teachme.codes/python/virtual_environments): 

 Virtual environments are isolated Python environments that allow you to install and manage dependencies for different projects. They help avoid conflicts between project dependencies and ensure reproducibility.

### [Python Standard Library](https://learning.teachme.codes/python/python_standard_library): 

 The Python Standard Library is a collection of modules and packages that provide a wide range of functionality, such as file I/O, networking, and data processing. It is included with Python and does not require additional installation.

### [Regular Expressions](https://learning.teachme.codes/python/regular_expressions): 

 Regular expressions are used to search and manipulate text patterns in Python. They provide a powerful and flexible way to match and extract data from strings.

### [Using map_filter_reduce](https://learning.teachme.codes/python/using_map_filter_reduce): 

 The map(), filter(), and reduce() functions are built-in functions in Python that allow you to apply a function to each element of an iterable, filter elements based on a condition, and reduce a sequence of elements to a single value, respectively.

### [String Manipulation Functions](https://learning.teachme.codes/python/string_manipulation_functions): 

 String manipulation functions in Python allow you to manipulate and format strings, such as concatenating, splitting, and replacing substrings. They are essential for working with text data.

### [Numeric and Math Functions](https://learning.teachme.codes/python/numeric_and_math_functions): 

 Numeric and math functions in Python provide a wide range of mathematical operations, such as arithmetic, trigonometric, and statistical functions. They are essential for scientific computing and data analysis.

### [Data Structure Functions](https://learning.teachme.codes/python/data_structure_functions): 

 Data structure functions in Python provide methods to manipulate lists, tuples, sets, and dictionaries. They allow you to add, remove, and modify elements in data structures efficiently.

### [Date and Time Functions](https://learning.teachme.codes/python/date_and_time_functions): 

 Date and time functions in Python provide methods to work with dates, times, and time zones. They allow you to parse, format, and manipulate date and time values.

### [Input and Output Functions](https://learning.teachme.codes/python/input_and_output_functions): 

 Input and output functions in Python allow you to interact with the user through the console, read input from files, and write output to files. They are essential for building interactive applications.

### [Built-in Sorting and Searching](https://learning.teachme.codes/python/built_in_sorting_and_searching): 

 Python provides built-in functions and methods for sorting and searching elements in lists, tuples, sets, and dictionaries. They allow you to efficiently organize and search data.

### [Type Conversion Functions](https://learning.teachme.codes/python/type_conversion_functions): 

 Type conversion functions in Python allow you to convert data between different data types, such as integers, floats, strings, and lists. They are essential for data processing and manipulation.

### [Object-Oriented Functions](https://learning.teachme.codes/python/object_oriented_functions): 

 Object-oriented programming is a programming paradigm that uses objects and classes to model real-world entities. Python supports object-oriented programming, making it easy to create and work with objects.

### [Classes and Objects](https://learning.teachme.codes/python/classes_and_objects): 

 Classes are blueprints for creating objects, while objects are instances of classes. They allow you to model real-world entities and define their behavior and attributes.

### [Inheritance and Polymorphism](https://learning.teachme.codes/python/inheritance_and_polymorphism): 

 Inheritance allows you to create new classes based on existing classes, while polymorphism allows objects of different classes to be treated as objects of a common superclass. They help promote code reuse and flexibility.

### [Encapsulation and Abstraction](https://learning.teachme.codes/python/encapsulation_and_abstraction): 

 Encapsulation is the process of hiding the internal implementation details of a class, while abstraction is the process of hiding unnecessary details and exposing only the essential features. They help improve code maintainability and readability.

### [Magic Methods and Operator Overloading](https://learning.teachme.codes/python/magic_methods_and_operator_overloading): 

 Magic methods are special methods in Python that allow you to define custom behavior for built-in operations, such as addition, subtraction, and comparison. They provide a way to customize the behavior of objects.

### [Composition and Aggregation](https://learning.teachme.codes/python/composition_and_aggregation): 

 Composition is a design pattern in which a class contains objects of other classes, while aggregation is a design pattern in which a class has a reference to another class. They help promote code reuse and modularity.

### [Class and Static Methods](https://learning.teachme.codes/python/class_and_static_methods): 

 Class and static methods are methods that belong to a class rather than an instance of a class. They allow you to define behavior that is shared across all instances of a class or does not depend on instance state.

### [Properties and Descriptors](https://learning.teachme.codes/python/properties_and_descriptors): 

 Properties and descriptors are used to define custom behavior for accessing and setting attributes of a class. They allow you to enforce constraints and validation rules on attribute values.

### [Abstract Base Classes](https://learning.teachme.codes/python/abstract_base_classes): 

 Abstract base classes are classes that define a set of methods that must be implemented by subclasses. They provide a way to define interfaces and enforce method implementations in derived classes.

### [Metaclasses in Python](https://learning.teachme.codes/python/metaclasses_in_python): 

 Metaclasses are classes that define the behavior of classes. They allow you to customize class creation and modify class attributes and methods. Metaclasses are a powerful feature in Python for advanced use cases.

### [Unit Testing in Python](https://learning.teachme.codes/python/unit_testing_in_python): 

 Unit testing is a software testing technique in which individual units or components of a software application are tested in isolation. Python provides built-in libraries and frameworks for writing and running unit tests.

### [Debugging Techniques](https://learning.teachme.codes/python/debugging_techniques): 

 Debugging is the process of identifying and fixing errors in a program. Python provides built-in tools and techniques for debugging, such as print statements, logging, and debugging tools.

### [Profiling and Optimization](https://learning.teachme.codes/python/profiling_and_optimization): 

 Profiling is the process of measuring the performance of a program to identify bottlenecks and optimize code. Python provides built-in tools and libraries for profiling and optimizing code.

### [Concurrency and Parallelism](https://learning.teachme.codes/python/concurrency_and_parallelism): 

 Concurrency is the ability of a program to execute multiple tasks simultaneously, while parallelism is the ability of a program to execute multiple tasks in parallel. Python provides built-in libraries and frameworks for writing concurrent and parallel code.

### [Asynchronous Programming](https://learning.teachme.codes/python/asynchronous_programming): 

 Asynchronous programming is a programming paradigm that allows tasks to run concurrently without blocking the main program. Python provides built-in libraries and frameworks for writing asynchronous code.





# Object-Oriented Functions

## Introduction to Object-Oriented Programming

| Title                                      | Concept                                                | Description                                                                 |
|--------------------------------------------|--------------------------------------------------------|-----------------------------------------------------------------------------|
| Definition of Object-Oriented Programming  | OOP is a paradigm that uses objects and classes.       | Models entities using objects, promoting code reusability and structure.  |
| Key Concepts of OOP                        | Classes, Objects, Encapsulation, Inheritance, Polymorphism. | Fundamental principles of OOP for structuring and organizing code.         |
| Advantages of OOP in Python                | Reusability, Modularity, Flexibility, Maintainability. | Enhances code structure, promotes efficiency, and simplifies maintenance. |

## Classes and Objects

### Defining Classes in Python

| Title                       | Concept                                            | Code                                                                     |
|-----------------------------|----------------------------------------------------|--------------------------------------------------------------------------|
| Syntax for Class Definition | Use the `class` keyword to define a class.        | <pre lang="python">class ClassName:<br>    # Class attributes and methods</pre> |
| Attributes and Methods      | Variables and functions within a class.           | <pre lang="python">class Dog:<br>    def __init__(self, name, age):<br>        self.name = name<br>        self.age = age</pre> |

### Creating Objects

| Title                       | Concept                                            | Code                                                                     |
|-----------------------------|----------------------------------------------------|--------------------------------------------------------------------------|
| Instantiating Objects       | Creating instances of a class.                    | <pre lang="python">dog1 = Dog("Buddy", 3)</pre>                           |
| Object Initialization       | Setting initial values for object attributes.     | <pre lang="python">class Car:<br>    def __init__(self, color):<br>        self.color = color</pre> |

### Class Constructors and Destructors

| Title                       | Concept                                            | Code                                                                     |
|-----------------------------|----------------------------------------------------|--------------------------------------------------------------------------|
| `__init__()` Method         | Constructor method for object initialization.     | <pre lang="python">def __init__(self, param1, param2):<br>    self.param1 = param1<br>    self.param2 = param2</pre> |
| `__del__()` Method          | Destructor method for object cleanup.             | <pre lang="python">def __del__(self):<br>    print("Object destroyed")</pre> |

## Inheritance and Polymorphism

### Understanding Inheritance

| Title                       | Concept                                            | Code                                                                     |
|-----------------------------|----------------------------------------------------|--------------------------------------------------------------------------|
| Base Class and Derived Class | Establishing relationships between classes.      | <pre lang="python">class ParentClass:<br>    # Base class definition<br>class ChildClass(ParentClass):<br>    # Derived class from ParentClass</pre> |
| Types of Inheritance         | Single, Multiple, Multilevel, Hierarchical.       |                                                                           |

### Implementing Inheritance in Python

| Title                       | Concept                                            | Code                                                                     |
|-----------------------------|----------------------------------------------------|--------------------------------------------------------------------------|
| Syntax for Inheritance       | Extending base classes to create subclasses.      | <pre lang="python">class BaseClass:<br>    pass<br>class SubClass(BaseClass):<br>    pass</pre> |
| Method Overriding            | Customizing behaviors of inherited methods.       | <pre lang="python">class Base:<br>    def show(self):<br>        print("Base class method")<br>class Sub(Base):<br>    def show(self):<br>        print("Sub class method")</pre> |

### Polymorphism in Python

| Title                       | Concept                                            | Code                                                                     |
|-----------------------------|----------------------------------------------------|--------------------------------------------------------------------------|
| Polymorphic Functions        | Treating objects of different classes as same type. | <pre lang="python">def sound(animal):<br>    animal.make_sound()</pre>     |
| Operator Overloading         | Redefining operators for custom object behavior. |                                                                           |

## Encapsulation and Abstraction

### Encapsulation in OOP

| Title                       | Concept                                            | Code                                                                     |
|-----------------------------|----------------------------------------------------|--------------------------------------------------------------------------|
| Definition of Encapsulation  | Restricting access to class members.              |                                                                           |
| Access Modifiers in Python   | Controlling visibility of class attributes.       | <pre lang="python">class MyClass:<br>    def __init__(self):<br>        self.__private_var = 10<br>        self._protected_var = 20</pre> |

### Abstraction Concepts

| Title                       | Concept                                            | Code                                                                     |
|-----------------------------|----------------------------------------------------|--------------------------------------------------------------------------|
| Abstract Classes            | Classes that cannot be instantiated directly.    | <pre lang="python">from abc import ABC, abstractmethod<br>class AbstractClass(ABC):<br>    @abstractmethod<br>    def abstract_method(self):<br>        pass</pre> |

## Instance and Class Variables

### Instance Variables

| Title                       | Concept                                            | Code                                                                      |
|-----------------------------|----------------------------------------------------|---------------------------------------------------------------------------|
| Definition and Scope        | Unique to each object instance.                   | <pre lang="python">self.attribute = value</pre>                           |
| Accessing Instance Data     | Retrieving values specific to an object.          | <pre lang="python">print(object.attribute)</pre>                           |

### Class Variables

| Title                       | Concept                                            | Code                                                                      |
|-----------------------------|----------------------------------------------------|---------------------------------------------------------------------------|
| Shared Class Variables      | Attributes shared among all instances of a class. | <pre lang="python">class MyClass:<br>    class_variable = value</pre>     |
| Modifying Class Variables   | Updating shared values across all objects.        | <pre lang="python">MyClass.class_variable = new_value</pre>                |

By mastering these concepts and techniques, you can effectively utilize object-oriented functions in Python to create scalable, efficient, and maintainable code structures.
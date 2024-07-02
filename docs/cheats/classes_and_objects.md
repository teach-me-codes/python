# Classes and Objects: Introduction to Classes and Objects

## Understanding Classes

| Title                       | Concept                                                            | Description                                    |
|-----------------------------|--------------------------------------------------------------------|------------------------------------------------|
| Definition of Classes       | Classes are blueprints for creating objects in Python.            | Define attributes and methods common to all instances of the class. |
| Purpose of Classes          | Encapsulation, Inheritance, Polymorphism.                         | Encapsulate data and behavior, promote code reuse, allow flexible method implementations. |
| Difference Between Class and Object | Class is a template; object is an instance of the class. | Classes define attributes and methods; objects have specific attribute values. |

## Basics of Object-Oriented Programming

| Title                       | Concept                                                            | Description                                    |
|-----------------------------|--------------------------------------------------------------------|------------------------------------------------|
| Encapsulation               | Bundling data and methods within a class to restrict direct access. | Enhances data protection and code modularity. |
| Inheritance                 | Creating new classes based on existing ones.                      | Promotes code reuse and establishes class hierarchies. |
| Polymorphism                | Treating objects of different classes as objects of a common superclass. | Allows for flexible and reusable code. |
| Advantages of OOP in Python | Code Reusability, Modularity, Flexibility, Maintainability. | Enhances code structure and efficiency. |
  
# Classes and Objects: Creating Classes in Python

## 1. Class Declaration

| Title                       | Concept                                                            | Code                                           |
|-----------------------------|--------------------------------------------------------------------|------------------------------------------------|
| Syntax for Declaring Classes | Define a class using the `class` keyword.                         |<pre lang="python">class ClassName:<br>    # Class attributes and methods go here</pre>|
| Naming Conventions          | Use CamelCase for class names.                                     | For example, `class Car:` |

## 2. Attributes and Methods

| Title                       | Concept                                                            | Code                                           |
|-----------------------------|--------------------------------------------------------------------|------------------------------------------------|
| Defining Attributes         | Variables holding data associated with objects.                   |<pre lang="python">class Dog:<br>    def __init__(self, name, age):<br>        self.name = name<br>        self.age = age</pre>|
| Creating Methods            | Functions within a class for operations on attributes.            |<pre lang="python">class Circle:<br>    def __init__(self, radius):<br>        self.radius = radius<br>    def calculate_area(self):<br>        return 3.14 * self.radius ** 2</pre>|

## 3. Constructor Method

| Title                       | Concept                                                            | Code                                           |
|-----------------------------|--------------------------------------------------------------------|------------------------------------------------|
| Definition and Usage of Constructors | Special method initializing new objects.                        |<pre lang="python">class Person:<br>    def __init__(self, name, age):<br>        self.name = name<br>        self.age = age</pre>|
| Role of Special Method `__init__` | Sets the initial state of objects.                               |<pre lang="python">person1 = Person("Alice", 30)<br># person1.name will be "Alice" and person1.age will be 30</pre>|

## Instance and Class Variables

### 1. Instance Variables

| Title                       | Concept                                                            | Code                                           |
|-----------------------------|--------------------------------------------------------------------|------------------------------------------------|
| Definition and Scope of Instance Variables | Unique to each object of a class.                             |<pre lang="python">class Car:<br>    def __init__(self, brand, model):<br>        self.brand = brand<br>        self.model = model<br>my_car = Car("Toyota", "Camry")<br>print(my_car.brand)  # Output: Toyota</pre>|
| Setting and Accessing Instance-Specific Data | Use `self` keyword within class methods.                       |<pre lang="python">class Student:<br>    def __init__(self, name, age):<br>        self.name = name<br>        self.age = age<br>    def display_info(self):<br>        print(f"Name: {self.name}, Age: {self.age}")<br>student = Student("Alice", 20)<br>student.display_info()</pre>|

### 2. Class Variables

| Title                       | Concept                                                            | Code                                           |
|-----------------------------|--------------------------------------------------------------------|------------------------------------------------|
| Understanding Class-Level Variables | Shared among all instances of a class.                         |<pre lang="python">class Circle:<br>    pi = 3.14<br>    def __init__(self, radius):<br>        self.radius = radius<br>    def calculate_area(self):<br>        return Circle.pi * self.radius ** 2<br>circle = Circle(5)<br>print(circle.calculate_area())  # Output: 78.5</pre>|
| Accessing and Modifying Class Variables | Use the class name to access or modify them.                    |<pre lang="python">class BankAccount:<br>    interest_rate = 0.05<br>account = BankAccount()<br>print(account.interest_rate)  # Output: 0.05<br>BankAccount.interest_rate = 0.06<br>print(account.interest_rate)  # Output: 0.06</pre>|

# Classes and Objects: Inheritance in Python

## Inheritance in Python

| Title                       | Concept                                                            | Description                                    |
|-----------------------------|--------------------------------------------------------------------|------------------------------------------------|
| Definition and Purpose of Inheritance | Derive new classes from existing ones.                        | Promotes code reuse and extends base class functionality. |
| Types of Inheritance        | Single, Multiple, Multilevel, Hierarchical.                     | Inherit attributes and methods in various ways. |

## Syntax for Inheriting Classes

| Title                       | Concept                                                            | Code                                           |
|-----------------------------|--------------------------------------------------------------------|------------------------------------------------|
| Extending Base Classes      | Specify the base class for inheritance.                          |<pre lang="python">class BaseClass:<br>    def show(self):<br>        print("Base Class method")<br>class SubClass(BaseClass):<br>    def show(self):<br>        print("SubClass method")<br># Creating objects and calling methods<br>base_obj = BaseClass()<br>sub_obj = SubClass()<br>base_obj.show()  # Output: Base Class method<br>sub_obj.show()   # Output: SubClass method</pre>|
| Overriding Methods in Subclasses | Define a method with the same name in the subclass.               | Customize behavior specific to the subclass. |

## `super()` Method

| Title                       | Concept                                                            | Code                                           |
|-----------------------------|--------------------------------------------------------------------|------------------------------------------------|
| Utilization of `super()` for Method Resolution | Invoke methods from the base class.                              |<pre lang="python">class BaseClass:<br>    def show(self):<br>        print("Base Class method")<br>class SubClass(BaseClass):<br>    def show(self):<br>        super().show()<br>        print("SubClass method")<br>sub_obj = SubClass()<br>sub_obj.show()<br># Output:<br># Base Class method<br># SubClass method</pre>|
| Benefits of `super()` in Resolving Inheritance Conflicts | Ensures proper method resolution and simplifies structure.   | Useful in multiple inheritance scenarios. |

# Classes and Objects: Polymorphism and Method Overriding

## Polymorphism and Method Overriding

### Polymorphism

| Title                       | Concept                                                            | Description                                    |
|-----------------------------|--------------------------------------------------------------------|------------------------------------------------|
| Understanding Polymorphism  | Treat objects of different classes as a common superclass.       | Enhances code structure and flexibility. |
| Advantages of Polymorphism  | Code Reusability and Enhanced Flexibility.                       | Use shared method names with distinct implementations. |

### Method Overriding

| Title                       | Concept                                                            | Code                                           |
|-----------------------------|--------------------------------------------------------------------|------------------------------------------------|
| Definition of Method Overriding | Subclass provides specific method implementation.               | Customize inherited methods for subclass needs. |
| Implementing Method Overriding | Define a method with the same name in the subclass.               |<pre lang="python">class Animal:<br>    def sound(self):<br>        print("Animal makes a sound")<br>class Dog(Animal):<br>    def sound(self):<br>        print("Dog barks")<br>class Cat(Animal):<br>    def sound(self):<br>        print("Cat meows")<br>dog = Dog()<br>dog.sound()  # Output: Dog barks<br>cat = Cat()<br>cat.sound()  # Output: Cat meows</pre>|

# Classes and Objects: Encapsulation and Data Hiding

## Encapsulation

| Title                       | Concept                                                            | Description                                    |
|-----------------------------|--------------------------------------------------------------------|------------------------------------------------|
| Encapsulation Concept       | Bundle data and methods in a class to control access.             | Enhances organization and safeguards object integrity. |
| Purpose and Benefits of Encapsulation | Data Protection, Modularity, Flexibility.                      | Control data access, improve organization, enhance maintainability. |
| Implementing Encapsulation in Python Classes | Use private attributes and public methods. |<pre lang="python">class BankAccount:<br>    def __init__(self, initial_balance):<br>        self.__balance = initial_balance<br
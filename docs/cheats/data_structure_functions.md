# Data Structure Functions in Python

## Introduction to Data Structure Functions

### Overview of Data Structures
| Title                           | Concept                                                            | Description                                    |
|-----------------------------|--------------------------------------------------------------------|------------------------------------------------|
| Explanation of Data Structures   | Data structures organize and store data efficiently in memory.    | Arrays, lists, stacks, queues, and maps are examples of data structures. |
| Importance in Programming       | Facilitate data organization, manipulation, and retrieval.         | Data structures optimize algorithms and enhance program efficiency. |

### Understanding Functions in Python
| Title                           | Concept                                                            | Description                                    |
|-----------------------------|--------------------------------------------------------------------|------------------------------------------------|
| Definition of Functions         | Functions are blocks of reusable code to perform specific tasks.   | Functions help in structuring code and promoting reusability. |
| Role of Functions in Data Structure Manipulation | Functions manipulate data structures effectively.                 | Functions provide methods for adding, removing, and modifying elements in data structures. |

# Lists Functions

## Creating and Accessing Lists

| Title                           | Concept                                                            | Code                                           |
|-----------------------------|--------------------------------------------------------------------|------------------------------------------------|
| Syntax for List Creation         | Creating lists using square brackets in Python.                    |<pre lang="python">my_list = [1, 2, 3, 4, 5]</pre>|
| Indexing and Slicing Lists       | Accessing specific elements and sublists in a list.                |<pre lang="python">print(my_list[0])  # Output: 1<br>print(my_list[1:3])  # Output: [2, 3]</pre>|

## Modifying Lists

| Title                           | Concept                                                            | Code                                           |
|-----------------------------|--------------------------------------------------------------------|------------------------------------------------|
| Adding Elements to Lists         | Appending, inserting, or extending elements in a list.             |<pre lang="python">my_list.append(6)<br>my_list.insert(2, 10)<br>my_list.extend([7, 8])</pre>|
| Removing Elements from Lists     | Removing elements based on index or value from a list.             |<pre lang="python">my_list.remove(3)<br>my_list.pop(0)</pre>|

## List Operations

| Title                           | Concept                                                            | Code                                           |
|-----------------------------|--------------------------------------------------------------------|------------------------------------------------|
| Common Operations on Lists       | Operations like sorting, reversing, and counting in lists.         |<pre lang="python">my_list.sort()<br>my_list.reverse()<br>count = my_list.count(2)</pre>|
| Iterating Over Lists             | Using loops or list comprehensions to iterate through lists.       |<pre lang="python">for item in my_list:<br>    print(item)</pre>|

## List Comprehensions

| Title                           | Concept                                                            | Code                                           |
|-----------------------------|--------------------------------------------------------------------|------------------------------------------------|
| Definition and Syntax            | Concise way to create lists based on existing lists.               |<pre lang="python">new_list = [x**2 for x in range(10) if x % 2 == 0]</pre>|
| Advantages of List Comprehensions | Simplify and condense code for list creation.                    | Compact and readable syntax for list operations. |

# Tuple Functions

## Creating and Accessing Tuples

| Title                           | Concept                                                            | Code                                           |
|-----------------------------|--------------------------------------------------------------------|------------------------------------------------|
| Tuple Initialization             | Defining tuples with parentheses in Python.                        |<pre lang="python">my_tuple = (1, 2, 3)</pre>|
| Accessing Tuple Elements         | Retrieving elements from tuples using indexing.                    |<pre lang="python">print(my_tuple[0])  # Output: 1</pre>|

## Modifying Tuples

| Title                           | Concept                                                            | Code                                           |
|-----------------------------|--------------------------------------------------------------------|------------------------------------------------|
| Immutability of Tuples           | Tuples are immutable, meaning their elements cannot be changed.    |<pre lang="python">my_tuple[0] = 5  # This will raise an error</pre>|
| Workarounds for Modifying Tuples | Reassigning a new tuple to work with the desired changes.          |<pre lang="python">my_tuple = (4, 2, 3)</pre>|

## Tuple Operations

| Title                           | Concept                                                            | Code                                           |
|-----------------------------|--------------------------------------------------------------------|------------------------------------------------|
| Tuple Concatenation              | Combining tuples to create a new tuple.                            |<pre lang="python">new_tuple = my_tuple + (4, 5)</pre>|
| Tuple Packing and Unpacking      | Assigning multiple values to a single tuple or vice versa.         |<pre lang="python">a, b, c = my_tuple  # Unpacking<br>my_new_tuple = (1, 2, 3)  # Packing</pre>|

## Tuple Methods

| Title                           | Concept                                                            | Code                                           |
|-----------------------------|--------------------------------------------------------------------|------------------------------------------------|
| Methods Available for Tuples     | `count()` and `index()` methods for tuple manipulation.            |<pre lang="python">count = my_tuple.count(2)<br>index = my_tuple.index(3)</pre>|

# Dictionary Functions

## Creating and Accessing Dictionaries

| Title                           | Concept                                                            | Code                                           |
|-----------------------------|--------------------------------------------------------------------|------------------------------------------------|
| Dictionary Initialization        | Defining dictionaries using curly braces in Python.                |<pre lang="python">my_dict = {'one': 1, 'two': 2}</pre>|
| Accessing Dictionary Items       | Retrieving values based on keys from dictionaries.                 |<pre lang="python">print(my_dict['one'])  # Output: 1</pre>|

## Modifying Dictionaries

| Title                           | Concept                                                            | Code                                           |
|-----------------------------|--------------------------------------------------------------------|------------------------------------------------|
| Adding and Updating Dictionary Items | Inserting new key-value pairs or updating existing ones.         |<pre lang="python">my_dict['three'] = 3<br>my_dict['one'] = 10</pre>|
| Removing Dictionary Items        | Deleting items from dictionaries based on keys.                   |<pre lang="python">del my_dict['two']<br>my_dict.pop('three')</pre>|

## Dictionary Operations

| Title                           | Concept                                                            | Code                                           |
|-----------------------------|--------------------------------------------------------------------|------------------------------------------------|
| Common Operations on Dictionaries | Performing actions like iterating, sorting, and copying.         |<pre lang="python">for key, value in my_dict.items():<br>    print(key, value)</pre>|
| Iterating Over Dictionary Items   | Accessing keys, values, or items in dictionaries efficiently.     |<pre lang="python">keys = my_dict.keys()<br>values = my_dict.values()</pre>|

## Dictionary Comprehensions

| Title                           | Concept                                                            | Code                                           |
|-----------------------------|--------------------------------------------------------------------|------------------------------------------------|
| Syntax for Dictionary Comprehensions | Creating dictionaries in a concise manner.                        |<pre lang="python">{key: value for key, value in zip(keys, values)}</pre>|
| Use Cases for Dictionary Comprehensions | Applications in data transformation and filtering.               | Efficient way to generate dictionaries from existing data. |

# Set Functions

## Creating and Accessing Sets

| Title                           | Concept                                                            | Code                                           |
|-----------------------------|--------------------------------------------------------------------|------------------------------------------------|
| Set Initialization               | Defining sets using curly braces or the set() function.            |<pre lang="python">my_set = {1, 2, 3}</pre>|
| Accessing Set Elements          | Performing checks or operations on set elements.                  |<pre lang="python">if 1 in my_set:<br>    print("1 is in the set")</pre>|

## Modifying Sets

| Title                           | Concept                                                            | Code                                           |
|-----------------------------|--------------------------------------------------------------------|------------------------------------------------|
| Adding Elements to Sets         | Inserting new elements into sets using add() or update().         |<pre lang="python">my_set.add(4)<br>my_set.update({5, 6})</pre>|
| Removing Elements from Sets     | Deleting elements from sets through discard() or remove().        |<pre lang="python">my_set.remove(3)<br>my_set.discard(2)</pre>|

## Set Operations

| Title                           | Concept                                                            | Code                                           |
|-----------------------------|--------------------------------------------------------------------|------------------------------------------------|
| Operations like Union, Intersection, and Difference | Set theory operations to combine or compare sets.              |<pre lang="python">union_set = set1 | set2<br>intersection_set = set1 & set2<br>difference_set = set1 - set2</pre>|
| Subset and Superset Operations   | Checking relationships between sets like subset and superset.    |<pre lang="python">is_subset = set1.issubset(set2)<br>is_superset = set1.issuperset(set2)</pre>|

## Set Comprehensions

| Title                           | Concept                                                            | Code                                           |
|-----------------------------|--------------------------------------------------------------------|------------------------------------------------|
| Syntax for Set Comprehensions   | Constructing sets based on existing sets or iterables.            |<pre lang="python">{x for x in my_list if x % 2 == 0}</pre>|
| Benefits of Set Comprehensions   | Streamlined generation of sets with specific conditions.          | Concise and expressive syntax for set creation. |

# Stack Functions
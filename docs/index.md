
# Welcome to Python Learning Portal

<style>
.circular-nav {
    position: relative;
    width: 600px; /* Increase width to accommodate the fourth button */
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
    <button class="nav-button" id="book"><i class="fas fa-book"></i> Book </button>
    <button class="nav-button" id="questions"><i class="fas fa-lightbulb"></i> Q&A</button>
    <button class="nav-button" id="cheatsheets"><i class="fas fa-text"></i> Cheat Sheets</button>
    <button class="nav-button" id="projects"><i class="fas fa-laptop"></i> Projects</button>
    <button class="nav-button" id="references"><i class="fas fa-text"></i> References </button>
</div>

<script>
document.getElementById('book').onclick = function() {
    window.location.href = 'https://learning.teachme.codes/python/chapters/chapters';
};
document.getElementById('projects').onclick = function() {
    window.location.href = 'https://learning.teachme.codes/python/projects/projects';
};
document.getElementById('questions').onclick = function() {
    window.location.href = 'https://learning.teachme.codes/python/qnas/qnas';
};
document.getElementById('cheatsheets').onclick = function() {
    window.location.href = 'https://learning.teachme.codes/python/cheats/cheats';
};
document.getElementById('references').onclick = function() {
    window.location.href = 'https://learning.teachme.codes/python/references/references';
};
</script>



| Book Chapters | Questions & Answers | Cheat Sheets | Projects | References |
|--------|----------|-----|--------------|------------|
|[Introduction to Python](https://learning.teachme.codes/python/chapters/introduction_to_python)|[Introduction to QnAs](https://learning.teachme.codes/python/qnas/introduction_to_python)|[Introduction to Cheats](https://learning.teachme.codes/python/cheats/introduction_to_python)|[Introduction to Projects](https://learning.teachme.codes/python/projects/introduction_to_projects)|[Python Official Documentation](https://docs.python.org/3/tutorial/index.html)|
|[Python Syntax and Semantics](https://learning.teachme.codes/python/chapters/python_syntax_and_semantics)|[Python Syntax and QnAs](https://learning.teachme.codes/python/qnas/python_syntax_and_semantics)|[Python Syntax and Cheats](https://learning.teachme.codes/python/cheats/python_syntax_and_semantics)|[Python Syntax and Projects](https://learning.teachme.codes/python/projects/python_syntax_and_semantics)|[Python Syntax](https://docs.python.org/3/reference/lexical_analysis.html)|
|[Variables and Data Types](https://learning.teachme.codes/python/chapters/variables_and_data_types)|[Variables and QnAs](https://learning.teachme.codes/python/qnas/variables_and_data_types)|[Variables and Cheats](https://learning.teachme.codes/python/cheats/variables_and_data_types)|[Variables and Projects](https://learning.teachme.codes/python/projects/variables_and_data_types)|[Python Data Types](https://docs.python.org/3/library/stdtypes.html)|
|[Control Flow Statements](https://learning.teachme.codes/python/chapters/control_flow_statements)|[Control Flow QnAs](https://learning.teachme.codes/python/qnas/control_flow_statements)|[Control Flow Cheats](https://learning.teachme.codes/python/cheats/control_flow_statements)|[Control Flow Projects](https://learning.teachme.codes/python/projects/control_flow_statements)|[Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html)|
|[Functions and Lambdas](https://learning.teachme.codes/python/chapters/functions_and_lambdas)|[Functions and QnAs](https://learning.teachme.codes/python/qnas/functions_and_lambdas)|[Functions and Cheats](https://learning.teachme.codes/python/cheats/functions_and_lambdas)|[Functions and Projects](https://learning.teachme.codes/python/projects/functions_and_lambdas)|[Python Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)|
|[Exception Handling](https://learning.teachme.codes/python/chapters/exception_handling)|[Exception QnAs](https://learning.teachme.codes/python/qnas/exception_handling)|[Exception Cheats](https://learning.teachme.codes/python/cheats/exception_handling)|[Exception Projects](https://learning.teachme.codes/python/projects/exception_handling)|[Python Exceptions](https://docs.python.org/3/tutorial/errors.html)|
|[File IO Operations](https://learning.teachme.codes/python/chapters/file_io_operations)|[File IO QnAs](https://learning.teachme.codes/python/qnas/file_io_operations)|[File IO Cheats](https://learning.teachme.codes/python/cheats/file_io_operations)|[File IO Projects](https://learning.teachme.codes/python/projects/file_io_operations)|[File IO](https://docs.python.org/3/tutorial/inputoutput.html)|
|[List Comprehensions](https://learning.teachme.codes/python/chapters/list_comprehensions)|[List QnAs](https://learning.teachme.codes/python/qnas/list_comprehensions)|[List Cheats](https://learning.teachme.codes/python/cheats/list_comprehensions)|[List Projects](https://learning.teachme.codes/python/projects/list_comprehensions)|[List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)|
|[Generators and Iterators](https://learning.teachme.codes/python/chapters/generators_and_iterators)|[Generators and QnAs](https://learning.teachme.codes/python/qnas/generators_and_iterators)|[Generators and Cheats](https://learning.teachme.codes/python/cheats/generators_and_iterators)|[Generators and Projects](https://learning.teachme.codes/python/projects/generators_and_iterators)|[Generators](https://docs.python.org/3/tutorial/classes.html#generators)|
|[Decorators in Python](https://learning.teachme.codes/python/chapters/decorators_in_python)|[Decorators in QnAs](https://learning.teachme.codes/python/qnas/decorators_in_python)|[Decorators in Cheats](https://learning.teachme.codes/python/cheats/decorators_in_python)|[Decorators in Projects](https://learning.teachme.codes/python/projects/decorators_in_python)|[Decorators](https://docs.python.org/3/glossary.html#term-decorator)|
|[Context Managers](https://learning.teachme.codes/python/chapters/context_managers)|[Context QnAs](https://learning.teachme.codes/python/qnas/context_managers)|[Context Cheats](https://learning.teachme.codes/python/cheats/context_managers)|[Context Projects](https://learning.teachme.codes/python/projects/context_managers)|[Context Managers](https://docs.python.org/3/reference/datamodel.html#context-managers)|
|[Modules and Packages](https://learning.teachme.codes/python/chapters/modules_and_packages)|[Modules and QnAs](https://learning.teachme.codes/python/qnas/modules_and_packages)|[Modules and Cheats](https://learning.teachme.codes/python/cheats/modules_and_packages)|[Modules and Projects](https://learning.teachme.codes/python/projects/modules_and_packages)|[Modules](https://docs.python.org/3/tutorial/modules.html)|
|[Virtual Environments](https://learning.teachme.codes/python/chapters/virtual_environments)|[Virtual QnAs](https://learning.teachme.codes/python/qnas/virtual_environments)|[Virtual Cheats](https://learning.teachme.codes/python/cheats/virtual_environments)|[Virtual Projects](https://learning.teachme.codes/python/projects/virtual_environments)|[Virtual Environments](https://docs.python.org/3/library/venv.html)|
|[Python Standard Library](https://learning.teachme.codes/python/chapters/python_standard_library)|[Python Standard QnAs](https://learning.teachme.codes/python/qnas/python_standard_library)|[Python Standard Cheats](https://learning.teachme.codes/python/cheats/python_standard_library)|[Python Standard Projects](https://learning.teachme.codes/python/projects/python_standard_library)|[Standard Library](https://docs.python.org/3/library/index.html)|
|[Regular Expressions](https://learning.teachme.codes/python/chapters/regular_expressions)|[Regular QnAs](https://learning.teachme.codes/python/qnas/regular_expressions)|[Regular Cheats](https://learning.teachme.codes/python/cheats/regular_expressions)|[Regular Projects](https://learning.teachme.codes/python/projects/regular_expressions)|[Regular Expressions](https://docs.python.org/3/library/re.html)|
|[Using map_filter_reduce](https://learning.teachme.codes/python/chapters/using_map_filter_reduce)|[Using QnAs](https://learning.teachme.codes/python/qnas/using_map_filter_reduce)|[Using Cheats](https://learning.teachme.codes/python/cheats/using_map_filter_reduce)|[Using Projects](https://learning.teachme.codes/python/projects/using_map_filter_reduce)|[Functional Programming](https://docs.python.org/3/howto/functional.html)|
|[String Manipulation Functions](https://learning.teachme.codes/python/chapters/string_manipulation_functions)|[String Manipulation QnAs](https://learning.teachme.codes/python/qnas/string_manipulation_functions)|[String Manipulation Cheats](https://learning.teachme.codes/python/cheats/string_manipulation_functions)|[String Manipulation Projects](https://learning.teachme.codes/python/projects/string_manipulation_functions)|[String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)|
|[Numeric and Math Functions](https://learning.teachme.codes/python/chapters/numeric_and_math_functions)|[Numeric and Math QnAs](https://learning.teachme.codes/python/qnas/numeric_and_math_functions)|[Numeric and Math Cheats](https://learning.teachme.codes/python/cheats/numeric_and_math_functions)|[Numeric and Math Projects](https://learning.teachme.codes/python/projects/numeric_and_math_functions)|[Math Module](https://docs.python.org/3/library/math.html)|
|[Data Structure Functions](https://learning.teachme.codes/python/chapters/data_structure_functions)|[Data Structure QnAs](https://learning.teachme.codes/python/qnas/data_structure_functions)|[Data Structure Cheats](https://learning.teachme.codes/python/cheats/data_structure_functions)|[Data Structure Projects](https://learning.teachme.codes/python/projects/data_structure_functions)|[Data Structures](https://docs.python.org/3/tutorial/datastructures.html)|
|[Date and Time Functions](https://learning.teachme.codes/python/chapters/date_and_time_functions)|[Date and Time QnAs](https://learning.teachme.codes/python/qnas/date_and_time_functions)|[Date and Time Cheats](https://learning.teachme.codes/python/cheats/date_and_time_functions)|[Date and Time Projects](https://learning.teachme.codes/python/projects/date_and_time_functions)|[Datetime Module](https://docs.python.org/3/library/datetime.html)|
|[Input and Output Functions](https://learning.teachme.codes/python/chapters/input_and_output_functions)|[Input and Output QnAs](https://learning.teachme.codes/python/qnas/input_and_output_functions)|[Input and Output Cheats](https://learning.teachme.codes/python/cheats/input_and_output_functions)|[Input and Output Projects](https://learning.teachme.codes/python/projects/input_and_output_functions)|[Input and Output](https://docs.python.org/3/tutorial/inputoutput.html)|
|[Built-in Sorting and Searching](https://learning.teachme.codes/python/chapters/built_in_sorting_and_searching)|[Built-in Sorting and QnAs](https://learning.teachme.codes/python/qnas/built_in_sorting_and_searching)|[Built-in Sorting and Cheats](https://learning.teachme.codes/python/cheats/built_in_sorting_and_searching)|[Built-in Sorting and Projects](https://learning.teachme.codes/python/projects/built_in_sorting_and_searching)|[Sorting HOW TO](https://docs.python.org/3/howto/sorting.html)|
|[Type Conversion Functions](https://learning.teachme.codes/python/chapters/type_conversion_functions)|[Type Conversion QnAs](https://learning.teachme.codes/python/qnas/type_conversion_functions)|[Type Conversion Cheats](https://learning.teachme.codes/python/cheats/type_conversion_functions)|[Type Conversion Projects](https://learning.teachme.codes/python/projects/type_conversion_functions)|[Type Conversion](https://docs.python.org/3/library/functions.html#type-conversion)|
|[Object-Oriented Functions](https://learning.teachme.codes/python/chapters/object_oriented_functions)|[Object-Oriented QnAs](https://learning.teachme.codes/python/qnas/object_oriented_functions)|[Object-Oriented Cheats](https://learning.teachme.codes/python/cheats/object_oriented_functions)|[Object-Oriented Projects](https://learning.teachme.codes/python/projects/object_oriented_functions)|[Object-Oriented Programming](https://docs.python.org/3/tutorial/classes.html)|
|[Classes and Objects](https://learning.teachme.codes/python/chapters/classes_and_objects)|[Classes and QnAs](https://learning.teachme.codes/python/qnas/classes_and_objects)|[Classes and Cheats](https://learning.teachme.codes/python/cheats/classes_and_objects)|[Classes and Projects](https://learning.teachme.codes/python/projects/classes_and_objects)|[Classes](https://docs.python.org/3/tutorial/classes.html)|
|[Inheritance and Polymorphism](https://learning.teachme.codes/python/chapters/inheritance_and_polymorphism)|[Inheritance and QnAs](https://learning.teachme.codes/python/qnas/inheritance_and_polymorphism)|[Inheritance and Cheats](https://learning.teachme.codes/python/cheats/inheritance_and_polymorphism)|[Inheritance and Projects](https://learning.teachme.codes/python/projects/inheritance_and_polymorphism)|[Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)|
|[Encapsulation and Abstraction](https://learning.teachme.codes/python/chapters/encapsulation_and_abstraction)|[Encapsulation and QnAs](https://learning.teachme.codes/python/qnas/encapsulation_and_abstraction)|[Encapsulation and Cheats](https://learning.teachme.codes/python/cheats/encapsulation_and_abstraction)|[Encapsulation and Projects](https://learning.teachme.codes/python/projects/encapsulation_and_abstraction)|[Encapsulation](https://docs.python.org/3/tutorial/classes.html#private-variables)|
|[Magic Methods and Operator Overloading](https://learning.teachme.codes/python/chapters/magic_methods_and_operator_overloading)|[Magic Methods and QnAs](https://learning.teachme.codes/python/qnas/magic_methods_and_operator_overloading)|[Magic Methods and Cheats](https://learning.teachme.codes/python/cheats/magic_methods_and_operator_overloading)|[Magic Methods and Projects](https://learning.teachme.codes/python/projects/magic_methods_and_operator_overloading)|[Magic Methods](https://docs.python.org/3/reference/datamodel.html#special-method-names)|
|[Composition and Aggregation](https://learning.teachme.codes/python/chapters/composition_and_aggregation)|[Composition and QnAs](https://learning.teachme.codes/python/qnas/composition_and_aggregation)|[Composition and Cheats](https://learning.teachme.codes/python/cheats/composition_and_aggregation)|[Composition and Projects](https://learning.teachme.codes/python/projects/composition_and_aggregation)|[Composition and Aggregation](https://docs.python.org/3/tutorial/classes.html#tut-composition)|


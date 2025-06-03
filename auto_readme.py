topics = [
    "Introduction to Python and Setting Up Environment",
    "Printing, Comments, and Basic Syntax",
    "Variables and Data Types",
    "Basic Input and Output",
    "String Operations and Formatting",
    "Arithmetic and Assignment Operators",
    "Conditional Statements (if, else, elif)",
    "Comparison and Logical Operators",
    "Working with Lists",
    "Looping with for Loops",
    "Looping with while Loops",
    "List Comprehensions",
    "Tuples and Sets",
    "Dictionaries (Key-Value Pairs)",
    "Functions (Defining and Calling)",
    "Function Arguments and Return Values",
    "Scope and Global vs Local Variables",
    "Error Handling with try, except",
    "Working with Files (Read/Write)",
    "Modules and import Statement",
    "Built-in Functions (len, range, etc.)",
    "Creating and Using Custom Modules",
    "Object-Oriented Programming - Classes & Objects",
    "Class Attributes and Methods",
    "Inheritance and Polymorphism",
    "Working with External Libraries (math, random)",
    "Introduction to JSON and APIs",
    "Basic Project: Command-line Calculator",
    "Basic Project: To-Do List Manager",
    "Wrap-up and Next Steps (Flask, Django, etc.)"
]

# Short example code or exercise for each day
exercises = [
    "# No code today. Just install Python and your editor (VSCode, etc.)",
    'print("Hello, World!")  # Basic print statement',
    'name = "Alice"\nage = 25\nprint(name, age)',
    'user_input = input("Enter your name: ")\nprint("Hello", user_input)',
    'text = "Python"\nprint(text.upper())\nprint(len(text))',
    'a = 10\nb = 3\nprint(a + b, a - b, a * b, a / b)',
    'age = 18\nif age >= 18:\n    print("Adult")\nelse:\n    print("Minor")',
    'a = 5\nb = 10\nprint(a < b and b > 0)',
    'fruits = ["apple", "banana", "cherry"]\nprint(fruits[0])',
    'for i in range(5):\n    print("Number:", i)',
    'count = 0\nwhile count < 5:\n    print(count)\n    count += 1',
    'squares = [x*x for x in range(5)]\nprint(squares)',
    'my_tuple = (1, 2, 3)\nmy_set = {1, 2, 2, 3}\nprint(my_tuple)\nprint(my_set)',
    'person = {"name": "Alice", "age": 30}\nprint(person["name"])',
    'def greet():\n    print("Hello!")\ngreet()',
    'def add(x, y):\n    return x + y\nprint(add(3, 4))',
    'x = 5\ndef show():\n    x = 10\n    print(x)\nshow()\nprint(x)',
    'try:\n    print(10 / 0)\nexcept ZeroDivisionError:\n    print("Cannot divide by zero")',
    'with open("sample.txt", "w") as f:\n    f.write("Hello File")',
    'import math\nprint(math.sqrt(16))',
    'print(len("Python"))\nprint(range(5))',
    '# Create a file `mymodule.py` with a function, then import and use it here.',
    'class Person:\n    def __init__(self, name):\n        self.name = name\n    def greet(self):\n        print("Hi", self.name)',
    'p = Person("Alice")\np.greet()',
    'class Animal:\n    def speak(self):\n        print("Animal speaks")\nclass Dog(Animal):\n    def speak(self):\n        print("Bark")\nd = Dog()\nd.speak()',
    'import random\nprint(random.randint(1, 10))',
    'import json\ndata = {"name": "Alice"}\nprint(json.dumps(data))',
    'def calc():\n    a = int(input("a: "))\n    b = int(input("b: "))\n    print("Sum:", a + b)\ncalc()',
    'tasks = []\ntask = input("Enter a task: ")\ntasks.append(task)\nprint("Tasks:", tasks)',
    'print("You did it! Start building small apps or explore Flask/Django.")'
]

# Create a README.md file summarizing the 30-day beginner Python course

readme_content = "# 30-Day Beginner Python Challenge 🐍\n\n"
readme_content += "Welcome to the 30-day Python programming challenge! This challenge is designed to help beginners learn Python step-by-step through short lessons and exercises.\n\n"
readme_content += "## 📅 Daily Topics and Exercises\n\n"

for i in range(1, 31):
    readme_content += f"### Day {i}: {topics[i-1]}\n"
    readme_content += f"- **File**: `day_{i}.py`\n"
    readme_content += f"- **Overview**: {topics[i-1]}\n"
    readme_content += f"- **Exercise**:\n```python\n{exercises[i-1]}\n```\n\n"

readme_content += "---\n"
readme_content += "💡 **Tip**: Run each file in a Python environment and try modifying the examples to understand them better. Keep a notebook or markdown file to track what you learn every day.\n\n"
readme_content += "Happy coding! 🚀\n"

# Write the README file
readme_path = "README.md"
with open(readme_path, "w") as f:
    f.write(readme_content)

readme_path

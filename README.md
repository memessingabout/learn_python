# 30-Day Beginner Python Challenge 🐍

Welcome to the 30-day Python programming challenge! This challenge is designed to help beginners learn Python step-by-step through short lessons and exercises.

## 📅 Daily Topics and Exercises

### Day 1: Introduction to Python and Setting Up Environment

- **File**: `Roadmap_learning/day_1.py`
- **Overview**: Introduction to Python and Setting Up Environment
- **Exercise**:

```python
# No code today. Just install Python and your editor (VSCode, etc.)
```

### Day 2: Printing, Comments, and Basic Syntax

- **File**: `Roadmap_learning/day_2.py`
- **Overview**: Printing, Comments, and Basic Syntax
- **Exercise**:

```python
print("Hello, World!")  # Basic print statement
```

### Day 3: Variables and Data Types

- **File**: `Roadmap_learning/day_3.py`
- **Overview**: Variables and Data Types
- **Exercise**:

```python
name = "Alice"
age = 25
print(name, age)
```

### Day 4: Basic Input and Output

- **File**: `Roadmap_learning/day_4.py`
- **Overview**: Basic Input and Output
- **Exercise**:

```python
user_input = input("Enter your name: ")
print("Hello", user_input)
```

### Day 5: String Operations and Formatting

- **File**: `Roadmap_learning/day_5.py`
- **Overview**: String Operations and Formatting
- **Exercise**:

```python
text = "Python"
print(text.upper())
print(len(text))
```

### Day 6: Arithmetic and Assignment Operators

- **File**: `Roadmap_learning/day_6.py`
- **Overview**: Arithmetic and Assignment Operators
- **Exercise**:

```python
a = 10
b = 3
print(a + b, a - b, a * b, a / b)
```

### Day 7: Conditional Statements (if, else, elif)

- **File**: `Roadmap_learning/day_7.py`
- **Overview**: Conditional Statements (if, else, elif)
- **Exercise**:

```python
age = 18
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

### Day 8: Comparison and Logical Operators

- **File**: `Roadmap_learning/day_8.py`
- **Overview**: Comparison and Logical Operators
- **Exercise**:

```python
a = 5
b = 10
print(a < b and b > 0)
```

### Day 9: Working with Lists

- **File**: `Roadmap_learning/day_9.py`
- **Overview**: Working with Lists
- **Exercise**:

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])
```

### Day 10: Looping with for Loops

- **File**: `Roadmap_learning/day_10.py`
- **Overview**: Looping with for Loops
- **Exercise**:

```python
for i in range(5):
    print("Number:", i)
```

### Day 11: Looping with while Loops

- **File**: `Roadmap_learning/day_11.py`
- **Overview**: Looping with while Loops
- **Exercise**:

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### Day 12: List Comprehensions

- **File**: `Roadmap_learning/day_12.py`
- **Overview**: List Comprehensions
- **Exercise**:

```python
squares = [x*x for x in range(5)]
print(squares)
```

### Day 13: Tuples and Sets

- **File**: `Roadmap_learning/day_13.py`
- **Overview**: Tuples and Sets
- **Exercise**:

```python
my_tuple = (1, 2, 3)
my_set = {1, 2, 2, 3}
print(my_tuple)
print(my_set)
```

### Day 14: Dictionaries (Key-Value Pairs)

- **File**: `Roadmap_learning/day_14.py`
- **Overview**: Dictionaries (Key-Value Pairs)
- **Exercise**:

```python
person = {"name": "Alice", "age": 30}
print(person["name"])
```

### Day 15: Functions (Defining and Calling)

- **File**: `Roadmap_learning/day_15.py`
- **Overview**: Functions (Defining and Calling)
- **Exercise**:

```python
def greet():
    print("Hello!")
greet()
```

### Day 16: Function Arguments and Return Values

- **File**: `Roadmap_learning/day_16.py`
- **Overview**: Function Arguments and Return Values
- **Exercise**:

```python
def add(x, y):
    return x + y
print(add(3, 4))
```

### Day 17: Scope and Global vs Local Variables

- **File**: `Roadmap_learning/day_17.py`
- **Overview**: Scope and Global vs Local Variables
- **Exercise**:

```python
x = 5
def show():
    x = 10
    print(x)
show()
print(x)
```

### Day 18: Error Handling with try, except

- **File**: `Roadmap_learning/day_18.py`
- **Overview**: Error Handling with try, except
- **Exercise**:

```python
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")
```

### Day 19: Working with Files (Read/Write)

- **File**: `Roadmap_learning/day_19.py`
- **Overview**: Working with Files (Read/Write)
- **Exercise**:

```python
with open("sample.txt", "w") as f:
    f.write("Hello File")
```

### Day 20: Modules and import Statement

- **File**: `Roadmap_learning/day_20.py`
- **Overview**: Modules and import Statement
- **Exercise**:

```python
import math
print(math.sqrt(16))
```

### Day 21: Built-in Functions (len, range, etc.)

- **File**: `Roadmap_learning/day_21.py`
- **Overview**: Built-in Functions (len, range, etc.)
- **Exercise**:

```python
print(len("Python"))
print(range(5))
```

### Day 22: Creating and Using Custom Modules

- **File**: `Roadmap_learning/day_22.py`
- **Overview**: Creating and Using Custom Modules
- **Exercise**:

```python
# Create a file `mymodule.py` with a function, then import and use it here.
```

### Day 23: Object-Oriented Programming - Classes & Objects

- **File**: `Roadmap_learning/day_23.py`
- **Overview**: Object-Oriented Programming - Classes & Objects
- **Exercise**:

```python
class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print("Hi", self.name)
```

### Day 24: Class Attributes and Methods

- **File**: `Roadmap_learning/day_24.py`
- **Overview**: Class Attributes and Methods
- **Exercise**:

```python
p = Person("Alice")
p.greet()
```

### Day 25: Inheritance and Polymorphism

- **File**: `Roadmap_learning/day_25.py`
- **Overview**: Inheritance and Polymorphism
- **Exercise**:

```python
class Animal:
    def speak(self):
        print("Animal speaks")
class Dog(Animal):
    def speak(self):
        print("Bark")
d = Dog()
d.speak()
```

### Day 26: Working with External Libraries (math, random)

- **File**: `Roadmap_learning/day_26.py`
- **Overview**: Working with External Libraries (math, random)
- **Exercise**:

```python
import random
print(random.randint(1, 10))
```

### Day 27: Introduction to JSON and APIs

- **File**: `Roadmap_learning/day_27.py`
- **Overview**: Introduction to JSON and APIs
- **Exercise**:

```python
import json
data = {"name": "Alice"}
print(json.dumps(data))
```

### Day 28: Basic Project: Command-line Calculator

- **File**: `Roadmap_learning/day_28.py`
- **Overview**: Basic Project: Command-line Calculator
- **Exercise**:

```python
def calc():
    a = int(input("a: "))
    b = int(input("b: "))
    print("Sum:", a + b)
calc()
```

### Day 29: Basic Project: To-Do List Manager

- **File**: `Roadmap_learning/day_29.py`
- **Overview**: Basic Project: To-Do List Manager
- **Exercise**:

```python
tasks = []
task = input("Enter a task: ")
tasks.append(task)
print("Tasks:", tasks)
```

### Day 30: Wrap-up and Next Steps (Flask, Django, etc.)

- **File**: `Roadmap_learning/day_30.py`
- **Overview**: Wrap-up and Next Steps (Flask, Django, etc.)
- **Exercise**:

```python
print("You did it! Start building small apps or explore Flask/Django.")
```

## 🧩 Mini-Projects to Reinforce Learning

Apply your knowledge with these increasingly challenging projects:

1. **Beginner (Days 1-10)**

   - **Command-line Calculator**: Create a simple calculator that performs basic operations
   - **Number Guessing Game**: Generate a random number and let the user guess it
2. **Intermediate (Days 11-20)**

   - **Todo List Application**: Create a command-line todo list with add/remove/list functionality
   - **File Organizer**: Write a script that organizes files in a directory by type
3. **Advanced (Days 21-30)**

   - **Data Analysis Tool**: Build a tool to analyze and visualize data from CSV files
   - **Web Scraper**: Create a script that extracts information from websites

## 📊 Track Your Progress

Keep track of your learning journey with this checklist:

- [ ] **Phase 1: Foundations** (Days 1-15)

  - [ ] Completed all daily exercises
  - [ ] Built at least one beginner project
  - [ ] Reviewed and understood all concepts in `phase_one.py`
- [ ] **Phase 2: Intermediate** (Days 16-25)

  - [ ] Completed all daily exercises
  - [ ] Built at least one intermediate project
  - [ ] Reviewed and understood all concepts in `phase_two.py`
- [ ] **Phase 3: Advanced** (Days 26-30)

  - [ ] Completed all daily exercises
  - [ ] Built at least one advanced project
  - [ ] Started exploring specialized Python domains

## 🧠 Algorithm Practice

Improve your problem-solving skills with these algorithm challenges:

1. **Two-Pointer Technique** (`two_pointer.py`)

   - Master efficient array manipulation techniques
   - Solve increasingly complex problems
2. **Data Structures** (`python_data_structures.md`)

   - Understand core Python data structures
   - Practice implementation and manipulation

## 📘 Additional Resources

- **Official Python Documentation**: [docs.python.org](https://docs.python.org)
- **Real Python**: [realpython.com](https://realpython.com)
- **Python Algorithms Book**: "Grokking Algorithms" by Aditya Bhargava
- **Interactive Practice**: [LeetCode](https://leetcode.com), [HackerRank](https://hackerrank.com)

## 💡 Tips for Success

1. **Code daily**: Consistent practice is more important than marathon sessions
2. **Build projects**: Apply what you learn immediately to cement understanding
3. **Read other code**: Study the implementation in `soln.py` and other files
4. **Take notes**: Document your learning journey and insights
5. **Join communities**: Connect with other Python learners online

---

💡 **Remember**: Learning to code is a marathon, not a sprint. Celebrate small victories and be patient with yourself!

Happy coding! 🚀

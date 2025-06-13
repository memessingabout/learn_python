""" Day 12: List Comprehensions """

"""
List comprehensions provide a concise way to create lists.
Syntax: [expression for item in iterable if condition]
"""

# Basic list comprehension
squares = [x*x for x in range(5)]
print(f"Squares: {squares}")

# List comprehension with condition
even_squares = [x*x for x in range(10) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Working with strings
names = ["alice", "bob", "charlie", "diana"]
capitalized_names = [name.capitalize() for name in names]
print(f"Capitalized names: {capitalized_names}")

# Filtering with conditions
long_names = [name for name in names if len(name) > 4]
print(f"Names longer than 4 characters: {long_names}")

# Nested list comprehension
matrix = [[i + j for j in range(3)] for i in range(3)]
print(f"Matrix: {matrix}")

# Converting nested loops to list comprehension
# Traditional approach:
result_traditional = []
for x in range(3):
    for y in range(3):
        if x != y:
            result_traditional.append((x, y))

# List comprehension approach:
result_comprehension = [(x, y) for x in range(3) for y in range(3) if x != y]
print(f"Traditional approach: {result_traditional}")
print(f"List comprehension: {result_comprehension}")

# Practical example: Processing data
temperatures_celsius = [0, 20, 30, 40]
temperatures_fahrenheit = [c * 9/5 + 32 for c in temperatures_celsius]
print(f"Celsius: {temperatures_celsius}")
print(f"Fahrenheit: {temperatures_fahrenheit}")

# Dictionary comprehension (bonus)
word_lengths = {word: len(word) for word in names}
print(f"Word lengths: {word_lengths}")

# Set comprehension (bonus)
unique_lengths = {len(word) for word in names}
print(f"Unique word lengths: {unique_lengths}")

""" Day 13: Tuples and Sets """

"""
TUPLES:
- Ordered, immutable collections
- Allow duplicate values
- Use parentheses () or just comma separation
- Useful for data that shouldn't change

SETS:
- Unordered, mutable collections
- No duplicate values allowed
- Use curly braces {} or set() function
- Useful for removing duplicates and set operations
"""

# ===== TUPLES =====
print("=== TUPLES ===")

# Creating tuples
my_tuple = (1, 1, 3, 2, 5, 4, 2, 3)
coordinates = (10.5, 20.3)
single_item_tuple = (42,)  # Note the comma for single item
empty_tuple = ()

print(f"Original tuple: {my_tuple}")
print(f"Coordinates: {coordinates}")
print(f"Single item tuple: {single_item_tuple}")

# Tuple operations
print(f"Length: {len(my_tuple)}")
print(f"Count of 1: {my_tuple.count(1)}")
print(f"Index of 3: {my_tuple.index(3)}")
print(f"First element: {my_tuple[0]}")
print(f"Last element: {my_tuple[-1]}")
print(f"Slice [1:4]: {my_tuple[1:4]}")

# Tuple unpacking
x, y = coordinates
print(f"Unpacked coordinates: x={x}, y={y}")

# Multiple assignment with tuples
name, age, city = ("Alice", 30, "New York")
print(f"Name: {name}, Age: {age}, City: {city}")

# ===== SETS =====
print("\n=== SETS ===")

# Creating sets
cleaned_my_tuple = set(my_tuple)  # Remove duplicates from tuple
my_set = {1, 2, 2, 3}  # Duplicates automatically removed
colors_set = {"red", "green", "blue", "red"}

print(f"Set from tuple (duplicates removed): {cleaned_my_tuple}")
print(f"Set with duplicates: {my_set}")
print(f"Colors set: {colors_set}")

# Set operations
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print(f"Union (A | B): {set_a | set_b}")
print(f"Intersection (A & B): {set_a & set_b}")
print(f"Difference (A - B): {set_a - set_b}")
print(f"Symmetric difference (A ^ B): {set_a ^ set_b}")

# Set methods
fruits = {"apple", "banana", "cherry"}
print(f"Original fruits: {fruits}")

fruits.add("orange")
print(f"After adding orange: {fruits}")

fruits.update(["mango", "grape"])
print(f"After updating with list: {fruits}")

fruits.discard("banana")  # Won't raise error if not found
print(f"After discarding banana: {fruits}")

# Practical example: Finding common elements
student_a_subjects = {"math", "physics", "chemistry", "biology"}
student_b_subjects = {"math", "chemistry", "english", "history"}

common_subjects = student_a_subjects & student_b_subjects
unique_to_a = student_a_subjects - student_b_subjects
all_subjects = student_a_subjects | student_b_subjects

print(f"\nStudent A subjects: {student_a_subjects}")
print(f"Student B subjects: {student_b_subjects}")
print(f"Common subjects: {common_subjects}")
print(f"Unique to A: {unique_to_a}")
print(f"All subjects: {all_subjects}")

# Converting between data types
numbers_list = [1, 2, 3, 2, 1, 4, 5, 4]
unique_numbers = list(set(numbers_list))  # Remove duplicates and convert back
print(f"Original list: {numbers_list}")
print(f"Unique numbers: {unique_numbers}")




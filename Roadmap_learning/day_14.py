""" Day 14: Dictionaries (Key-Value Pairs) """

"""
Dictionaries are mutable collections of key-value pairs.
- Keys must be immutable (strings, numbers, tuples)
- Values can be any data type
- Use curly braces {} with key: value pairs
- Very efficient for lookups by key
"""

# ===== CREATING DICTIONARIES =====
print("=== CREATING DICTIONARIES ===")

person = {
    "name": "Alice", 
    "age": 30,
    "city": "New York",
    "skills": ["Python", "JavaScript", "SQL"]
}

# Alternative ways to create dictionaries
empty_dict = {}
dict_from_constructor = dict(name="Bob", age=25)
dict_from_tuples = dict([("x", 1), ("y", 2)])

print(f"Person: {person}")
print(f"From constructor: {dict_from_constructor}")
print(f"From tuples: {dict_from_tuples}")

# ===== ACCESSING VALUES =====
print("\n=== ACCESSING VALUES ===")

print(f"Name: {person['name']}")
print(f"Age using get(): {person.get('age')}")
print(f"Country (with default): {person.get('country', 'Unknown')}")

# Safe access with get() vs direct access
# person["country"]  # This would raise KeyError
print(f"Safe access: {person.get('country', 'Not specified')}")

# ===== MODIFYING DICTIONARIES =====
print("\n=== MODIFYING DICTIONARIES ===")

# Adding/updating values
person["country"] = "USA"
person["age"] = 31  # Update existing key
person.update({"email": "alice@email.com", "phone": "123-456-7890"})

print(f"After updates: {person}")

# Removing items
removed_phone = person.pop("phone")
print(f"Removed phone: {removed_phone}")
print(f"After removing phone: {person}")

# ===== DICTIONARY METHODS =====
print("\n=== DICTIONARY METHODS ===")

print(f"Keys: {list(person.keys())}")
print(f"Values: {list(person.values())}")
print(f"Items: {list(person.items())}")

# Check if key exists
print(f"Has 'name': {'name' in person}")
print(f"Has 'salary': {'salary' in person}")

# ===== ITERATING THROUGH DICTIONARIES =====
print("\n=== ITERATING THROUGH DICTIONARIES ===")

# Iterate through key-value pairs
print("Key-Value pairs:")
for key, value in person.items():
    print(f"  {key}: {value}")

# Iterate through keys only
print("\nKeys only:")
for key in person:  # Same as person.keys()
    print(f"  {key}")

# Iterate through values only
print("\nValues only:")
for value in person.values():
    print(f"  {value}")

# ===== NESTED DICTIONARIES =====
print("\n=== NESTED DICTIONARIES ===")

company = {
    "employees": {
        "alice": {"age": 30, "department": "Engineering"},
        "bob": {"age": 25, "department": "Marketing"},
        "charlie": {"age": 35, "department": "Sales"}
    },
    "departments": ["Engineering", "Marketing", "Sales", "HR"]
}

print(f"Alice's department: {company['employees']['alice']['department']}")
print(f"All departments: {company['departments']}")

# ===== DICTIONARY COMPREHENSIONS =====
print("\n=== DICTIONARY COMPREHENSIONS ===")

# Create a dictionary of squares
squares_dict = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares_dict}")

# Filter dictionary based on condition
high_performers = {name: info for name, info in company["employees"].items() 
                  if info["age"] >= 30}
print(f"Employees 30+: {high_performers}")

# Transform values
upper_departments = {name: info["department"].upper() 
                    for name, info in company["employees"].items()}
print(f"Uppercase departments: {upper_departments}")

# ===== PRACTICAL EXAMPLES =====
print("\n=== PRACTICAL EXAMPLES ===")

# Word frequency counter
text = "hello world hello python world"
word_count = {}
for word in text.split():
    word_count[word] = word_count.get(word, 0) + 1
print(f"Word frequency: {word_count}")

# Using dictionary as a lookup table
grade_scale = {
    90: "A", 85: "B+", 80: "B", 75: "C+", 
    70: "C", 65: "D+", 60: "D", 0: "F"
}

def get_letter_grade(score):
    for min_score in sorted(grade_scale.keys(), reverse=True):
        if score >= min_score:
            return grade_scale[min_score]
    return "F"

test_scores = [95, 87, 73, 68, 55]
for score in test_scores:
    print(f"Score {score}: Grade {get_letter_grade(score)}")

# Grouping data
students = [
    {"name": "Alice", "grade": "A", "subject": "Math"},
    {"name": "Bob", "grade": "B", "subject": "Math"},
    {"name": "Charlie", "grade": "A", "subject": "Science"},
    {"name": "Alice", "grade": "B+", "subject": "Science"}
]

# Group by subject
subjects_dict = {}
for student in students:
    subject = student["subject"]
    if subject not in subjects_dict:
        subjects_dict[subject] = []
    subjects_dict[subject].append(student)

print(f"\nGrouped by subject: {subjects_dict}")


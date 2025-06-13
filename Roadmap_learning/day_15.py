""" Day 15: Functions (Defining and Calling) """

"""
Functions are reusable blocks of code that perform specific tasks.
Key concepts:
- Parameters: inputs to the function (defined in function signature)
- Arguments: actual values passed to the function when called
- Return values: output from the function
- Scope: where variables can be accessed
"""

# ===== BASIC FUNCTION DEFINITION =====
print("=== BASIC FUNCTIONS ===")

def greet(name):
    """Simple function that takes one parameter and returns a string."""
    return f"Hello, {name}!"

def calculate_area(length, width):
    """Function with multiple parameters."""
    area = length * width
    return area

# Function calls
greeting = greet("Alice")
print(greeting)

area = calculate_area(5, 3)
print(f"Area: {area}")

# ===== FUNCTION ARGUMENTS TYPES =====
print("\n=== FUNCTION ARGUMENT TYPES ===")

def comprehensive_function(pos_arg, default_arg="default", *args, **kwargs):
    """
    Demonstrates all types of function arguments:
    - pos_arg: positional argument (required)
    - default_arg: default argument (optional)
    - *args: variable positional arguments (tuple)
    - **kwargs: variable keyword arguments (dictionary)
    """
    print(f"Positional: {pos_arg}")
    print(f"Default: {default_arg}")
    print(f"Extra positional (*args): {args}")
    print(f"Keyword (**kwargs): {kwargs}")
    print("-" * 30)

# Different ways to call the function:
print("1. Positional arguments only:")
comprehensive_function("Hello")

print("\n2. Keyword arguments:")
comprehensive_function(pos_arg="Hello", default_arg="Custom")

print("\n3. Mixed usage:")
comprehensive_function("Hello", "Custom", "extra1", "extra2", name="Grace", age=25)

# ===== RETURN VALUES =====
print("\n=== RETURN VALUES ===")

def no_return():
    """Function with no explicit return (returns None)."""
    print("This function doesn't return anything")

def single_return(x):
    """Function returning a single value."""
    return x * 2

def multiple_return(a, b):
    """Function returning multiple values (as a tuple)."""
    return a + b, a - b, a * b, a / b if b != 0 else None

# Examples of return values
result1 = no_return()  # Returns None
print(f"No return result: {result1}")

result2 = single_return(5)
print(f"Single return: {result2}")

# Unpacking multiple return values
sum_val, diff_val, prod_val, div_val = multiple_return(10, 3)
print(f"Multiple returns: sum={sum_val}, diff={diff_val}, prod={prod_val}, div={div_val}")

# ===== SCOPE AND VARIABLES =====
print("\n=== SCOPE AND VARIABLES ===")

global_var = "I'm global"

def scope_example():
    local_var = "I'm local"
    print(f"Inside function - Global: {global_var}")
    print(f"Inside function - Local: {local_var}")
    
    # Modifying global variable
    global global_var
    global_var = "Modified global"

print(f"Before function call: {global_var}")
scope_example()
print(f"After function call: {global_var}")

# ===== LAMBDA FUNCTIONS =====
print("\n=== LAMBDA FUNCTIONS ===")

# Simple lambda functions
square = lambda x: x ** 2
add = lambda a, b: a + b

print(f"Square of 5: {square(5)}")
print(f"Add 3 and 7: {add(3, 7)}")

# Lambda with built-in functions
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(f"Original: {numbers}")
print(f"Squared: {squared_numbers}")
print(f"Even numbers: {even_numbers}")

# ===== FUNCTION DECORATORS (BASIC) =====
print("\n=== BASIC DECORATORS ===")

def timer_decorator(func):
    """A simple decorator that prints when a function is called."""
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} completed")
        return result
    return wrapper

@timer_decorator
def slow_function():
    """Function with decorator applied."""
    import time
    time.sleep(0.1)  # Simulate slow operation
    return "Task completed"

result = slow_function()
print(f"Result: {result}")

# ===== PRACTICAL EXAMPLES =====
print("\n=== PRACTICAL EXAMPLES ===")

def validate_email(email):
    """Simple email validation function."""
    return "@" in email and "." in email.split("@")[-1]

def calculate_grade(scores):
    """Calculate average grade and letter grade."""
    if not scores:
        return 0, "F"
    
    average = sum(scores) / len(scores)
    
    if average >= 90:
        letter = "A"
    elif average >= 80:
        letter = "B"
    elif average >= 70:
        letter = "C"
    elif average >= 60:
        letter = "D"
    else:
        letter = "F"
    
    return average, letter

def fibonacci(n):
    """Generate fibonacci sequence up to n terms."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    
    return fib_sequence

# Test practical functions
emails = ["test@example.com", "invalid-email", "user@domain.org"]
for email in emails:
    print(f"{email}: {'Valid' if validate_email(email) else 'Invalid'}")

student_scores = [85, 92, 78, 96, 88]
avg, letter = calculate_grade(student_scores)
print(f"Scores: {student_scores}")
print(f"Average: {avg:.1f}, Grade: {letter}")

fib_numbers = fibonacci(10)
print(f"First 10 Fibonacci numbers: {fib_numbers}")

# ===== FUNCTION CALLING OTHER FUNCTIONS =====
print("\n=== FUNCTIONS CALLING OTHER FUNCTIONS ===")

def format_name(first, last):
    """Format a person's name."""
    return f"{first.title()} {last.title()}"

def create_email(first, last, domain="company.com"):
    """Create an email address from name components."""
    formatted_name = format_name(first, last)
    email = f"{first.lower()}.{last.lower()}@{domain}"
    return formatted_name, email

def process_employee(first, last, scores):
    """Process employee data: format name, create email, calculate grade."""
    name, email = create_email(first, last)
    avg_score, grade = calculate_grade(scores)
    
    return {
        "name": name,
        "email": email,
        "average_score": avg_score,
        "grade": grade
    }

# Example usage
employee_data = process_employee("john", "doe", [88, 92, 85, 90])
print("Employee processed:")
for key, value in employee_data.items():
    print(f"  {key}: {value}")

# ===== RECURSIVE FUNCTIONS =====
print("\n=== RECURSIVE FUNCTIONS ===")

def factorial(n):
    """Calculate factorial using recursion."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def countdown(n):
    """Countdown function using recursion."""
    if n <= 0:
        print("Done!")
    else:
        print(n)
        countdown(n - 1)

print(f"Factorial of 5: {factorial(5)}")
print("Countdown from 5:")
countdown(5)
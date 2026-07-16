# Functions in Python

# Basic function
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")

# Function that returns a value
def add(a, b):
    return a + b

result = add(3, 4)
print(result)

# Default parameter value
def greet_with_title(name, title="Mr"):
    print(f"Hello, {title}. {name}!")

greet_with_title("Smith")
greet_with_title("Jones", "Dr")

# Multiple return values
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([4, 1, 7, 2, 9])
print(low, high)

# *args - accept any number of arguments
def total(*args):
    return sum(args)

print(total(1, 2, 3))
print(total(10, 20, 30, 40))

# **kwargs - accept any number of keyword arguments
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_info(name="Alice", age=30, city="NYC")

# Simple recursion
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120

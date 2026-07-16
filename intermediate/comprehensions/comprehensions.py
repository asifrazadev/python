# List, Set, and Dict Comprehensions in Python

# 1. List Comprehensions
numbers = [1, 2, 3, 4, 5, 6]

# Convert all values
squares = [x * x for x in numbers]
print(f"Squares: {squares}")

# Filter values
evens = [x for x in numbers if x % 2 == 0]
print(f"Evens: {evens}")

# 2. Set Comprehensions
# A set stores unique values, useful for deduplicating transformed data
messy_numbers = [1, 2, 2, 3, 4, 4, 5]
unique_squares = {x * x for x in messy_numbers}
print(f"Unique Squares Set: {unique_squares}")

# 3. Dict Comprehensions
names = ["Alice", "Bob", "Charlie"]
salaries = [5000, 7000, 8000]

# Combine lists into a dictionary using zip
salary_dict = {name: salary for name, salary in zip(names, salaries)}
print(f"Salary Dict: {salary_dict}")

# Transform key-value pairs
bonus_dict = {name: salary * 1.1 for name, salary in salary_dict.items() if salary < 8000}
print(f"Bonus Dict: {bonus_dict}")

# Variables & Data Types

# Basic assignment
name = "Alice"
age = 30
height = 5.7
is_student = True
nothing = None

print(name)
print(age)
print(height)
print(is_student)
print(nothing)

# Check the type
print(type(name))
print(type(age))

# Multiple assignment
x = y = z = 0
a, b, c = 1, 2, 3

print(x, y, z)
print(a, b, c)

# Swap two variables
a, b = b, a
print(a, b)

# Delete a variable
temp = "temporary"
print(temp)
del temp
# print(temp)  # would cause NameError

# Constants (UPPER_CASE by convention)
MAX_SCORE = 100
PI = 3.14159

print(MAX_SCORE)
print(PI)

# Exception Handling in Python
# Prevents your program from crashing when something goes wrong

# Basic try / except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Catch the error message
try:
    number = int("hello")
except ValueError as e:
    print(f"Error: {e}")

# Multiple except blocks
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Please use numbers"

print(divide(10, 2))
print(divide(10, 0))
print(divide(10, "x"))

# try / except / else / finally
try:
    number = int("42")
except ValueError:
    print("Not a valid number")
else:
    print(f"Success! Number is {number}")  # runs only if no error
finally:
    print("This always runs")              # cleanup code goes here

# Raise your own error
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    print(f"Age set to {age}")

try:
    set_age(-5)
except ValueError as e:
    print(f"Error: {e}")

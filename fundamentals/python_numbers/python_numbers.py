# Numbers in Python

# Integers
x = 10
y = 3

print(x + y)   # addition
print(x - y)   # subtraction
print(x * y)   # multiplication
print(x / y)   # division (always float)
print(x // y)  # floor division (whole number)
print(x % y)   # remainder (modulo)
print(x ** y)  # power (10 to the power of 3)

# Floats
pi = 3.14
print(pi)
print(round(pi, 1))  # round to 1 decimal place

# Useful math functions (no import needed)
print(abs(-5))    # absolute value -> 5
print(min(3, 7))  # smallest
print(max(3, 7))  # largest

# Convert between types
print(int(3.9))   # -> 3  (cuts off decimal, does NOT round)
print(float(5))   # -> 5.0
print(str(42))    # -> "42"

# Checking if a number is even or odd
number = 7
if number % 2 == 0:
    print("even")
else:
    print("odd")

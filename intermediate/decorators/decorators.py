# Decorators in Python

import time

# A decorator function takes another function as argument,
# extends its behavior, and returns a new wrapper function.
def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {(end - start) * 1000:.2f} milliseconds to execute.")
        return result
    return wrapper

# Using the decorator using the @ syntax
@time_it
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number * number)
    return result

@time_it
def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number * number * number)
    return result

# Test decorators
nums = range(1, 100000)

squares = calc_square(nums)
cubes = calc_cube(nums)

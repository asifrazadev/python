# Generators in Python

# A Generator function uses yield instead of return
def fibonacci_generator(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

# Using the generator function
fib = fibonacci_generator(100)

print(next(fib))  # 0
print(next(fib))  # 1
print(next(fib))  # 1
print(next(fib))  # 2

print("\nLooping the remaining values:")
for val in fib:
    print(val, end=" ")
print()

print("-" * 20)

# Generator Expression (memory-efficient shorthand for comprehensions)
# Uses parentheses () instead of square brackets []
squares_gen = (x * x for x in range(1000000))

# Printing only first few items
print(next(squares_gen))
print(next(squares_gen))
print(next(squares_gen))
# Notice: No list of 1 million items was created in memory!

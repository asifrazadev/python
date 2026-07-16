# Lists in Python

fruits = ["apple", "banana", "cherry"]

# Access items
print(fruits[0])   # first
print(fruits[-1])  # last

# Add items
fruits.append("mango")
print(fruits)

# Insert at a position
fruits.insert(1, "orange")
print(fruits)

# Remove items
fruits.remove("banana")  # remove by value
print(fruits)

popped = fruits.pop()    # remove last item
print(popped)
print(fruits)

# Check if item is in list
print("apple" in fruits)

# Length
print(len(fruits))

# Loop through
for fruit in fruits:
    print(fruit)

# Sort
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
print(numbers)

# Reverse
numbers.reverse()
print(numbers)

# List from a range
nums = list(range(1, 6))
print(nums)

# Simple list comprehension
squares = [x * x for x in range(1, 6)]
print(squares)

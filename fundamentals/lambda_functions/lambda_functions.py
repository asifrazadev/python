# Lambda Functions in Python
# A lambda is a small, one-line anonymous function

# Basic syntax: lambda parameters: expression
square = lambda x: x * x
print(square(5))   # 25

add = lambda x, y: x + y
print(add(3, 4))   # 7

# Most useful with sorted()
words = ["banana", "apple", "cherry", "date"]

# sort by length of word
by_length = sorted(words, key=lambda w: len(w))
print(by_length)

# sort by last character
by_last = sorted(words, key=lambda w: w[-1])
print(by_last)

# sort list of dicts by a field
people = [
    {"name": "Charlie", "age": 32},
    {"name": "Alice",   "age": 25},
    {"name": "Bob",     "age": 28},
]
by_age = sorted(people, key=lambda p: p["age"])
for p in by_age:
    print(p["name"], p["age"])

# map() - apply function to each item
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

# filter() - keep items where function returns True
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

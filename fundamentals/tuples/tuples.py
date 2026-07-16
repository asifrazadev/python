# Tuples in Python
# Like a list but CANNOT be changed after creation

colors = ("red", "green", "blue")
print(colors)

# Access items (same as list)
print(colors[0])
print(colors[-1])

# Cannot change a tuple
# colors[0] = "yellow"  # this would cause an error

# Length
print(len(colors))

# Check membership
print("red" in colors)

# Unpack into variables
r, g, b = colors
print(r, g, b)

# Swap variables
x = 10
y = 20
x, y = y, x
print(x, y)

# Single item tuple needs a trailing comma
single = (42,)
print(type(single))   # <class 'tuple'>
not_tuple = (42)
print(type(not_tuple))  # <class 'int'>

# Tuples can be used as dictionary keys (lists cannot)
locations = {
    (40.71, -74.00): "New York",
    (51.50, -0.12):  "London"
}
print(locations[(40.71, -74.00)])

# Count and find
t = (1, 2, 2, 3, 2)
print(t.count(2))   # how many times 2 appears
print(t.index(3))   # index of first 3

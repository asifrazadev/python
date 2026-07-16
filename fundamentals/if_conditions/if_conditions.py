# If Conditions in Python

age = 20

# Basic if / elif / else
if age >= 18:
    print("adult")
elif age >= 13:
    print("teenager")
else:
    print("child")

# Comparison operators
x = 10
y = 20
print(x == y)   # equal
print(x != y)   # not equal
print(x < y)    # less than
print(x > y)    # greater than
print(x <= y)   # less than or equal
print(x >= y)   # greater than or equal

# Logical operators
has_ticket = True
has_id = False

if has_ticket and has_id:
    print("entry allowed")
elif has_ticket or has_id:
    print("partial entry")
else:
    print("no entry")

# not operator
is_raining = False
if not is_raining:
    print("go outside")

# Check if something is in a list
fruits = ["apple", "banana", "cherry"]
if "apple" in fruits:
    print("apple is in the list")

# Ternary (one-line if)
score = 75
result = "pass" if score >= 50 else "fail"
print(result)

# Truthy and falsy values
# These are all False: 0, "", [], {}, None, False
name = ""
if name:
    print("has name")
else:
    print("no name")  # prints this because "" is falsy

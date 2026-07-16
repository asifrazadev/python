# Strings in Python

name = "Alice"
greeting = "Hello, World!"

# Print and basic info
print(greeting)
print(len(greeting))  # number of characters

# Uppercase and lowercase
print(greeting.upper())
print(greeting.lower())

# Remove extra spaces
messy = "  hello  "
print(messy.strip())

# Replace part of a string
print(greeting.replace("World", "Python"))

# Check if something is inside
print("Hello" in greeting)   # True
print("Bye" in greeting)     # False

# Split into a list
sentence = "apple,banana,cherry"
fruits = sentence.split(",")
print(fruits)

# Join a list into a string
joined = " - ".join(fruits)
print(joined)

# Slicing
word = "Python"
print(word[0])     # first letter
print(word[-1])    # last letter
print(word[0:3])   # first 3 letters
print(word[::-1])  # reversed

# f-strings (best way to format)
age = 25
print(f"My name is {name} and I am {age} years old.")

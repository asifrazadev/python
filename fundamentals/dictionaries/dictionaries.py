# Dictionaries in Python

person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Access a value
print(person["name"])
print(person.get("age"))
print(person.get("email", "not found"))  # safe - returns default if missing

# Add / update
person["email"] = "alice@example.com"
person["age"] = 31
print(person)

# Remove
del person["city"]
print(person)

# Check if key exists
print("name" in person)
print("city" in person)

# Loop through keys and values
for key, value in person.items():
    print(f"{key}: {value}")

# All keys and all values
print(list(person.keys()))
print(list(person.values()))

# Length
print(len(person))

# Nested dictionary
student = {
    "name": "Bob",
    "grades": {
        "math": 90,
        "english": 85
    }
}

print(student["grades"]["math"])

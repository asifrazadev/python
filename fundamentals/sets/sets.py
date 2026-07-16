# Sets in Python
# A set stores unique items only - no duplicates, no order

fruits = {"apple", "banana", "cherry"}
print(fruits)

# Duplicates are automatically removed
numbers = {1, 2, 2, 3, 3, 3, 4}
print(numbers)  # {1, 2, 3, 4}

# Add and remove
fruits.add("mango")
print(fruits)

fruits.discard("banana")  # safe - no error if not found
print(fruits)

# Check membership (very fast)
print("apple" in fruits)
print("grape" in fruits)

# Set operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)   # union - all items from both
print(A & B)   # intersection - items in both
print(A - B)   # difference - in A but not in B

# Remove duplicates from a list
my_list = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(my_list))
print(unique)

# Sets and Frozen Sets in Python

# Normal Set (mutable, can add or remove elements)
basket = {"apple", "orange", "apple", "pear", "orange", "banana"}
print(f"Normal set: {basket} (duplicates automatically removed)")

basket.add("grape")
basket.discard("pear")
print(f"After add/discard: {basket}")

print("-" * 20)

# Frozen Set (immutable, CANNOT add/remove elements, is hashable)
frozen_basket = frozenset(["apple", "orange", "banana"])
print(f"Frozen set: {frozen_basket}")

# frozen_basket.add("grape") # raises AttributeError

# Why use a frozen set?
# 1. As a key in a dictionary (normal sets cannot be keys because they are mutable)
location_info = {
    frozenset(["London", "UK"]): "Europe",
    frozenset(["New York", "USA"]): "North America"
}
print(f"Lookup using frozenset key: {location_info[frozenset(['UK', 'London'])]}")

# 2. As an element inside another set (sets cannot contain normal sets)
set_of_sets = {frozenset([1, 2]), frozenset([3, 4])}
print(f"Set of frozensets: {set_of_sets}")

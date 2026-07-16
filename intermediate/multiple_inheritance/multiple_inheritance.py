# Multiple Inheritance in Python

# Base Class 1
class Father:
    def skills(self):
        print("I enjoy gardening and programming.")

    def personality(self):
        print("I am calm.")

# Base Class 2
class Mother:
    def skills(self):
        print("I enjoy painting and cooking.")

    def personality(self):
        print("I am outgoing.")

# Child Class inheriting from BOTH Father and Mother
class Child(Father, Mother):
    def skills(self):
        # We can call parent skills explicitly if we want both
        Father.skills(self)
        Mother.skills(self)
        print("I also enjoy sports!")

# Create Child object
c = Child()
c.skills()

print("-" * 20)

# Method Resolution Order (MRO)
# Which personality does the Child get?
# Since Father is listed first in Class definition `Child(Father, Mother)`,
# Python resolves it in Father first.
c.personality()

# Print the MRO order
print("\nMethod Resolution Order (MRO):")
for cls in Child.__mro__:
    print(cls.__name__)

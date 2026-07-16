# For Loops in Python

# Loop over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop with range
for i in range(5):        # 0 to 4
    print(i)

for i in range(1, 6):     # 1 to 5
    print(i)

for i in range(0, 10, 2): # 0, 2, 4, 6, 8
    print(i)

# Loop over a string
for letter in "hello":
    print(letter)

# enumerate - get index and value together
for index, fruit in enumerate(fruits):
    print(index, fruit)

# zip - loop two lists together
names = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 92]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# while loop
count = 0
while count < 5:
    print(count)
    count += 1

# break - stop the loop early
for i in range(10):
    if i == 5:
        break
    print(i)

# continue - skip to next iteration
for i in range(10):
    if i % 2 == 0:
        continue   # skip even numbers
    print(i)

# nested loops
for row in range(1, 4):
    for col in range(1, 4):
        print(f"({row},{col})", end=" ")
    print()

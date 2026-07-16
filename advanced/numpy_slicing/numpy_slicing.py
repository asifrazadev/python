# NumPy Slicing, Stacking, and Boolean Indexing in Python

import numpy as np

# 1. 2D Slicing
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original 2D Array:\n", a)

# Slice syntax: [row_slice, col_slice]
print("Row index 1, Col index 2: ", a[1, 2]) # 6
print("First two rows:\n", a[0:2])
print("Last column only: ", a[:, 2]) # [3, 6, 9]

print("-" * 30)

# 2. Boolean Indexing
# Select items matching a conditional mask without loops
mask = a > 5
print("Boolean Mask (a > 5):\n", mask)
print("Elements > 5: ", a[mask]) # [6, 7, 8, 9]

# Replace elements matching condition
a[a % 2 == 0] = -1
print("Evens replaced with -1:\n", a)

print("-" * 30)

# 3. Stacking Arrays
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])

# Horizontal Stacking
h_stack = np.hstack((x, y))
print("Horizontal Stack:\n", h_stack)

# Vertical Stacking
v_stack = np.vstack((x, y))
print("Vertical Stack:\n", v_stack)

# NumPy nditer Iteration in Python

import numpy as np

# 1. Basic nditer iteration
a = np.arange(12).reshape(3, 4)
print("Original 3x4 Array:\n", a)

print("\nIterating element-by-element using nditer:")
for x in np.nditer(a):
    print(x, end=" ")
print()

print("-" * 30)

# 2. Controlling Iteration Order
# 'C' order (row-by-row, C-style memory layout)
print("Iterating in C-order:")
for x in np.nditer(a, order="C"):
    print(x, end=" ")
print()

# 'F' order (column-by-column, Fortran-style memory layout)
print("Iterating in Fortran-order:")
for x in np.nditer(a, order="F"):
    print(x, end=" ")
print()

print("-" * 30)

# 3. Modifying Values during Iteration
# Must use the readwrite flag and modify items in-place
print("Modifying array in-place (squaring elements):")
with np.nditer(a, op_flags=["readwrite"]) as it:
    for x in it:
        x[...] = x * x

print("Modified array:\n", a)

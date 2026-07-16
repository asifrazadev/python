# NumPy Basic Array Operations in Python

import numpy as np

# 1. Inspecting Array Properties
a = np.array([[1, 2], [3, 4], [5, 6]], dtype=np.float64)

print(f"Dimensions (ndim): {a.ndim}")
print(f"Data Type (dtype): {a.dtype}")
print(f"Shape (rows, cols): {a.shape}")
print(f"Item Size (bytes): {a.itemsize}")
print(f"Total elements (size): {a.size}")

print("-" * 30)

# 2. Shorthand Initializers
zero_arr = np.zeros((2, 3))
print("Zeros array:\n", zero_arr)

one_arr = np.ones((2, 3))
print("Ones array:\n", one_arr)

range_arr = np.arange(1, 5) # [1, 2, 3, 4]
print("Range array: ", range_arr)

line_arr = np.linspace(1, 5, 10) # 10 linearly spaced values between 1 and 5
print("Linspace array:\n", line_arr)

print("-" * 30)

# 3. Reshaping Arrays
# Flatten or change shapes (must have compatible sizes!)
b = a.reshape(2, 3)
print("Reshaped from (3,2) to (2,3):\n", b)

# Flattening
print("Flattened array:\n", a.ravel())

print("-" * 30)

# 4. Mathematical Operations & Axes
# axis=0 represents columns, axis=1 represents rows
print("Min: ", a.min())
print("Max: ", a.max())
print("Sum: ", a.sum())

print("Sum along columns (axis=0): ", a.sum(axis=0))
print("Sum along rows (axis=1): ", a.sum(axis=1))
print("Square root of elements:\n", np.sqrt(a))
print("Standard Deviation: ", np.std(a))

# NumPy Introduction in Python
# NumPy Array vs Python List (Memory & Speed)

import sys
import time
import numpy as np

# 1. Memory Comparison
list_items = range(1000)
# A Python list contains pointers to objects (adds high overhead)
print(f"Size of one element in Python list: {sys.getsizeof(5)} bytes")
print(f"Total size of Python list of 1000 items: {sys.getsizeof(5) * len(list_items)} bytes")

arr_items = np.arange(1000)
# A NumPy array stores contiguous raw values directly in memory
print(f"Size of one element in NumPy array: {arr_items.itemsize} bytes")
print(f"Total size of NumPy array of 1000 items: {arr_items.size * arr_items.itemsize} bytes")

print("-" * 30)

# 2. Speed Comparison
SIZE = 1000000

# Using Python Lists
L1 = range(SIZE)
L2 = range(SIZE)

start = time.time()
result_list = [(x + y) for x, y in zip(L1, L2)]
print(f"Python list addition took: {(time.time() - start) * 1000:.2f} ms")

# Using NumPy Arrays
A1 = np.arange(SIZE)
A2 = np.arange(SIZE)

start = time.time()
result_arr = A1 + A2  # vectorized addition!
print(f"NumPy array addition took: {(time.time() - start) * 1000:.2f} ms")

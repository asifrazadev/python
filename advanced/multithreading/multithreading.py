# Multithreading in Python

import time
import threading

# Task 1: Calculate square of numbers
def calc_square(numbers):
    print("Calculate square of numbers")
    for n in numbers:
        time.sleep(0.2)  # simulate I/O delay (e.g. web request, database lookup)
        print(f"square: {n*n}")

# Task 2: Calculate cube of numbers
def calc_cube(numbers):
    print("Calculate cube of numbers")
    for n in numbers:
        time.sleep(0.2)  # simulate I/O delay
        print(f"cube: {n*n*n}")

numbers = [2, 3, 8, 9]

t = time.time()

# 1. Create thread objects
t1 = threading.Thread(target=calc_square, args=(numbers,))
t2 = threading.Thread(target=calc_cube, args=(numbers,))

# 2. Start threads
t1.start()
t2.start()

# 3. Wait for both threads to finish before printing completion
t1.join()
t2.join()

print(f"Done in: {time.time() - t:.4f} seconds")
print("Hooray! Both tasks ran concurrently.")

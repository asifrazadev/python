# Multiprocessing Introduction in Python

import time
import multiprocessing

# CPU Bound task
def calc_square(numbers):
    for n in numbers:
        time.sleep(0.1)  # simulate computing delay
        print(f"square: {n*n}")

def calc_cube(numbers):
    for n in numbers:
        time.sleep(0.1)
        print(f"cube: {n*n*n}")

if __name__ == "__main__":
    numbers = [2, 3, 5, 8]

    start_time = time.time()

    # 1. Create processes
    p1 = multiprocessing.Process(target=calc_square, args=(numbers,))
    p2 = multiprocessing.Process(target=calc_cube, args=(numbers,))

    # 2. Start processes (running on separate CPU cores!)
    p1.start()
    p2.start()

    # 3. Wait for processes to finish
    p1.join()
    p2.join()

    print(f"Done in: {time.time() - start_time:.4f} seconds")
    print("Processes complete.")

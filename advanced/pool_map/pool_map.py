# Multiprocessing Pool (Map) in Python

import time
import multiprocessing

def f(n):
    # Simulate some heavy math calculations
    sum_val = 0
    for i in range(1, 10000):
        sum_val += i * i
    return sum_val

if __name__ == "__main__":
    t1 = time.time()
    
    # 1. Create a Multiprocessing Pool
    # By default, it creates processes equal to the number of CPU cores on your machine.
    p = multiprocessing.Pool()

    # 2. Distribute work across processes using pool.map()
    # It splits the input list into chunks and submits them to workers.
    # It preserves the order of input.
    result = p.map(f, range(1000))
    p.close()
    p.join()

    print(f"Pool took: {time.time() - t1:.4f} seconds")
    print(f"First few results: {result[:5]}")

# Multiprocessing Lock in Python

import time
import multiprocessing

# Critical Section function (modifies shared data)
def deposit(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        # Acquire the lock to prevent other processes from accessing this block
        lock.acquire()
        balance.value = balance.value + 1
        # Always release the lock
        lock.release()

def withdraw(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        # Alternative: use lock as a context manager (auto-releases!)
        with lock:
            balance.value = balance.value - 1

if __name__ == "__main__":
    # Shared variable starting at $100
    balance = multiprocessing.Value("i", 100)
    
    # Create the Lock
    lock = multiprocessing.Lock()

    # Create processes
    p1 = multiprocessing.Process(target=deposit, args=(balance, lock))
    p2 = multiprocessing.Process(target=withdraw, args=(balance, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    # Expected value is 100 because we deposited 100 and withdrew 100.
    # Without locks, this value is highly unpredictable due to race conditions!
    print(f"Final balance: {balance.value}")

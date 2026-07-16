# Sharing Data between Processes using Value and Array in Python

import multiprocessing

def calc_square(numbers, result, value):
    # Update shared Value
    value.value = 5.67

    # Update shared Array
    for idx, n in enumerate(numbers):
        result[idx] = n * n

if __name__ == "__main__":
    numbers = [2, 3, 5]

    # Shared Array: 'i' stands for integer, size is 3
    result = multiprocessing.Array("i", 3)
    
    # Shared Value: 'd' stands for double (float)
    v = multiprocessing.Value("d", 0.0)

    # Note: Normal global variables cannot be modified by child processes
    # since each process runs in its own memory space. We must use shared variables.
    p = multiprocessing.Process(target=calc_square, args=(numbers, result, v))

    p.start()
    p.join()

    # Access shared data from main process
    print(f"Shared value after process completion: {v.value}")
    print(f"Shared array elements: {list(result)}")

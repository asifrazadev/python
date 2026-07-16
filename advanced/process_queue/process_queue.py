# Sharing Data using Multiprocessing Queue in Python

import multiprocessing

def calc_square(numbers, q):
    for n in numbers:
        q.put(n * n)  # push items into the queue

if __name__ == "__main__":
    numbers = [2, 3, 5]
    
    # 1. Create a multiprocessing Queue
    # Note: This is different from the standard queue.Queue library class!
    q = multiprocessing.Queue()

    p = multiprocessing.Process(target=calc_square, args=(numbers, q))

    p.start()
    p.join()

    # 2. Extract values from the queue in the parent process
    print("Values popped from shared queue:")
    while not q.empty():
        print(q.get())

'''
For CPU bound taks,
factrial calculations, especially for large numbers,
involves significant amount of CPU processing.
Multiprocessing can be used to distribute the load across multiple cores.
'''

import multiprocessing
import math
import sys
import time

sys.set_int_max_str_digits(1000000)

def compute_factorial(n):
    print(f'Calculating factorial of {n}...')
    result = math.factorial(n)
    return result

if __name__ == "__main__":
    start_time = time.time()
    numbers = [50000, 60000, 70000, 80000, 90000]
    with multiprocessing.Pool() as pool:
        results = pool.map(compute_factorial, numbers)
    end_time = time.time()
    print(results)
    print(f'Time taken: {end_time - start_time} seconds')

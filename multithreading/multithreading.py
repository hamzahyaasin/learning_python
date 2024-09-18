### When to use 
#### I/O-bound program, that spends more time waiting for I/O operations (eg file operations, network requests, etc)
#### concurrent execution: when you want to improve the performance of your program by running multiple threads in parallel


import threading
import time

def print_numbers():
    for i in range(20):
        time.sleep(2)
        print(f"Number: {i}")
        
def print_letters():
    for i in range(65, 85):
        time.sleep(2)
        print(f"Letter: {chr(i)}")


## Creating 2 threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t=time.time()

t1.start()
t2.start()

## Wait for the threads to finish
t1.join()
t2.join()

finished_time = time.time() - t
print(finished_time)
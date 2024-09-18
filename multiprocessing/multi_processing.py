#when to use
## CPU-bound program, that spends more time doing CPU operations (eg. calculations, data processing, etc)
## parallel execution: when you want to run multiple processes in parallel

import multiprocessing
import time

def square_numbers():
    for i in range(25):
        time.sleep(0.2)
        print(f"Square: {i*i}")
        
def cube_numbers():
    for i in range(25):
        time.sleep(0.2)
        print(f"Cube: {i*i*i}")
        
if __name__ == "__main__":
    ## Creating 2 processes
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    t=time.time()

    p1.start()
    p2.start()

    ## Wait for the processes to finish
    p1.join()
    p2.join()

    finished_time = time.time() - t
    print(finished_time)

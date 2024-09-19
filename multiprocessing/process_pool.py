from concurrent.futures import ProcessPoolExecutor
import time

def square(number):
    time.sleep(1)
    return f'Square: {number*number}'


num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if __name__ == '__main__':

    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square, num)
        
    for result in results:
        print(result) 
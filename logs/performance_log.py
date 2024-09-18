import logging
import time
from logging.handlers import RotatingFileHandler
import numpy as np
import matplotlib.pyplot as plt

def mandelbrot_set(width=800, height=800, max_iter=1000, xmin=-2.5, xmax=1.5, ymin=-2.0, ymax=2.0):
    """
    Generates and displays the Mandelbrot set fractal.
    
    Parameters:
    width (int): The width of the output image in pixels.
    height (int): The height of the output image in pixels.
    max_iter (int): The maximum number of iterations for each point.
    xmin, xmax (float): The range of the real axis.
    ymin, ymax (float): The range of the imaginary axis.
    
    Returns:
    None
    """
    # Create a 2D array to hold the result
    mandelbrot_set = np.zeros((height, width))

    # Create a grid of complex numbers
    x, y = np.linspace(xmin, xmax, width), np.linspace(ymin, ymax, height)
    C = x[:, np.newaxis] + 1j * y[np.newaxis, :]

    # Initialize Z as 0
    Z = np.zeros(C.shape, dtype=complex)

    # Create a mask to track points that are still within the set
    mask = np.ones(C.shape, dtype=bool)

    # Mandelbrot calculation
    for i in range(max_iter):
        Z[mask] = Z[mask]**2 + C[mask]
        mask = mask & (np.abs(Z) <= 2)
        mandelbrot_set += mask

    # Plotting the Mandelbrot set using Matplotlib
    plt.imshow(np.log(mandelbrot_set.T), cmap='magma', extent=[xmin, xmax, ymin, ymax])
    plt.colorbar(label='Log of Iteration Count')
    plt.title('Mandelbrot Set')
    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.show()

# Call the function
# mandelbrot_set()


def benchmark_logging_performance():
    logger = logging.getLogger('performance_logger')
    logger.setLevel(logging.DEBUG)
    
    #file handler
    file_handler = logging.FileHandler('performance_file.log')
    file_handler.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    
    start_time = time.time()
    mandelbrot_set()
    # for i in range(100):
    #     logger.debug('This is a debug message')
    end_time = time.time()
    print(f'FileHandler execution time: {end_time - start_time}')
    logger.removeHandler(file_handler)
    
    #console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    logger.addHandler(console_handler)
    
    start_time = time.time()
    mandelbrot_set()
    # for i in range(10000):
    #     logger.debug('This is a debug message')
    end_time = time.time()
    print(f'StreamHandler execution time: {end_time - start_time}')
    logger.removeHandler(console_handler)
    
    #rotating file handler
    rotating_file_handler = RotatingFileHandler('performance_rotating_file.log',maxBytes=1024,backupCount=5)
    rotating_file_handler.setLevel(logging.DEBUG)
    logger.addHandler(rotating_file_handler)
    
    start_time = time.time()
    mandelbrot_set()
    # for i in range(10000):
    #     logger.debug('This is a debug message')
    end_time = time.time()
    print(f'RotatingFileHandler execution time: {end_time - start_time}')
    logger.removeHandler(rotating_file_handler)
    
    
############
#Testing the function
benchmark_logging_performance()
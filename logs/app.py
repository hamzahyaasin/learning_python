import logging

#configure logging settings
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[logging.FileHandler("app1.log"),
                    logging.StreamHandler()])

logger = logging.getLogger("ArithmeticApp")

def add(a, b):
    result = a + b
    logger.debug(f"Adding {a} and {b} = {result}")
    return result

def subtract(a, b):
    result = a - b
    logger.debug(f"Subtracting {a} and {b} = {result}")
    return result

def multiply(a, b): 
    result = a * b
    logger.debug(f"Multiplying {a} and {b} = {result}")
    return result

def divide(a, b):    
    try:
        result = a / b
        logger.debug(f"Dividing {a} and {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero is not allowed")
        return None
    
    
add(1,2)
subtract(1,2)
multiply(10,2)
divide(10,0)
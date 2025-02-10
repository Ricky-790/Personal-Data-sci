import logging

#Settings
logging.basicConfig(level=logging.DEBUG,
    # filename='myapp.log',
    # filemode='w',
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('myapp.log'), # File name
        logging.StreamHandler() #for putting the logs information inside the file
    ] 
    )

logger = logging.getLogger("ArithmeticApp")

def add(a,b):
    result = a+b
    logger.debug(f"Adding {a} and {b}")
    return result

def subtract(a,b):
    result = a-b
    logger.debug(f"Subtracting {a} and {b}")
    return result

def multiply(a,b):
    result = a*b
    logger.debug(f"Multiplying {a} and {b}")
    return result

def divide(a,b):
    try:
        result = a/b
        logger.debug(f"Dividing {a} and {b}")
        return result
    except ZeroDivisionError:
        logger.error("Can not divide by zero")
        return None
    
a = 5
b = 10

print(add(a,b))
print(subtract(a,b))
print(multiply(a,b))
print(divide(a,b))
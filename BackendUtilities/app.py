import logging 

#Logging setting
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S',
    handlers = [
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("ArithmeticApp")

def add(a, b) :
    result = a + b
    logger.debug(f"Adding {a} + {b} gives = {result}")
    return result

def subtract(a, b) :
    result = a - b
    logger.debug(f"Subtracting {a} - {b} gives = {result}")
    return result

def multiply(a, b) :
    result = a + b
    logger.debug(f"Multiplying {a} * {b} gives = {result}")
    return result

def divide(a, b) :
    try :
        result = a / b
        logger.debug(f"Dividing {a} by {b} gives = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None
    
add(10,2)
subtract(15,9)
multiply(8,2)
divide(20,2)
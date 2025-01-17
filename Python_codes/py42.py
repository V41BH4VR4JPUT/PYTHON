# Decorators in python
def addressing(func):
    def inner(*args , **kwargs):
         print("Function".center(80,"*"))
         func(*args , **kwargs)
         print("------------------------------------------------------------------------------------------------")
    return inner
def message():
   print("Greetings, I am optimus prime and I am leader of autobots.")

addressing(message)()   
@addressing
def calculations( a , b ):
    print("Addition : " , a + b)
    print("Subtraction : " , a - b)
    print("Multiplication : " , a * b)
    print("Division : " , a / b)
    print("Floor division : " , a // b)
    print("Modulus : " , a % b)
    print("Exponential : " , a ** b)

calculations(4 , 5)

# Practical Use Case

import logging
logging.basicConfig(level=logging.INFO)

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated


def my_function(a, b):
    return a + b

log_function_call(my_function)(1, 2)

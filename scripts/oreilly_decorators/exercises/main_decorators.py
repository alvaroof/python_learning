from math import sqrt
from decorators import count_calls
from decorators import jsonify
from decorators import groot
from decorators import four
from decorators import record_calls
import json

def call_logger(func):
    """Return a new function that calls func and prints when it was called."""
    def new_func(*args, **kwargs):
        print("Function started")
        result = func(*args, **kwargs)
        print(result)
        print("Function returned")
        return result
    return new_func

def alvaro(func):
    """leave your mark in the function"""
    func.alvaro_was_here = "Definitely True"
    func.__doc__ = """This is the new docstring. Made definitely by Alvaro"""
    return func
    
if __name__ == '__main__':

    # @call_logger
    # def add(x,y):
    #     return x+y

    # add(4,5)

    # @alvaro
    # def add(x, y):
    #     return x+y

    # print(add.__doc__)
    # print(add.alvaro_was_here)
    
    @count_calls
    def quadratic(a, b, c):
        x1 = -b / (2*a)
        x2 = sqrt(b**2 - 4*a*c) / (2*a)
        return (x1 + x2), (x1 - x2)
    print(quadratic.calls)
    print(quadratic(2, 8, 6))
    # (-1.0, -3.0)
    print(quadratic(a=4, b=9, c=2))
    # (-0.25, -2.0)
    print(quadratic.calls)
    # 2
    

    @jsonify
    def get_thing():
        return {'trey': "red", 'diane': "purple"}

    print(get_thing())
    # '{"trey": "red", "diane": "purple"}
    
    @groot
    def greet(name):
        print("Hello {}".format(name))
    
    a = greet("Trey")
    print(a)
    
    @record_calls
    def greet(name="world"):
        """Greet someone by their name."""
        print(f"Hello {name}")
        
    greet("Trey")
    # Hello Trey

    print(greet.call_count)
    # 1
    
    print(greet(name="Trey"))
    # Hello Trey

    print(greet.call_count)
    # 2

    print(greet.calls)
    # [Call(args=('Trey',), kwargs={}), Call(args=(), kwargs={'name': 'Trey'})]
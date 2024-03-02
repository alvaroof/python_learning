"""Function object exercises"""


def call(func, *args, **kwargs):
    """Call the function provided with the given arguments."""
    return func(*args, **kwargs)


def call_later(func, *args, **kwargs):
    """Return a function to call given function with provided arguments."""
    def new_func():
        return func(*args, **kwargs)
    return new_func

def exclude(func, iterable):
    """Only keep items which fail a given predicate test"""
    return [x for x in iterable if not func(x)]

def call_logger(func):
    """Return a new function that calls func and prints when it was called."""
    def new_func(*args, **kwargs):
        print("Function started")
        result = func(*args, **kwargs)
        print("Function returned")
        return result
    return new_func

def call_again(func, *args):
    """Return function return value and a function to call again."""
    def partial_func():
        return func(*args)
    return (func(*args), partial_func)


def only_once(func):
    """Return new version of the function that can only be called once."""
    func.call_count = 0
    def new_func(*args, **kwargs):
        func.call_count += 1
        if func.call_count <= 1:
            return func(*args, **kwargs)
        else:
            raise ValueError("You can't call this function twice!")
    return new_func

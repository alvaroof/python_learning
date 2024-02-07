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

# def call_logger(func):
#     """Return a new function that calls func and prints when it was called."""
#     def new_func():
#         print("Function started")
#         x = func()
#         print("Function returned")
#         return x
#     return new_func


def call_again():
    """Return function return value and a function to call again."""


def only_once():
    """Return new version of the function that can only be called once."""

"""Decorator exercises"""
from functools import wraps
from dataclasses import dataclass
import json

NO_RETURN = object()

def count_calls(func):
    """Record calls to the given function."""
    def decorated_func(*args, **kwargs):
        decorated_func.calls += 1
        return func(*args, **kwargs)
    decorated_func.calls = 0
    return decorated_func

def jsonify(func):
    """Decorate function to JSON-encode return value."""
    @wraps(func)
    def dec_func(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result)
    return dec_func


def groot(func):
    """Return function which prints 'Groot' (ignore decoratee)."""
    @wraps(func)
    def dec_func(*args, **kwargs):
        print("Groot")
    return dec_func

def four(func):
    """Return 4 (ignore decorated function)."""
    return 4

@dataclass
class Call:
    args: tuple
    kwargs: dict

def record_calls(func):
    """Recording number of times a decorated function is called."""
    @wraps(func)
    def dec_func(*args, **kwargs):
        dec_func.call_count += 1
        call = Call(args=args, kwargs=kwargs)
        dec_func.calls.append(call)
        try:
            call.exception = None
            call.return_value = func(*args, **kwargs)
        except Exception as e:
            call.exception = e
            call.return_value = NO_RETURN
            raise
        return call.return_value
    dec_func.call_count = 0
    dec_func.calls = []
    return dec_func

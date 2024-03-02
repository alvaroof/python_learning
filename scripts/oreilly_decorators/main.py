from functools import partial

def custom_map(func, iterable): # same as map built-in function
    return (func(x) for x in iterable)

def custom_filter(func, iterable): # same as built-in filter function
    return [x for x in iterable if func(x)]

def custom_partial(func, *first_args): # same as functools.partial
    """"Let's us preload a function with some arguments"""
    def new_func(*args):
        new_args = first_args + args
        return func(*new_args)
    return new_func

def add_two(x, y):
    return x+y

if __name__ == '__main__':
    l = [-4, -5, 1, 3, 4, 5]
    print(list(custom_filter(lambda x: x > 0, l)))
    partial_sum_four = partial(add_two, 4)
    print(partial_sum_four(5))
    
    count_lengths = partial(map, len)
    word_lengths = count_lengths(["some", "words", "banana"])
    print(list(word_lengths))
    
    
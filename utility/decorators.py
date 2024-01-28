from time import perf_counter

#use @timer_func on the wanted function
def timer_func(func):
    # This function shows the execution time of the function object passed
    def wrapper(*args, **kwargs):
        t1 = perf_counter()
        result = func(*args, **kwargs)
        t2 = perf_counter()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4e}s')
        return result
    return wrapper


#use @memoize on the wanted function
def memoize(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return wrapper

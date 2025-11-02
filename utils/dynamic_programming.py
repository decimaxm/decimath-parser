from inspect import signature

def memoize(my_func):
    '''Decorator: use a cache for storing intermediate results - useful for recursions'''
    # I know that in standard library is there a very useful and comfortable lru_cache... make your own business!

    def make_key(func, *args, **kwargs): # yeah, I took inspiration from CPython. You should too! https://github.com/python/cpython/blob/42336def77f53861284336b3335098a1b9b8cab2/Lib/functools.py
        sig = signature(func) # get the signature of the function 
        mapped_arguments = sig.bind(*args, **kwargs) # match positional and keyword arguments
        key = '_'.join([f'{k}_{v}' for k,v in mapped_arguments.arguments.items()])
        return key

    cache = {}
    def memoized_function(*args, **kwargs):
        key = make_key(my_func, *args, **kwargs)
        if key in cache.keys():
            val = cache[key]
        else:
            val = my_func(*args, **kwargs)
            cache[key] = val
        return val
    
    memoized_function.cache = cache
    
    return memoized_function
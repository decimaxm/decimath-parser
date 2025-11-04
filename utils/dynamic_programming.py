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



#TODO: there is too much duplicated code here. Can't we generalize the function?
def memoize_method(my_instance_method):
    '''Decorator for instance methods: use a cache for storing intermediate results - useful for recursions'''
    # I know that in standard library is there a very useful and comfortable lru_cache... make your own business!

    def make_key(self, my_instance_method, *args, **kwargs): # yeah, I took inspiration from CPython. You should too! https://github.com/python/cpython/blob/42336def77f53861284336b3335098a1b9b8cab2/Lib/functools.py
        sig = signature(my_instance_method) # get the signature of the function 
        mapped_arguments = sig.bind(self, *args, **kwargs) # match positional and keyword arguments
        key = '_'.join([f'{k}_{v}' for k,v in mapped_arguments.arguments.items()])
        return key

    cache_name = f"_memoization_cache_{my_instance_method.__name__}"
    def memoized_function(self, *args, **kwargs):
        # check that cache exists, otherwise creates it as an empty dict
        if not hasattr(self, cache_name):
            setattr(self, cache_name, {})
        cache = getattr(self, cache_name)

        key = make_key(self, my_instance_method, *args, **kwargs)
        if key in cache.keys():
            val = cache[key]
        else:
            val = my_instance_method(self, *args, **kwargs)
            cache[key] = val
        return val
    
    
    return memoized_function
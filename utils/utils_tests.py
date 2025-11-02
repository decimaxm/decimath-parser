from .dynamic_programming import memoize, memoize_method

def memoization_test():
    
    @memoize
    def fibonacci(n): # 1 1 2 3 5 8 
        if n == 0:
            return 0 
        elif n == 1:
            return 1
        else:
            dad = fibonacci(n-1)
            grandpa = fibonacci(n-2)
            return dad + grandpa
    fibonacci(10)
    print(fibonacci.cache)
    fibonacci(11) 
    print(fibonacci.cache)
    

class Dummy:
    def __init__(self):
        self.counter = 0

    @memoize_method
    def compute(self, x, y):
        # simple sum method, count calls
        self.counter += 1
        return x + y

def method_memoization_test():
    d1 = Dummy()
    d2 = Dummy()

    # first call on d1
    res1 = d1.compute(2, 3)
    print("d1 counter after first call:", d1.counter, "cache:", getattr(d1, "_memoization_cache_compute"))

    # second call same arguments on d1 -> should use cache
    res1b = d1.compute(2, 3)
    print("d1 counter after second call:", d1.counter, "cache:", getattr(d1, "_memoization_cache_compute"))

    # third call, different arguments on d1 -> should not use cache
    res1c = d1.compute(2, 8)
    print("d1 counter after second call:", d1.counter, "cache:", getattr(d1, "_memoization_cache_compute"))

    # first call on d2 -> cache should be separate
    res2 = d2.compute(2, 3)
    print("d2 counter after first call:", d2.counter, "cache:", getattr(d2, "_memoization_cache_compute"))

    # simple checks
    assert res1 == 5
    assert res1b == 5
    assert res1c == 10
    assert d1.counter == 2   # second call used cache, third didn't 
    assert d2.counter == 1   # separate cache for d2

    # new argument on d1 -> recalculated
    res3 = d1.compute(3, 4)
    assert res3 == 7
    assert d1.counter == 3


if __name__ == '__main__':
    memoization_test()
    method_memoization_test()
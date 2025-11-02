from .dynamic_programming import memoize

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
    
if __name__ == '__main__':
    memoization_test()
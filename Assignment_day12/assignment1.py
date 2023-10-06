import time
def cached(func):
    cache={}
    def wrapper(*args):
        for arg in args:
         result = cache.get(arg)
        if not result:
            result = func(*args)
            cache.setdefault(arg, result)
            print("new data", result)
        else:
            print('Cached data', cache[arg])
            return result
    return wrapper

def performance_monitor(func):
    def inner(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        time_taken = end - start
        print(f"Time taken to execute: {time_taken} seconds")
        return result
    return inner

@cached
@performance_monitor
def factorial(n):
    fn=1
    for i in range(1,n+1):
        time.sleep(0.5)
        fn *= i
    return fn

r1=factorial(5)
r2=factorial(10)
r3=factorial(5)
import time
import math
def performance_log(fn_target):
    def inner(*args, **kwargs):
        
        start = time.time()
        fn_result = fn_target(*args, **kwargs)
        end = time.time()
        print(f'total time taken is {end-start}sec')
        
        return fn_result
    return inner


def check_prime(num):
    if num < 2:
        return False
    for i in range(2,int(math.sqrt(num)) + 1):
        if(num % i == 0):
            break
        else:
            return True
    else:
        True
    

@performance_log
def find_primes(min,max):
    result = []
    for num in range(min,max):
        if check_prime(num):
            result.append(num)
    return result

x = find_primes(100,1000)
print(len(x))



    



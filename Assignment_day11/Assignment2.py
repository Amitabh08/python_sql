import time
import math

class  timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.time_consumed = self.end - self.start

   
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
    

def find_primes(min,max):
    result = []
    for num in range(min,max):
        if check_prime(num):
            result.append(num)
    return result

                 

with timer() as t:
    f = find_primes(100,100000)
    print(len(f))
print('time taken = ', t.time_consumed)


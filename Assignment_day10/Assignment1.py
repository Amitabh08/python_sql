from math import sqrt

def check_prime(num):
    if(num==1):
        return False
    for i in range(2,int(sqrt(num))+1):
        if(num%i==0):
            return False
    return True

class PrimeIterator:
    def __init__(self, start, end=None):
        if end == None:
            self.i = 1
            self.j = start
        else:
            self.i = start
            self.j = end

    def __iter__(self):
        self.n = self.i -1
        return self

    def __next__(self):
        if self.n <= self.j:
            self.n += 1
            while not check_prime(self.n):
                self.n += 1
                if self.n > self.j:
                        raise StopIteration()
            else:
                return self.n
        else:
            raise StopIteration()

x = iter(PrimeIterator(1000,10000))
for i in x:
    print(i, end = " ")

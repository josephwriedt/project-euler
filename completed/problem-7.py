# 10001st Prime

from typing import List, Dict

def sieve_of_eratosthenes():
    n = 2

    d: List[Dict] = {}

    while True:
        if n not in d:
            yield n
            d[n * n] = [n] 
        else:
            for p in d.get(n):
                d.setdefault(p + n, []).append(p)
                
            del d[n]

        n += 1
        
primes = sieve_of_eratosthenes()

N = 10001

for i in range(N):
    print("ith Prime:", i+1, next(primes))
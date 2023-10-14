# Largest Prime Factor

from typing import List, Dict

def prime_number(n):
    x = 2

    # keys = numbers
    # values = list of prime multiples that are the prime factors of key
    not_prime: Dict[List] = {}

    yield x
    while x * x <= n:
        # if x is prime
        if x not in not_prime:
            # yield prime
            yield x

            not_prime[x * x] = [x]
        else:
            for mult in not_prime[x]:
                not_prime.setdefault(x + mult, []).append(mult)

            del not_prime[x]
        x += 1

    yield False

N = 600851475143

is_divisible = lambda x: N % x == 0

primes = prime_number(N)

while (i := next(primes)):
    if is_divisible(i):
        print('N is divisible by:', i)

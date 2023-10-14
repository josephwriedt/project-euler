# Smallest Multiple

from typing import List, Dict

# reusing code from problem-3.py
def prime_number(n):
    x = 2

    # keys = numbers
    # values = list of prime multiples that are the prime factors of key
    not_prime: Dict[List] = {}

    yield x
    while x <= n:
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

def factor(number, prime) -> int:
    if number % prime == 0:
        return factor(number//prime, prime) + 1
    else:
        return 0

print("Factor", factor(16,2))

prime_factorization: List[Dict] = []
for i in range(20):
    prime_factorization.append({})
primes = prime_number(20)

while (p := next(primes)):
    for i in range(1,21):
        if (f := factor(i, p)):
            # print("Number", i, "Prime", p, "Factor", f)
            prime_factorization[i - 1].update({p:f})

print("Prime Factorization Dict:")
for i in range(len(prime_factorization)):
    print(i + 1, prime_factorization[i])

smallest_multiples = {}
for i in range(len(prime_factorization)):
    number = i + 1
    d: Dict = prime_factorization[i]
    for key in d:
        value = d.get(key)
        if value > smallest_multiples.get(key, 0):
            smallest_multiples[key] = value

print("Smallest Multiple Dict:", smallest_multiples.__str__())

number = 1
for prime in smallest_multiples.keys():
    number = number * prime ** smallest_multiples[prime]

print("Smallest Multiple", number)

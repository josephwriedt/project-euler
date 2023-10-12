# Largest Prime Factor

def prime_number(n):
    x = 2

    not_prime = set()

    yield x
    while x * x <= n:
        # if x is prime
        if x not in not_prime:
            # yield prime
            yield x

            # update the not prime set with multipules of prime (sieve of eratosthenes)
            not_prime.update(range(x, n, x))

        x += 1

    yield False

N = 600851475143

is_divisible = lambda x: N % x == 0

primes = prime_number(N)

while (i := next(primes)):
    if is_divisible(i):
        print('N is divisible by:', i)

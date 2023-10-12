# Even Fibonacci Numbers

# generator
def fibonacci(n):
    x, y = 1, 2

    while x < n:
        yield x
        x, y = y, x + y
    else:
        yield False

N = 4000000

f = fibonacci(N)

sum = 0
# walrus operator: := (assigns)
while (x := next(f)) != False:
    if x % 2 == 0:
        sum += x

print("Sum:", sum)
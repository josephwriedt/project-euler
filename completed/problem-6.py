# Sum Square Difference

# Noticing that for (a + b + c + ...)^2 - (a^2 + b^2 + c^2 + ...) = 2a(b + c + ...) + 2b(c + d + ...) + ...


def sum_square_diff(n: int) -> int:
    final = 0
    for a in reversed(range(1, n + 1)):
        final += 2 * a * sum(range(1, a))

    return final

N = 100

print("Final", sum_square_diff(N))
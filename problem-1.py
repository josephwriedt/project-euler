# Multiples of 3 or 5

from typing import List

def find_multiples_below(n: int, multiple: int) -> List[int]:
    a = (n-1)//multiple
    print("Division", a)
    return list(map(lambda x: x * multiple, range(1,a + 1)))

N = 1000

three_multiples: List[int] = find_multiples_below(N, 3)

five_multiples: List[int] = find_multiples_below(N, 5)


multiple_set = set(three_multiples + five_multiples)
print("Multiple Set:", multiple_set)
sum = sum(multiple_set)

# sum = sum(three_multiples) + sum(five_multiples)
print("Sum:", sum)
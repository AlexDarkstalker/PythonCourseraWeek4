import math


def MinDivisor(n):
    i = 2
    while i <= math.sqrt(n):
        if not n % i:
            return i
        i += 1
    return n

n = int(input())
print(MinDivisor(n))

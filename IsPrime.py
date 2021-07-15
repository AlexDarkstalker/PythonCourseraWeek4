import math


def isPrime(n):
    i = 2
    while i <= math.sqrt(n):
        if not n % i:
            return "NO"
        i += 1
    return "YES"


n = int(input())
print(isPrime(n))

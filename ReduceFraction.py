def gcd(a, b):
    if not a % b:
        return b
    return gcd(b, a % b)


def reduceFraction(n, m):
    k = gcd(n, m)
    return int(n / k), int(m / k)


a = int(input())
b = int(input())
print(*reduceFraction(a, b))

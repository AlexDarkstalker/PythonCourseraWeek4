def gcd(a, b):
    if not a % b:
        return b
    return gcd(b, a % b)


a = int(input())
b = int(input())
print(gcd(a, b))

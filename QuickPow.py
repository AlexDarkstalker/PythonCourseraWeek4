def pow(a, n):
    if not n:
        return 1
    if not n % 2:
        return pow(a * a, n / 2)
    return a * pow(a, n - 1)


a = float(input())
n = int(input())
print(pow(a, n))

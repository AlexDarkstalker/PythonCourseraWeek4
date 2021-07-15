def sum():
    n = int(input())
    if n:
        return n + sum()
    return 0


print(sum())

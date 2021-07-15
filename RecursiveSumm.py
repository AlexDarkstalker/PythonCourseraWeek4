def sum(a, b):
    if not b:
        return a
    return sum(a + 1, b - 1)


a = int(input())
b = int(input())
print(sum(a, b))

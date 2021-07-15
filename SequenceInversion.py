def inverse():
    n = int(input())
    if n:
        inverse()
        print(n)
    else:
        print(n)


inverse()

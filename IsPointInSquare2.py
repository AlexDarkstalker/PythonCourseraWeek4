def IsPointInSquare(x, y):
    return -1 <= x <= 1 and -1 <= y <= 1 and abs(x) <= 1 - abs(y)

x = float(input())
y = float(input())
if IsPointInSquare(x, y):
    print("YES")
else:
    print("NO")

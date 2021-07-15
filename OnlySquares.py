import math


def squareInverse(print0):
    n = int(input())
    if n != 0:
        if n > 0:
            if not math.sqrt(n) % 1:
                squareInverse(False)
            else:
                if not print0:
                    squareInverse(False)
                else:
                    squareInverse(True)
            if not math.sqrt(n) % 1:
                print(n, end=" ")
        else:
            if not print0:
                squareInverse(False)
            else:
                squareInverse(True)
    elif n == 0 and print0:
        print(n, end=" ")


squareInverse(True)

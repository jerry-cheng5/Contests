import sys

N = int(sys.stdin.readline())
for i in range(N):
    n = int(sys.stdin.readline())

    if n < 34:
        temp = 1
        for j in range(1, n + 1):
            temp *= int(j)
        print(temp % 2**32)
    else:
        print('0')
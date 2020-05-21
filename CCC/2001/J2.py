import sys

x = int(sys.stdin.readline())
m = int(sys.stdin.readline())
n = 'No such integer exists.'

for i in range(m):
    if x * i % m == 1:
        n = i
        break
print(n)
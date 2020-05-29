'''
DMOJ
CCC 2001 J2 - Mod Inverse
https://dmoj.ca/problem/ccc01j2
Jerry Cheng
'''

import sys

x = int(sys.stdin.readline())
m = int(sys.stdin.readline())
n = 'No such integer exists.'

for i in range(m):
    if x * i % m == 1:
        n = i
        break
print(n)
'''
DMOJ
CCC 2001 J1 - Dressing Up
https://dmoj.ca/problem/ccc01j1
Jerry Cheng
'''

import sys

h = int(sys.stdin.readline())
counter = 1

for i in range(1, h - 1, 2):
    print('*' * i + ' ' * (h * 2 - i * 2) + '*' * i)

print('*' * h * 2)

for i in reversed(range(1, h - 1, 2)):
    print('*' * i + ' ' * (h * 2 - i * 2) + '*' * i)

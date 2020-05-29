'''
DMOJ
CCC 2003 J1 - Trident
https://dmoj.ca/problem/ccc03j1
Jerry Cheng
'''

import sys
input = sys.stdin.readline

t = int(input().strip())
s = int(input().strip())
h = int(input().strip())

if t > 0:
    print(((('*' + ' ' * s) * 2 + '*\n') * t).strip())
print('*' * (s*2 + 3))
if h > 0:
    print(((' ' * (s + 1) + '*\n') * h).rstrip())
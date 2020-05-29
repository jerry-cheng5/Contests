'''
DMOJ
CCC 2004 J2 - Squares
https://dmoj.ca/problem/ccc04j2
Jerry Cheng
'''

import sys
input = sys.stdin.readline

first = int(input().strip())
second = int(input().strip())

for i in range(second - first + 1):
    if i % 4 == 0 and i % 3 == 0 and i % 5 == 0:
        print("All positions change in year", first + i)
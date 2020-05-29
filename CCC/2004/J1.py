'''
DMOJ
CCC 2004 J1 - Squares
https://dmoj.ca/problem/ccc04j1
Jerry Cheng
'''

import sys
import math
input = sys.stdin.readline

print("The largest square has side length %d." % (math.floor(math.sqrt(int(input().strip())))))
'''
HackerRank
Plus Minus
https://www.hackerrank.com/challenges/plus-minus/problem
Jerry Cheng
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    p = n = z = 0
    for num in arr:
        if num > 0:
            p += 1
        elif num < 0:
            n += 1
        else:
            z += 1
    print('%.6f\n%.6f\n%.6f' % (p/len(arr), n/len(arr), z/len(arr)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

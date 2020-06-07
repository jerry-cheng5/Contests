'''
HackerRank
Diagonal Difference
https://www.hackerrank.com/challenges/diagonal-difference/problem
Jerry Cheng
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'diagonalDifference' function below.

def diagonalDifference(arr):
    # Write your code here
    d1 = d2 = 0
    for i in range(len(arr)):
        d1 += arr[i][i]
        d2 += arr[i][len(arr)-1-i]
    return max(d1, d2) - min(d1, d2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

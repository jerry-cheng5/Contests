'''
HackerRank
Breaking the Records
https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
Jerry Cheng
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    maxc = minc = 0
    max = -1
    min = float('inf')
    for score in scores:
        if score > max:
            max = score
            maxc += 1
        if score < min:
            min = score
            minc += 1
    return maxc-1, minc-1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

'''
HackerRank
Between Two Sets
https://www.hackerrank.com/challenges/between-two-sets/problem
Jerry Cheng
'''

#!/bin/python3

import math
import os
import random
import re
import sys

def getTotalX(a, b):
    # Write your code here
    count = 0
    for i in range(max(a), max(b) + 1):
        is_between = True
        for j in a:
            if i%j != 0:
                is_between = False
        for k in b:
            if k%i != 0:
                is_between = False
        if is_between == True:
            count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()

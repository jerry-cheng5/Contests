'''
HackerRank
Sock Merchant
https://www.hackerrank.com/challenges/sock-merchant/problem
Jerry Cheng
'''

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count = {}
    pairs = 0
    for sock in ar:
        if sock not in count.keys():
            count[sock] = 1
        else:
            count[sock] += 1
    for i in list(count.values()):
        pairs += i // 2
    return pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

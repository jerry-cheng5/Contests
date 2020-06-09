'''
HackerRank
Bon Appetit
https://www.hackerrank.com/challenges/bon-appetit/problem
Jerry Cheng
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    if b == int((sum(bill) - bill[k])/2):
        print('Bon Appetit')
    else:
        print(b - int((sum(bill) - bill[k])/2))

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)

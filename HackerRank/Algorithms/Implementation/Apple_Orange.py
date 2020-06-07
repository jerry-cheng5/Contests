'''
HackerRank
Apple and Orange
https://www.hackerrank.com/challenges/apple-and-orange/problem
Jerry Cheng
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    ac = oc = 0
    for apple in apples:
        if a + apple >= s and a + apple <= t:
            ac += 1
    for orange in oranges:
        if b + orange >= s and b + orange <= t:
            oc += 1
    print(ac)
    print(oc)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)

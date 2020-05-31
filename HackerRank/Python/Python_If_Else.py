'''
HackerRank
Python If-Else
https://www.hackerrank.com/challenges/py-if-else/problem
Jerry Cheng
'''

import sys

n = int(input().strip())
if n % 2 != 0:
    print("Weird")
elif n <= 5 or n > 20:
    print("Not Weird")
else:
    print("Weird")
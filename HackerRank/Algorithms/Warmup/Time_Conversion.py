'''
HackerRank
Time Conversion
https://www.hackerrank.com/challenges/time-conversion/problem
Jerry Cheng
'''

#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    if 'PM' in s:
        if s[:2] == '12':
            return(s[:8])
        return(str(int(s[:2]) + 12) + s[2:8])
    else:
        if s[:2] == '12':
            return('00' + s[2:8])
        return(s[:8])

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

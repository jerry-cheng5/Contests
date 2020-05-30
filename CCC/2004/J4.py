'''
DMOJ
CCC 2004 J4 - Simple Encryption
https://dmoj.ca/problem/ccc04j4
Jerry Cheng
'''

import sys
import re
import math
input = sys.stdin.readline

regex = re.compile('[^a-zA-Z]')
shift = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13,
         'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25}

def get_shift(key, letter):
    n = ''
    if shift[letter] + shift[key] > 25:
        return list(shift.keys())[list(shift.values()).index(shift[letter] + shift[key] - 26)]
    else:
        return list(shift.keys())[list(shift.values()).index(shift[letter] + shift[key])]


key = str(input().strip())
phrase = regex.sub('', str(input().strip()))

chart = [[] for _ in range(math.ceil(len(phrase)/len(key)))]

j = 0
for i in range(len(phrase)):
    chart[j//len(key)].append(phrase[i])
    j = j+1

for i in range(len(chart)):
    for j in range(len(chart[i])):
        chart[i][j] = get_shift(key[j], chart[i][j])

for i in chart:
    for j in i:
        print(j, end='')


'''
DMOJ
CCC 2000 J2 - 9966
https://dmoj.ca/problem/ccc00j2
Jerry Cheng
'''

import sys

m = sys.stdin.readline()
n = sys.stdin.readline()
count = 0

for i in range(int(m), int(n)+1):
    number = str(i)
    mirrored = ""

    for j in reversed(range(len(number))):
        if number[j] == '6':
            mirrored += '9'
        elif number[j] == '9':
            mirrored += '6'
        elif number[j] == '0' or number[j] == '1' or number[j] == '8':
            mirrored += number[j]
        else:
            mirrored += '_'

    if number == mirrored:
        count += 1

print(count)

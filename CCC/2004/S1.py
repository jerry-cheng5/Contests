'''
DMOJ
CCC 2004 S1 - Fix
https://dmoj.ca/problem/ccc04s1
Jerry Cheng
'''

import sys
input = sys.stdin.readline

N = int(input().strip())
words = []

for i in range(N):
    words.append([])
    for j in range(3):
        words[i].append(str(input().strip()))
    words[i].sort(key=len)

for i in range(N):
    fixfree = True
    for j in range(3):
        fix = words[i][j]
        if words[i][j+1 if j+1 < 2 else j+1-3][:len(fix)] == fix:
            fixfree = False
        if words[i][j+1 if j+2 < 2 else j+2-3][:len(fix)] == fix:
            fixfree = False
        if words[i][j+1 if j+1 < 2 else j+1-3][-len(fix):] == fix:
            fixfree = False
        if words[i][j+1 if j+2 < 2 else j+2-3][-len(fix):] == fix:
            fixfree = False

    if fixfree:
        print("Yes")
    else:
        print("No")
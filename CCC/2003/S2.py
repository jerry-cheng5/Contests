'''
DMOJ
CCC 2003 S2 - Poetry
https://dmoj.ca/problem/ccc03s2
Jerry Cheng
'''

import sys
input = sys.stdin.readline

vowels = ('a', 'e', 'i', 'o', 'u')

for i in range(int(input().strip())):
    last_syl = []
    for j in range(4):
        current_line = str(input().strip()).lower()
        for k in reversed(range(len(current_line))):
            if all(l not in vowels for l in current_line):
                last_syl.append(current_line.strip())
                break
            elif current_line[k] in vowels:
                last_syl.append(current_line[k:])
                break
            elif current_line[k] == ' ':
                last_syl.append(current_line[k:].strip())
                break
    if last_syl[0] == last_syl[1] and last_syl[1] == last_syl[2] and last_syl[2] == last_syl[3]:
        print('perfect')
    elif last_syl[0] == last_syl[1] and last_syl[2] == last_syl[3]:
        print('even')
    elif last_syl[0] == last_syl[2] and last_syl[1] == last_syl[3]:
        print('cross')
    elif last_syl[0] == last_syl[3] and last_syl[1] == last_syl[2]:
        print('shell')
    else:
        print('free')

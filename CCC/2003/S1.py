'''
DMOJ
CCC 2003 S1 - Snakes and Ladders
https://dmoj.ca/problem/ccc03s1
Jerry Cheng
'''

import sys
input = sys.stdin.readline

move = 999
pos = 1
snakes = {54 : 19, 90 : 48, 99 : 77}
ladders = {9 : 34, 40 : 64, 67 : 86}

while pos < 100 and move != 0:
    move = int(input().strip())
    if move == 0:
        print('You Quit!')
        break
    elif pos + move == 100:
        print('You are now on square 100\nYou Win!')
        break
    elif pos + move > 100:
        print('You are now on square', pos)
    elif pos + move in snakes.keys():
        pos = snakes[pos + move]
        print('You are now on square', pos)
    elif pos + move in ladders.keys():
        pos = ladders[pos + move]
        print('You are now on square', pos)
    else:
        pos += move
        print('You are now on square', pos)
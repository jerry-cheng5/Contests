'''
DMOJ
CCC 2002 S3 - Blindfold
https://dmoj.ca/problem/ccc02s3
Jerry Cheng
'''

import sys
input = sys.stdin.readline

r = int(input().strip())
c = int(input().strip())
backyard = [list(input().strip()) for _ in range(r)]
moves = [input().strip() for _ in range(int(input().strip()))]
directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

for i in range(r):
    for j in range(c):
        for start_d in directions:
            d = start_d
            x = 0
            y = 0
            finished_moves = True
            for move in moves:
                if move == 'F':
                    if i+y+d[0] >= r or i+y+d[0] < 0 or j+x+d[1] >= c or j+x+d[1] < 0:
                        finished_moves = False
                        break
                    elif backyard[i][j] == 'X' or backyard[i+y+d[0]][j+x+d[1]] == 'X':
                        finished_moves = False
                        break
                    else:
                        x += d[1]
                        y += d[0]
                elif move == 'L':
                    if directions.index(d) == 0:
                        d = directions[3]
                    else:
                        d = directions[directions.index(d) - 1]
                elif move == 'R':
                    if directions.index(d) == 3:
                        d = directions[0]
                    else:
                        d = directions[directions.index(d) + 1]
            if finished_moves:
                backyard[i+y][j+x] = '*'

print('\n'.join(map(''.join, backyard)))

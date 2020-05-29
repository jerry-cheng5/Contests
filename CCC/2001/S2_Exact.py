'''
DMOJ
CCC 2001 S2 - Spirals (Exact Version)
https://dmoj.ca/problem/ccc01s2exact
Jerry Cheng
'''

import sys
import math
input = sys.stdin.readline

num_spirals = int(input().strip())

spiral_ranges = [input().strip().split() for _ in range(num_spirals)]

for n in range(num_spirals):
    x = int(spiral_ranges[n][0])
    y = int(spiral_ranges[n][1])

    rows = math.ceil(math.sqrt(y - x + 1))
    cols = round(math.sqrt(y - x + 1))
    
    spiral = [[0 for _ in range(cols)] for _ in range(rows)]
    
    row = (rows - 1) // 2
    col = (cols - 1) // 2
    
    spiral[row][col] = x
    counter = 0
    direction = 0
    
    while x < y:
        if direction == 0:
            for j in range(counter):
                x += 1
                row -= 1
                spiral[row][col] = x
                if x == y:
                    break
        elif direction == 1:
            for j in range(counter):
                x += 1
                col -= 1
                spiral[row][col] = x
                if x == y:
                    break
            counter += 1
        elif direction == 2:
            for j in range(counter):
                x += 1
                row += 1
                spiral[row][col] = x
                if x == y:
                    break
        elif direction == 3:
            for j in range(counter):
                x += 1
                col += 1
                spiral[row][col] = x
                if x == y:
                    break
            counter += 1
        direction = (direction + 1) % 4

    one_char = [True for _ in range(cols)]
    for i in range(cols):
        for j in range(rows):
            if len(str(spiral[j][i])) > 1:
                one_char[i] = False

    for i in range(rows):
        for j in range(cols):
            if spiral[i][j] == 0 and one_char[j] is False:
                spiral[i][j] = '  '
            elif spiral[i][j] == 0 and one_char[j] is True:
                spiral[i][j] = ' '
            elif len(str(spiral[i][j])) < 2 and one_char[j] is False:
                spiral[i][j] = ' ' + str(spiral[i][j])

            if j == cols - 1:
                print(spiral[i][j])
            else:
                print(spiral[i][j], end=' ')

    if n != num_spirals - 1:
        print('')
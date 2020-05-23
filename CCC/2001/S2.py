import sys
import math
input = sys.stdin.readline

x = int(input().strip())
y = int(input().strip())

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

for i in range(rows):
    for j in range(cols):
        if spiral[i][j] == 0:
            spiral[i][j] = '  '
        elif len(str(spiral[i][j])) < 2:
            spiral[i][j] = ' ' + str(spiral[i][j])
        if j == cols - 1:
            print(spiral[i][j])
        else:
            print(spiral[i][j], end=' ')

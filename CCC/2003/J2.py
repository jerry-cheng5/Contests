import sys
import math
input = sys.stdin.readline

while True:
    photos = int(input().strip())
    if photos == 0:
        break
    for i in reversed(range(math.floor(math.sqrt(photos)) + 1)):
        for j in range(math.ceil(math.sqrt(photos)), photos + 1):
            if i * j == photos:
                print('Minimum perimeter is %d with dimensions %d x %d' % (i*2 + j*2, i, j))
                photos = 0
                break
        if photos == 0:
            break

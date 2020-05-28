import sys
input = sys.stdin.readline

target = int(input().strip())
n = int(input().strip())
clubs = [int(input().strip()) for _ in range(n)]

strokes = [float('inf')] * (target + 1) #index is distance, while storing minmum number of strokes
strokes[0] = 0

for d in range(target + 1):
    for club in clubs:
        if d - club >= 0:
            strokes[d] = min(strokes[d], strokes[d - club] + 1)

if strokes[target] == float('inf'):
    print("Roberta acknowledges defeat.")
else:
    print("Roberta wins in %d strokes." % (strokes[target]))
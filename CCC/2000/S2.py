import sys

n = int(sys.stdin.readline())
streams = []
action = 0
stream = 0
percent_flow = 0

for i in range(n):
    streams.append(int(sys.stdin.readline()))

while action != 77:
    action = int(sys.stdin.readline())

    if action == 99:
        stream = int(sys.stdin.readline()) - 1
        percent_flow = int(sys.stdin.readline()) / 100

        streams.insert(stream + 1, streams[stream] * (1 - percent_flow))
        streams[stream] *= percent_flow

    elif action == 88:
        stream = int(sys.stdin.readline()) - 1
        streams[stream] += streams[stream + 1]
        streams.pop(stream + 1)

print(' '.join(map(str, map(int, streams))))

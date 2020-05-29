'''
DMOJ
CCC 2003 S3 - Floor Plan
https://dmoj.ca/problem/ccc03s3
Jerry Cheng
'''

import sys
input = sys.stdin.readline

class Graph:
    def __init__(self, diagram, r, c):
        self.nodes = diagram
        self.r = r
        self.c = c

    def find_rooms(self):
        count = []
        for j in range(len(self.nodes)):
            for i in range(len(self.nodes[j])):
                if self.nodes[j][i] != "I":
                    count.append(self.bfs(j, i, 0))
        return count

    def bfs(self, j, i, count):
        if j < r and j >= 0 and i < c and i >= 0:
            if self.nodes[j][i] == "I":
                return count
            else:
                self.nodes[j] = self.nodes[j][:i] + 'I' + self.nodes[j][i+1:]
                count += 1
                count = self.bfs(j + 1, i , count)
                count = self.bfs(j, i - 1, count)
                count = self.bfs(j, i + 1, count)
                count = self.bfs(j - 1, i, count)
                return count
        else:
            return count


flooring = int(input().strip())
r = int(input().strip())
c = int(input().strip())

diagram = [str(input().strip()) for _ in range(r)]

house = Graph(diagram, r, c)
count = house.find_rooms()
count.sort(reverse=True)
rooms = 0

for c in count:
    if flooring - c >= 0:
        flooring -= c
        rooms += 1
    else:
        break
if rooms == 1:
    print('1 room, %d square metre(s) left over' % (flooring))
else:
    print('%d rooms, %d square metre(s) left over' % (rooms, flooring))

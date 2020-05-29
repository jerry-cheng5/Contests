'''
DMOJ
CCC 2001 S3 - Strategic Bombing
https://dmoj.ca/problem/ccc01s3
Jerry Cheng
'''

import sys
input = sys.stdin.readline

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, first_node, second_node):
        if first_node in self.edges:
            self.edges[first_node].append(second_node)
        else:
            self.edges[first_node] = [second_node]
        if second_node in self.edges:
            self.edges[second_node].append(first_node)
        else:
            self.edges[second_node] = [first_node]

    def find_all_paths(self, start, end, path=[]): #BFS
        path = path + [start]
        if start == end:
            return [path]
        paths = []
        for node in self.edges[start]:
            if node not in path:
                newpaths = self.find_all_paths(node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    def find_dependant_edge(self):
        paths = roads.find_all_paths('A', 'B')
        longest_path = max(paths, key=len)
        dependant_edges = []

        for i in range(len(longest_path)-1):
            edge = longest_path[i:i+2]
            dependant = True
            for path in paths:
                if edge not in [path[i:i+2] for i in range(len(path) - 1)]:
                    dependant = False
            if dependant:
                dependant_edges.append(edge)
        return dependant_edges

roads = Graph()
while True:
    p = str(input().strip())
    if p == '**':
        break
    roads.add_edge(p[0], p[1])

paths = roads.find_all_paths('A', 'B')
dependant_roads = roads.find_dependant_edge()

for road in dependant_roads:
    print(road[0] + road[1])
print("There are %d disconnecting roads." % (len(dependant_roads)))

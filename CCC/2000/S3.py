import sys
import re
input = sys.stdin.readline
link_format = re.compile("<A HREF=\"([^\"]*)\">")

class Graph:

    def __init__(self, n):
        self.num_nodes = n
        self.num_edges = 0
        self.edges = {}

    def add_edge(self, start_node, end_node):
        if start_node in self.edges:
            self.edges[start_node].append(end_node)
        else:
            self.edges[start_node] = [end_node]

    def adj(self, node):
        if node not in self.edges:
            return []
        return self.edges[node]

    def dfs(self, node, visited):
        if node not in visited:
            visited.append(node)
            for n in self.adj(node):
                self.dfs(n, visited)
        return visited

n = int(input().strip())
links_g = Graph(n)

for i in range(n):
    cur_page = str(input().strip())
    while True:
        cur_line = str(input().strip())
        if '</HTML>' in cur_line:
            break
        links = re.findall(link_format, cur_line)

        for l in links:
            print("Link from %s to %s" % (cur_page, l))
            links_g.add_edge(cur_page, l)

while True:
    start_node = str(input().strip())
    if start_node == "The End":
        break
    end_node = str(input().strip())

    surf = False
    for i in links_g.dfs(start_node, []):
        if i == end_node:
            surf = True
            print("Can surf from %s to %s." % (start_node, end_node))
    if surf is False:
        print("Can't surf from %s to %s." % (start_node, end_node))

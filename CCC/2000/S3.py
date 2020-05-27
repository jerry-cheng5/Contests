import sys
import re
input = sys.stdin.readline
link_format = re.compile("<A HREF=\"([^\"]*)\">")

class Graph:
    __vertices = []
    __edges = []

    def add_vertex(self, vertex):
        if vertex not in self.__vertices:
            self.__vertices.append(vertex)

    def add_edge(self, start_node, end_node):
        if [self.__vertices.index(start_node), self.__vertices.index(end_node)] not in self.__edges:
            self.__edges.append([self.__vertices.index(start_node), self.__vertices.index(end_node)])

    def print_edges(self):
        for edge in self.__edges:
            print("Link from %s to %s" % (self.__vertices[edge[0]], self.__vertices[edge[1]]))

    def get_adj(self, node):
        adj = []
        for edge in self.__edges:
            if node == edge[0]:
                adj.append(edge[1])
        return adj

    def dfs(self, node, visited):
        if node not in visited:
            visited.append(node)
            for n in self.get_adj(node):
                self.dfs(n, visited)
        return visited

    def get_surf(self, start, end, visited):
        v = self.dfs(self.__vertices.index(start), visited)
        print(v)
        for i in v:
            if i == self.__vertices.index(end):
                print("Can surf from %s to %s." % (start, end))
            else:
                print("Can't surf from %s to %s." % (start, end))

    def print_graph(self):
        print('Vertices:', self.__vertices)
        print('Edges:', self.__edges)


links_g = Graph()
pages = int(input().strip())
for i in range(pages):
    current_page = str(input().strip())
    current_line = str(input().strip())
    links = []
    links_g.add_vertex(current_page)
    while "</HTML>" not in current_line:
        links = re.findall(link_format, current_line)
        current_line = str(input().strip())
        for l in links:
            links_g.add_vertex(l)
            links_g.add_edge(current_page, l)

links_g.print_edges()
links_g.print_graph()

while True:
    start_node = str(input().strip())
    if start_node == "The End": break
    end_node = str(input().strip())
    links_g.get_surf(start_node, end_node, [])





'''
3
http://ccc.uwaterloo.ca
<HTML> <TITLE>This is the CCC page</TITLE>
Hello there boys
and girls.  <B>Let's</B> try <A HREF="http://abc.def/ghi"> a
little
problem </A>
</HTML>
http://abc.def/ghi
<HTML> Now is the <TITLE>time</TITLE> for all good people to program.
<A HREF="http://www.www.www.com">hello</A><A HREF="http://xxx">bye</A>
</HTML>
http://www.www.www.com
<HTML>
<TITLE>Weird and Wonderful World</TITLE>
</HTML>
http://ccc.uwaterloo.ca
http://www.www.www.com
http://www.www.www.com
http://ccc.uwaterloo.ca
The End
'''
'''
DMOJ
CCC 2004 J3 - Smiles with Similes
https://dmoj.ca/problem/ccc04j3
Jerry Cheng
'''

import sys
input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())
adjs = []
nouns = []

for i in range(n):
    adjs.append(str(input().strip()))
for i in range(m):
    nouns.append(str(input().strip()))

for adj in adjs:
    for noun in nouns:
        print(adj, 'as', noun)

'''
HackerRank
Sparse Arrays
https://www.hackerrank.com/challenges/sparse-arrays/problem
Jerry Cheng
'''

s = int(input().strip())
strings = [input().strip() for _ in range(s)]
q = int(input().strip())
queries = [input().strip() for _ in range(q)]

for query in queries:
    count = 0
    for string in strings:
        if string == query:
            count += 1
    print(count)
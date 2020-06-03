'''
HackerRank
Dynamic Array
https://www.hackerrank.com/challenges/dynamic-array/problem
Jerry Cheng
'''

n, q = input().strip().split()
seq_list = [[] for _ in range(int(n))]
last_answer = 0

for i in range(int(q)):
    query, x, y = input().strip().split()
    index = (int(x) ^ int(last_answer)) % int(n)
    if query == '1':
        seq_list[index].append(y)
    elif query == '2':
        last_answer = seq_list[index][int(y)%int(len(seq_list[index]))]
        print(last_answer)
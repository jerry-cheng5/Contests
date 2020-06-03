'''
HackerRank
Array Manipulation
https://www.hackerrank.com/challenges/crush/problem
Jerry Cheng
'''

n, m = input().strip().split()

arr = [0 for _ in range(int(n))]
max = 0
x = 0

for i in range(int(m)):
    a, b, k = input().strip().split()
    a, b, k = int(a), int(b), int(k)
    arr[a-1] += k
    if b < len(arr):
        arr[b] -= k
for i in range(int(n)):
    x += arr[i]
    if x > max:
        max = x
print(max)
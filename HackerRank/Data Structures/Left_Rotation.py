'''
HackerRank
Left Rotation
https://www.hackerrank.com/challenges/array-left-rotation/problem
Jerry Cheng
'''

n, d = input().strip().split()

arr = input().strip().split()

arr = arr[int(d)%int(n):] + arr[:int(d)%int(n)]
print(' '.join(arr))
'''
HackerRank
2D Arrays - DS
https://www.hackerrank.com/challenges/2d-array/problem
Jerry Cheng
'''

arr = [input().strip().split() for _ in range(6)]
arr = [[int(i) for i in arr[j]] for j in range(len(arr))]

sum = float('-inf')
for i in range(4):
    for j in range(4):
        if arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + \
                arr[i + 2][j + 2] > sum:
            sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + \
                  arr[i + 2][j + 2]

print(sum)
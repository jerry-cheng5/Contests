import sys

quarters = int(sys.stdin.readline())
first = int(sys.stdin.readline())
second = int(sys.stdin.readline())
third = int(sys.stdin.readline())

machine = [[first, second, third], [35, 100, 10], [30, 60, 9]]
plays = 0

while quarters > 0:
    for i in range(3):
        quarters -= 1
        machine[0][i] += 1
        plays += 1
        if machine[0][i] == machine[1][i]:
            machine[0][i] = 0
            quarters += machine[2][i]
        if quarters == 0:
            break

print('Martha plays', plays, 'times before going broke.')
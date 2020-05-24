import sys
input = sys.stdin.readline

temp = [int(input().strip()) for i in range(4)]
target = int(input().strip())
num_tickets = []
combos = 0

for i in range(target // temp[0] + 1):
    for j in range(target // temp[1] + 1):
        for k in range(target // temp[2] + 1):
            for l in range(target // temp[3] + 1):
                if i*temp[0] + j*temp[1] + k*temp[2] + l*temp[3] == target:
                    print('# of PINK is %d # of GREEN is %d # of RED is %d # of ORANGE is %d' % (i, j, k, l))
                    combos += 1
                    num_tickets.append(i + j + k + l)

print('''Total combinations is %d.
Minimum number of tickets to print is %d.''' % (combos, min(num_tickets)))


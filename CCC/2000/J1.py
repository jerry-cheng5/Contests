import sys

month_params = sys.stdin.readline()
start_day = int(month_params[0]) - 1
if start_day < 0:
    start_day = 0
num_days = month_params[2:]
end = False

month = []
for i in range(0, start_day):
    month.append('   ')

for i in range(0, int(num_days)):
    if i + 1 < 10:
        month.append('  ' + str(i+1))
    else:
        month.append(' ' + str(i+1))

print('Sun Mon Tue Wed Thr Fri Sat')
for i in range(0, int(num_days)+start_day):
    if i != 0 and (i + 1) % 7 == 0:
        print(month[i])
    elif i + 1 == int(num_days)+start_day:
        print(month[i], end='')
    else:
        print(month[i], end=' ')

if month[-1] != 28 and start_day != 0:
    print()
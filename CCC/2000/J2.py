import sys

m = sys.stdin.readline()
n = sys.stdin.readline()
ones_eights = False
nine_and_six = False
one_eight_zero = False
count = 0

for i in range(int(m), int(n) + 1):
    temp = str(i)
    sum = 0
    for j in range(0, len(temp)):
        sum += int(temp[j])
    if sum % 8 == 0 or sum / len(temp) == 1:
        count += 1
        continue
    for j in range(0, len(temp)):
        if temp[j] != 9 and temp[j] != 6:
            break
    if


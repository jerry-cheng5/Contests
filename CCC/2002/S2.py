import sys
input = sys.stdin.readline

num = int(input().strip())
den = int(input().strip())

if num == 0:
    print(0)
elif num == den:
    print(1)
elif num > den:
    print(num // den, end=' ')
    for i in reversed(range(1, num % den + 1)):
        if (num % den) % i == 0 and den % i == 0:
            print('%d/%d' % ((num % den)/i, den/i))
            break
elif num < den:
    for i in reversed(range(1, num % den + 1)):
        if (num % den) % i == 0 and den % i == 0:
            print('%d/%d' % ((num % den)/i, den/i))
            break
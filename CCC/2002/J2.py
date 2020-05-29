'''
DMOJ
CCC 2002 J2 - AmeriCanadian
https://dmoj.ca/problem/ccc02j2
Jerry Cheng
'''

import sys
input = sys.stdin.readline

word = ''
can_words = []

while word != 'quit!':
    word = input().strip()
    if word == 'quit!':
        break
    if len(word) > 4 and word[-3:] and word[-3] not in ['a', 'e', 'i', 'o', 'u', 'y'] and word[-2:] == 'or':
        can_words.append(word[:-1] + 'u' + word[-1])
    else:
        can_words.append(word)

print('\n'.join(can_words))
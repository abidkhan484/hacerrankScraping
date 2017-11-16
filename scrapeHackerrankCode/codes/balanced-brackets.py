# Runtime Error
# Python 3

#!/bin/python3

import sys

def par_checker(s):
    length = len(s)
    if not length//2==length/2:
        return False
    l = ['(', '{', '[']
    r = [')', '}', ']']

    li = []
    for i in s:
        if i in r:
            break
        li.append(i)

    for i in range(length//2):
        for j in range(3):
            if l[j] == li[i]:
                break

        if not s[length-i-1]==r[j]:
            break

    else:
        return True

    return False


t = int(input().strip())
for a0 in range(t):
    s = input().strip()
    if par_checker(s) is True:
        print('YES')
    else:
        print('NO')


# Runtime Error
# Python 3

#!/bin/python3

import sys


g = int(input().strip())
for a0 in range(g):
    n,m,x = input().strip().split(' ')
    n,m,x = [int(n),int(m),int(x)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    a.reverse(); b.reverse()

    total = 0; count = 0
    while total <= x:
        if a[-1] > b[-1]:
            count += 1
            tmp = a.pop()
            total += tmp
        elif a[-1] <= b[-1]:
            count += 1
            tmp = b.pop()
            total += tmp

    print(count)


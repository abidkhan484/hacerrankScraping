# Accepted
# Python 3

#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    su = 0
    for i in a:
        if i<=0:
            su += 1
    if su < k:
        print('YES')
    else:
        print('NO')


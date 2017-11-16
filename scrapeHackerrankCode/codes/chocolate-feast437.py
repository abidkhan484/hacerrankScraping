# Terminated due to timeout
# Python 3

#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n,c,m = input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]

    count, temp = 0, n
    while temp:
        if temp != n:
            count += temp//m
            additional = temp%m
            temp = (temp//m) + additional
            if temp < m:
                break
        else:
            count += temp//c
            temp = temp//c

    print(count)


# Accepted
# Python 3

#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n,c,m = input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]

    count, temp, i = 0, n, 0
    while temp:
        if i != 0:
            count += temp//m
            additional = temp%m
            temp = (temp//m) + additional
            if temp < m:
                break
        else:
            count += temp//c
            temp = temp//c
            i += 1

    print(count)

